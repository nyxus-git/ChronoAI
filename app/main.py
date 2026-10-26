from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="ChronoAI Meeting Intelligence", version="1.0.0")

class ActionItem(BaseModel):
    task: str
    owner: str
    integration: str

@app.get("/")
def index():
    return {"status": "active", "service": "ChronoAI Realtime Diarization"}

@app.get("/api/meetings/summary")
def get_sample_summary():
    return {
        "meeting_title": "Product Architecture Review",
        "duration": "42:15",
        "speakers": ["Alex", "Sarah", "David"],
        "sentiment": "Positive (84%)",
        "action_items": [
            {"task": "Finalize Q3 roadmap", "owner": "Sarah", "integration": "Linear"},
            {"task": "Draft press release", "owner": "Alex", "integration": "Linear"}
        ]
    }
