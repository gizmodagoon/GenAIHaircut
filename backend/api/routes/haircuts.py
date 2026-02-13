from fastapi import APIRouter
from pydantic import BaseModel
from ai.barber_agent import get_barber_response
from ai.haircut_analyzer_agent import get_haircut_analysis

router = APIRouter()

class AskBarberRequest(BaseModel):
    prompt: str

class AnalyzeHaircutRequest(BaseModel):
    image: str
    
@router.get("/haircuts")
def get_haircuts():
    return [
        {"id": 1, "style": "mid fade"},
        {"id": 2, "style": "layered cut"}
    ]

@router.post("/haircuts/ask")
def ask_barber(query: AskBarberRequest):
    """
    Ask the barber agent a question about haircuts or hair-related topics.
    
    Request body should contain a 'prompt' field with the user's question or request.
    """
    result = get_barber_response(query.prompt)
    return result

@router.post("/haircuts/analyze")
def analyze_haircut(query: AnalyzeHaircutRequest):
    """
    Analyze a haircut query using Claude AI.
    
    Request body should contain a 'image' field with represents the haircut to analyze.
    """
    result = get_haircut_analysis(query.image)
    return result
