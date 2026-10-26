# ChronoAI ⏱️🗣️
> Real-time acoustic speaker diarization, emotion tracking, and autonomous action delegation to Linear & Jira.

## 🚀 Overview
ChronoAI is an intelligent meeting co-pilot connecting via WebRTC. It diarizes speakers using pyannote.audio, tracks conversational sentiment trends, automatically extracts action items with assignees, and syncs deliverables to Linear, Jira, and Notion.

## 🛠️ Tech Stack
- **Audio Diarization**: pyannote.audio, faster-whisper, WebRTC, PipeWire
- **Intelligence**: Mistral-Large, LangChain, Celery, Redis
- **Integrations**: Linear GraphQL API, Jira REST API, Notion SDK

## ⚡ Quick Start (Arch Linux)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8000 --reload
```
