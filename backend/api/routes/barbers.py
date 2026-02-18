import asyncio
import json
from ai.barber_agent import get_barber_response
from db.db import get_redis, CHAT_SESSION_TTL
from fastapi import APIRouter, Depends
from redis import asyncio as aioredis
from pydantic import BaseModel

router = APIRouter()

class AskBarberRequest(BaseModel):
    prompt: str
    session_id: str

@router.post("/barbers/ask")
async def ask_barber(query: AskBarberRequest, redis: aioredis.Redis = Depends(get_redis)):
    """
    Ask the barber agent a question about haircuts or hair-related topics.

    Request body should contain a 'prompt' and 'session_id'.
    """
    cache_key = f"session_messages:{query.session_id}"

    # Load prior conversation from Redis
    cached = await redis.get(cache_key)
    prior_messages = json.loads(cached) if cached else None

    result = await asyncio.to_thread(get_barber_response, query.prompt, prior_messages)

    # Cache updated message history
    await redis.set(cache_key, json.dumps(result["messages"]), ex=CHAT_SESSION_TTL)

    return {"response": result["response"]}
