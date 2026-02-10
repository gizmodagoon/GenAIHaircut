# GenAIHaircut Backend

This backend service powers the GenAI Haircut application, providing haircut analysis and recommendations using Claude AI.

## Modules

The backend consists of two main modules:

### 1. API Module (`/api`)

FastAPI-based REST API that provides endpoints for:
- Getting haircut information
- Analyzing haircuts using Claude AI

### 2. AI Module (`/ai`)

Claude AI integration using the Strands Python SDK:
- Haircut analysis capabilities
- Claude Sonnet 4.5 model integration via Anthropic API
- Example scripts for testing

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

### POST `/haircuts/analyze`
Analyzes a haircut query using Claude AI.

Request body:
```json
{
  "prompt": "What haircut would suit a round face?"
}
```

## Testing the API

You can test the endpoint using curl:

```bash
curl -X POST "http://127.0.0.1:8000/haircuts/analyze" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What haircuts look good on Asians?"}'
```

This will return a JSON response with the AI's analysis of the prompt.

## Direct AI Usage

You can also use the AI module directly in your code:

```python
from ai.claude_agent import get_haircut_analysis

result = get_haircut_analysis("What haircut would suit a round face?")
print(result["analysis"])
```

Or use the agent directly:
```python
from ai.claude_agent import create_haircut_agent

agent = create_haircut_agent()
response = agent("What haircut would suit a round face?")
print(response)
```

## Testing the AI Module

```bash
# From the backend directory
python -m ai.example
```

## Anthropic API Access

Ensure you have a valid Anthropic API key with access to the Claude Sonnet 4.5 model. You can obtain one at [console.anthropic.com](https://console.anthropic.com).
