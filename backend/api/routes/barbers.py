from pydantic import BaseModel
from ai.barber_agent import get_barber_response
from fastapi import APIRouter

router = APIRouter()

class AskBarberRequest(BaseModel):
    prompt: str

@router.post("/barbers/ask")
def ask_barber(query: AskBarberRequest):
    """
    Ask the barber agent a question about haircuts or hair-related topics.
    
    Request body should contain a 'prompt' field with the user's question or request.
    """
    result = get_barber_response(query.prompt)
    return result