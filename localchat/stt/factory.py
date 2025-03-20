# File: localchat/stt/factory.py

def create_stt_model(model_name: str, device: str = "cuda", **kwargs):
    """
    创建指定名称的STT模型实例。

    Args:
        model_name: 模型名称或标识符
        device: 运行设备
        **kwargs: 附加参数

    Returns:
        BaseSTT的实例
    """
    # 根据model_name选择合适的模型实现
    if model_name.startswith("whisper-"):
        from localchat.stt.whisper import WhisperSTT
        return WhisperSTT(model_name, device=device, **kwargs)
    # 可以添加更多模型类型
    else:
        raise ValueError(f"不支持的STT模型: {model_name}")