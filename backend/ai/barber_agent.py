from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands_tools.tavily import (
    tavily_search, tavily_extract, tavily_crawl, tavily_map
)
from typing import Dict, Any
import os

# Define attributes for tracing
trace_attributes = {
    "project": "GenAIHaircut",
    "user": "haircut-assistant"
}

def create_barber_agent() -> Agent:
    """
    Create and configure a Claude agent for haircut analysis.

    Requires ANTHROPIC_API_KEY environment variable to be set.

    Returns:
        Configured Strands Agent instance
    """
    system_prompt = """
        You are a knowledgable barber that is responsible for answering a single question at a time related to barbers, haircuts or something to do with hair.

        When responding to haircuts or hair related questions, please respond in a clear, structured format as it will be rendered on a website. 
        
        If the question does not relate haircuts or hair related questions, please respond with "Sorry, I can only answer questions related to haircuts or hair related questions."
    """

    model = AnthropicModel(
        client_args={"api_key": os.environ.get("ANTHROPIC_API_KEY")},
        model_id="claude-sonnet-4-5-20250929",
        max_tokens=1024)

    agent = Agent(
        system_prompt=system_prompt,
        name="Barber Agent",
        model=model,
        trace_attributes=trace_attributes,
        tools=[tavily_search,tavily_extract, tavily_crawl, tavily_map]
    )

    return agent

def get_barber_response(prompt: str) -> Dict[str, Any]:
    """
    Get questions answered by the barber agent.
    
    Args:
        prompt: User's question or request about haircuts
        
    Returns:
        Response from the barber agent
    """
    agent = create_barber_agent()
    
    # Ask the agent the question
    response = agent(prompt)

    # Extract and return the response
    return {
        "response": str(response),
    }
