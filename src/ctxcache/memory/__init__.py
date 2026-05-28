"""CtxCache Memory subsystem: temporal structured facts with cache-friendly placement (BUILD_HANDBOOK §5.7)."""

from __future__ import annotations

from ctxcache.memory.checks import MemoryWriteError, validate_fact_write
from ctxcache.memory.recall import (
    get_default_memory_store,
    pin,
    recall,
    remember,
    set_default_memory_store,
)
from ctxcache.memory.store import Fact, MemoryStore

__all__ = [
    "Fact",
    "MemoryStore",
    "MemoryWriteError",
    "validate_fact_write",
    "remember",
    "recall",
    "pin",
    "get_default_memory_store",
    "set_default_memory_store",
]
