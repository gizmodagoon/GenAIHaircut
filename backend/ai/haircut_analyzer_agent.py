from strands import Agent
from strands.models.anthropic import AnthropicModel
from typing import Dict, Any
import os

# Define attributes for tracing
trace_attributes = {
    "project": "GenAIHaircut",
    "user": "haircut-assistant"
}

def create_haircut_agent() -> Agent:
    """
    Create and configure a Claude agent for haircut analysis.

    Requires ANTHROPIC_API_KEY environment variable to be set.

    Returns:
        Configured Strands Agent instance
    """
    system_prompt = """
        You are a haircut analysis expert. Analyze haircut requests and provide insights.

        When analyzing haircuts, consider:
        1. Style characteristics
        2. Technique used
        3. Suitability for different face shapes
        4. Maintenance requirements

        Provide your analysis in a clear, structured format.
    """

    model = AnthropicModel(
        client_args={"api_key": os.environ.get("ANTHROPIC_API_KEY")},
        model_id="claude-sonnet-4-5-20250929",
        max_tokens=1024,
    )

    agent = Agent(
        system_prompt=system_prompt,
        name="Haircut Analysis Agent",
        model=model,
        trace_attributes=trace_attributes
    )

    return agent

def get_haircut_analysis(prompt: str) -> Dict[str, Any]:
    """
    Get haircut analysis from the Claude agent.
    
    Args:
        prompt: User's question or request about haircuts
        
    Returns:
        Response from the Claude agent
    """
    agent = create_haircut_agent()
    
    # Ask the agent the question
    response = agent(prompt)
    
    # Extract and return the response
    return {
        "response": str(response),
    }
