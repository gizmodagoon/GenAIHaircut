# GenAIHaircut Backend

This backend service powers the GenAI Haircut application, providing haircut analysis and recommendations using Claude AI.

## Modules

The backend consists of three main modules:

### 1. API Module (`/api`)

FastAPI-based REST API that provides endpoints for:
- Asking the barber agent hair-related questions
- Analyzing haircut images using Claude AI
- CRUD operations for haircuts (backed by PostgreSQL)

### 2. AI Module (`/ai`)

Claude AI integration using the Strands Agents SDK:
- Barber Agent powered by Claude Sonnet 4.5 via Anthropic API
- Web search capabilities via Tavily tools (search, extract, crawl, map)
- Haircut image analysis agent

### 3. Database Module (`/db`)

PostgreSQL database layer using SQLAlchemy (async) with Alembic migrations:
- Async session management via `asyncpg`
- `Haircut` model with CRUD operations
- Alembic for schema migrations
- Redis integration for chat session caching

## Setup

1. Ensure you have the required packages installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the `api/` directory with the following variables:

   ```env
   ANTHROPIC_API_KEY=your_anthropic_api_key
   DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/app
   TAVILY_API_KEY=your_tavily_api_key
   REDIS_URL=redis://localhost:6379
   ```

3. Run PostgreSQL:

   ```bash
   docker run --name fastapi-postgres \
     -e POSTGRES_USER=postgres \
     -e POSTGRES_PASSWORD=postgres \
     -e POSTGRES_DB=app \
     -p 5432:5432 \
     -d postgres:16
   ```

4. Run Redis:

   ```bash
   docker run --name fastapi-redis \
     -p 6379:6379 \
     -d redis:7
   ```

5. Run Alembic migrations:

   ```bash
   alembic upgrade head
   ```

## Alembic Migrations

To sync local model changes with the PostgreSQL database:

```bash
alembic revision --autogenerate -m "describe your change"
alembic upgrade head
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn api.main:app --reload
```

Once the server is running, you can access the API at:
```
http://127.0.0.1:8000/
```

You can also view the interactive API documentation at:
```
http://127.0.0.1:8000/docs
```

## API Endpoints

### POST `/barbers/chat-sessions`
Create a new chat session. Returns a `session_id` used for subsequent messages.

Response:
```json
{
  "session_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

### POST `/barbers/chat-sessions/{session_id}/messages`
Send a message to the barber agent within an existing chat session. Conversation history is maintained per session via Redis.

Request body:
```json
{
  "prompt": "What haircut would suit a round face?"
}
```

### DELETE `/barbers/chat-sessions/{session_id}`
Delete a chat session and its conversation history from Redis.

### POST `/haircuts/analysis`
Analyze a haircut image using Claude AI.

Request body:
```json
{
  "image": "<base64-encoded image or URL>"
}
```

### POST `/haircuts`
Create a new haircut record in the database.

Request body:
```json
{
  "style": "mid fade"
}
```

### GET `/haircuts`
Returns all haircut records from the database.

## Testing the API

Once the server is running, open the interactive Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test all endpoints directly from your browser.

## API Keys

- **Anthropic**: Obtain an API key with access to Claude Sonnet 4.5 at [console.anthropic.com](https://console.anthropic.com)
- **Tavily**: Obtain an API key for web search at [tavily.com](https://tavily.com)
