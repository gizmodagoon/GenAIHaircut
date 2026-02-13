# GenAIHaircut Backend

This backend service powers the GenAI Haircut application, providing haircut analysis and recommendations using Claude AI.

## Modules

The backend consists of two main modules:

### 1. API Module (`/api`)

FastAPI-based REST API that provides endpoints for:
- Getting haircut information
- Analyzing haircuts using Claude AI

### 2. AI Module (`/ai`)

Claude AI integration using the Strands Agents SDK:
- Barber Agent powered by Claude Sonnet 4.5 via Anthropic API
- Web search capabilities via Tavily tools (search, extract, crawl, map)

## Setup

1. Ensure you have the required packages installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your Anthropic API key:

   ```bash
   export ANTHROPIC_API_KEY=your_api_key
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

### GET `/haircuts`
Returns a list of available haircuts.

### POST `/haircuts/ask`
Ask the barber agent a question about haircuts or hair-related topics.

Request body:
```json
{
  "prompt": "What haircut would suit a round face?"
}
```

## Testing the API

You can test the endpoint using curl:

```bash
curl -X POST "http://127.0.0.1:8000/haircuts/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What haircuts look good on Asians?"}'
```

This will return a JSON response with the barber agent's response.

## Direct AI Usage

You can also use the AI module directly in your code:

```python
from ai.barber_agent import get_barber_response

result = get_barber_response("What haircut would suit a round face?")
print(result["response"])
```

Or use the agent directly:
```python
from ai.barber_agent import create_barber_agent

agent = create_barber_agent()
response = agent("What haircut would suit a round face?")
print(response)
```

## Anthropic API Access

Ensure you have a valid Anthropic API key with access to the Claude Sonnet 4.5 model. You can obtain one at [console.anthropic.com](https://console.anthropic.com).
