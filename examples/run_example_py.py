from localchat import StreamingPipeline

pipeline = StreamingPipeline(
    stt_model="whisper-large-v3",
    llm_model="ollama://mistral:7b",
    tts_model="your-preferred-model"
)

pipeline.run()