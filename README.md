# LocalChat
A realtime local LLM voice chat lib.

## 🚀 Project Overview
This project is a local real-time voice assistant that combines STT, LLM, and TTS to enable natural voice conversations. It supports both English and Chinese and is optimized for low latency and smooth interaction. Runs fully offline on consumer GPUs (e.g., RTX 4090).

## 🧠 Features
- Real-time speech-to-text using Whisper
- Fast local LLM replies (e.g., Baichuan 13B via Ollama)
- Streamable text-to-speech output with Coqui TTS
- Interruption handling (AI can be interrupted while speaking)
- Python-based, modular architecture (PyTorch)

## ⚙️ Tech Stack
- STT: Whisper / Faster-Whisper
- LLM: Baichuan / LLaMA / ChatGLM (via Ollama)
- TTS: Coqui XTTS / Piper
- Framework: Python + PyTorch


## 📂 Project Structure
    LocalChat/               # Top-level directory
    ├── localchat/           # Codebase
    │   ├── __init__.py
    │   ├── core/
    │   ├── stt/
    │   ├── llm/
    │   ├── tts/
    │   └── utils/
    ├── examples/            # Examples
    │   ├── simple_cli.py
    │   └── advanced_config.py
    ├── tests/               # Unit tests
    ├── docs/                # Documentation
    ├── setup.py             # Installer
    ├── pyproject.toml       # Python package metadata
    ├── README.md            # We are here
    └── LICENSE