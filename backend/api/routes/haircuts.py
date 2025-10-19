from fastapi import APIRouter, Body
from typing import Dict, Any
from ai.claude_agent import get_haircut_analysis

router = APIRouter()

@router.get("/haircuts")
def get_haircuts():
    return [
        {"id": 1, "style": "mid fade"},
        {"id": 2, "style": "layered cut"}
    ]

@router.post("/haircuts/analyze")
def analyze_haircut(query: Dict[str, Any] = Body(...)):
    """
    Analyze a haircut query using Claude AI.
    
    Request body should contain a 'prompt' field with the user's question or request.
    """
    prompt = query.get("prompt", "")
    if not prompt:
        return {"error": "Prompt is required"}
    
    result = get_haircut_analysis(prompt)
    return result
