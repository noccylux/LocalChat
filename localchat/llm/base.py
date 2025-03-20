# File: localchat/llm/base.py

from abc import ABC, abstractmethod
from typing import Generator


class BaseLLM(ABC):
    """语言模型的基类。"""

    @abstractmethod
    def __init__(self, model_name: str, device: str = "cuda", **kwargs):
        """
        初始化语言模型。

        Args:
            model_name: 要使用的模型名称或路径
            device: 运行模型的设备
            **kwargs: 其他模型特定参数
        """
        pass

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        为给定提示生成响应。

        Args:
            prompt: 要处理的输入文本
            **kwargs: 其他生成参数

        Returns:
            生成的文本响应
        """
        pass

    @abstractmethod
    def stream_generate(self, prompt: str, **kwargs) -> Generator[str, None, None]:
        """
        以流式方式生成响应。

        Args:
            prompt: 要处理的输入文本
            **kwargs: 其他生成参数

        Yields:
            生成的文本段
        """
        pass