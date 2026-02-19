import asyncio
import json
from uuid import uuid4,UUID
from ai.barber_agent import get_barber_response
from db.db import get_redis, CHAT_SESSION_TTL
from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import BaseModel
from redis import asyncio as aioredis

router = APIRouter(prefix="/barbers")

class BarberChatSessionMessageRequest(BaseModel):
    prompt: str

@router.post("/chat-sessions", status_code=status.HTTP_201_CREATED)
async def create_barber_chat_session(redis: aioredis.Redis = Depends(get_redis)):
    """
    Create a new chat session for the barber agent.
    """
    session_id = str(uuid4()) 
    cache_key = f"session_messages:{session_id}"

    # Cache chat session with empty messages to initialize
    await redis.set(cache_key, json.dumps([]), ex=CHAT_SESSION_TTL)

    return {"session_id": session_id}

@router.post("/chat-sessions/{session_id}/messages")
async def create_barber_chat_session_message(
    session_id: UUID,
    query: BarberChatSessionMessageRequest,
    redis: aioredis.Redis = Depends(get_redis)
):
    """
    Ask the barber agent a question about haircuts or hair-related topics.

    Request body should contain a 'prompt' and 'session_id'.
    """
    cache_key = f"session_messages:{session_id}"

    # Load prior conversation from Redis
    cached = await redis.get(cache_key)
    if cached is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chat session not found"
        )
    prior_messages = json.loads(cached)

    result = await asyncio.to_thread(get_barber_response, query.prompt, prior_messages)

    # Cache updated message history
    await redis.set(cache_key, json.dumps(result["messages"]), ex=CHAT_SESSION_TTL)

    return {"response": result["response"]}

@router.delete("/chat-sessions/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_chat_session(session_id: str, redis: aioredis.Redis = Depends(get_redis)):
    """
    Delete a chat session and its history from Redis.

    This can be used to clear conversation history for a given session ID.
    """
    cache_key = f"session_messages:{session_id}"
    deleted_status = await redis.delete(cache_key)

    if deleted_status == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chat session not found"
        )