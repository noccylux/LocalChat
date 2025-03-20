# File: localchat/tts/base.py

from abc import ABC, abstractmethod
from typing import Any, Generator


class BaseTTS(ABC):
    """文本转语音模型的基类。"""

    @abstractmethod
    def __init__(self, model_name: str, device: str = "cuda", **kwargs):
        """
        初始化TTS模型。

        Args:
            model_name: 要使用的模型名称或路径
            device: 运行模型的设备
            **kwargs: 其他模型特定参数
        """
        pass

    @abstractmethod
    def synthesize(self, text: str, **kwargs) -> Any:
        """
        将文本合成为语音。

        Args:
            text: 要合成的文本
            **kwargs: 其他合成参数

        Returns:
            音频数据
        """
        pass

    @abstractmethod
    def stream_synthesize(self, text_stream: Generator[str, None, None], **kwargs) -> Generator[Any, None, None]:
        """
        以流式方式将文本合成为语音。

        Args:
            text_stream: 文本段流
            **kwargs: 其他合成参数

        Yields:
            合成的音频段
        """
        pass