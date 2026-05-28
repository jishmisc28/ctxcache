"""LangChain integration alias for CtxCache prompt caching (BUILD_HANDBOOK §4.2, §6.1)."""

from __future__ import annotations

from ctxcache.integrations.langgraph import CtxCacheMiddleware

__all__ = ["CtxCacheMiddleware"]
