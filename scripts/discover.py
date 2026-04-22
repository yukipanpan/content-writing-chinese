"""
discover.py — Auto-discover source URLs from a topic/keyword.

Uses DuckDuckGo by default (free, no API key needed).
Set SEARCH_API_KEY to a Serper.dev key for Google-quality results.
Set BRAVE_API_KEY for Brave Search.

Usage:
  from discover import discover_urls
  urls = discover_urls(topic="Polkadot JAM upgrade", intent="analytical piece", n=5)
"""

import os
import sys
from urllib.parse import urlparse

# ── Domain blocklist ──────────────────────────────────────────────────────────
# These domains are filtered out from auto-discovered results.
# YouTube and Twitter/X are handled separately by fetcher.py.

BLOCKLIST = {
    "twitter.com", "x.com",
    "youtube.com", "youtu.be",
    "facebook.com", "instagram.com", "tiktok.com", "linkedin.com",
    "coinmarketcap.com", "coingecko.com",  # price aggregators, not articles
}


def _is_allowed(url: str) -> bool:
    try:
        domain = urlparse(url).netloc.lower().removeprefix("www.")
        return not any(domain == b or domain.endswith("." + b) for b in BLOCKLIST)
    except Exception:
        return True


# ── Search backends ───────────────────────────────────────────────────────────

def _search_duckduckgo(query: str, n: int) -> list[str]:
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        sys.exit(
            "duckduckgo-search not installed. Run: pip install duckduckgo-search\n"
            "Or set SEARCH_API_KEY (Serper) for Google results."
        )
    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=n * 3):
                url = r.get("href", "")
                if url and _is_allowed(url):
                    results.append(url)
                    if len(results) >= n:
                        break
    except Exception as e:
        print(f"  ⚠ DuckDuckGo search failed: {e}", file=sys.stderr)
    return results


def _search_serper(query: str, n: int) -> list[str]:
    import requests
    api_key = os.environ.get("SEARCH_API_KEY")
    try:
        resp = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
            json={"q": query, "num": min(n * 2, 20)},
            timeout=15,
        )
        resp.raise_for_status()
        urls = []
        for item in resp.json().get("organic", []):
            url = item.get("link", "")
            if url and _is_allowed(url):
                urls.append(url)
                if len(urls) >= n:
                    break
        return urls
    except Exception as e:
        print(f"  ⚠ Serper search failed: {e} — falling back to DuckDuckGo", file=sys.stderr)
        return _search_duckduckgo(query, n)


def _search_brave(query: str, n: int) -> list[str]:
    import requests
    api_key = os.environ.get("BRAVE_API_KEY")
    try:
        resp = requests.get(
            "https://api.search.brave.com/res/v1/web/search",
            headers={"Accept": "application/json", "X-Subscription-Token": api_key},
            params={"q": query, "count": min(n * 2, 20)},
            timeout=15,
        )
        resp.raise_for_status()
        urls = []
        for item in resp.json().get("web", {}).get("results", []):
            url = item.get("url", "")
            if url and _is_allowed(url):
                urls.append(url)
                if len(urls) >= n:
                    break
        return urls
    except Exception as e:
        print(f"  ⚠ Brave search failed: {e} — falling back to DuckDuckGo", file=sys.stderr)
        return _search_duckduckgo(query, n)


def _search(query: str, n: int) -> list[str]:
    """Pick backend based on available API keys."""
    if os.environ.get("SEARCH_API_KEY"):
        print(f"  searching (Serper/Google): {query!r}", file=sys.stderr)
        return _search_serper(query, n)
    if os.environ.get("BRAVE_API_KEY"):
        print(f"  searching (Brave): {query!r}", file=sys.stderr)
        return _search_brave(query, n)
    print(f"  searching (DuckDuckGo): {query!r}", file=sys.stderr)
    return _search_duckduckgo(query, n)


# ── Query construction ────────────────────────────────────────────────────────

def _build_queries(topic: str, intent: str) -> list[str]:
    """
    Build 1-2 English search queries from topic + intent.
    Primary query: the topic as-is.
    Secondary query: topic + key words extracted from intent (if they add information).
    """
    queries = [topic]

    # Extract meaningful words from intent (length > 4, not stop words)
    stop = {"write", "piece", "about", "article", "chinese", "english",
            "audience", "readers", "based", "from", "with", "that", "this",
            "what", "make", "into", "analytical", "tutorial", "summary"}
    extra = " ".join(
        w for w in intent.lower().split()
        if len(w) > 4 and w not in stop
    )[:60]

    if extra and extra.lower() not in topic.lower():
        queries.append(f"{topic} {extra}")

    return queries


# ── Public interface ──────────────────────────────────────────────────────────

def discover_urls(topic: str, intent: str = "", n: int = 5) -> list[str]:
    """
    Discover relevant source URLs for a topic.

    Args:
        topic:  English search topic / keyword phrase
        intent: Optional intent description — used to enrich the search query
        n:      Number of URLs to return (default 5)

    Returns:
        Deduplicated list of URLs, filtered by domain quality.
    """
    queries = _build_queries(topic, intent)
    per_query = max(3, (n // len(queries)) + 2)

    seen: set[str] = set()
    urls: list[str] = []

    for query in queries:
        for url in _search(query, per_query):
            if url not in seen:
                seen.add(url)
                urls.append(url)
                if len(urls) >= n:
                    return urls

    return urls[:n]
