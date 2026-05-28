"""CtxCache framework integrations (Pydantic AI, OpenAI Agents SDK, LangGraph)."""

from __future__ import annotations

from ctxcache.integrations.langchain import CtxCacheMiddleware as LangChainMiddleware
from ctxcache.integrations.langgraph import CtxCacheMiddleware
from ctxcache.integrations.openai_agents import set_default_openai_client, wrap_agents_client
from ctxcache.integrations.pydantic_ai import CtxCachePydanticAIModel, wrap_pydantic_ai_client

__all__ = [
    "CtxCacheMiddleware",
    "LangChainMiddleware",
    "wrap_pydantic_ai_client",
    "CtxCachePydanticAIModel",
    "set_default_openai_client",
    "wrap_agents_client",
]
