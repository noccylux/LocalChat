# File: localchat/core/__init__.py

from localchat.llm.base import BaseLLM
from localchat.llm.factory import create_llm_model

__all__ = ["BaseLLM", "create_llm_model"]
