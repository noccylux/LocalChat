# File: localchat/stt/base.py

from abc import ABC, abstractmethod
from typing import Any, Generator


class BaseSTT(ABC):
    """语音转文本模型的基类。"""

    @abstractmethod
    def __init__(self, model_name: str, device: str = "cuda", **kwargs):
        """
        初始化STT模型。

        Args:
            model_name: 要使用的模型名称或路径
            device: 运行模型的设备
            **kwargs: 其他模型特定参数
        """
        pass

    @abstractmethod
    def transcribe(self, audio: Any) -> str:
        """
        将音频转录为文本。

        Args:
            audio: 要转录的音频数据

        Returns:
            转录的文本
        """
        pass

    @abstractmethod
    def stream_transcribe(self, audio_stream) -> Generator[str, None, None]:
        """
        以流式方式转录音频。

        Args:
            audio_stream: 音频数据流

        Yields:
            转录的文本段
        """
        pass