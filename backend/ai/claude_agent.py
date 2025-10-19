from strands import Agent
from typing import Dict, Any
import os

# Define attributes for tracing
trace_attributes = {
    "project": "GenAIHaircut",
    "user": "haircut-assistant"
}

# AWS client configuration for Claude access via Bedrock
# These environment variables should be set in the deployment environment
AWS_REGION = os.environ.get("AWS_REGION", "us-west-2")

def create_haircut_agent() -> Agent:
    """
    Create and configure a Claude agent for haircut analysis.
    
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
    
    agent = Agent(
        system_prompt=system_prompt,
        name="Haircut Analysis Agent",
        model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
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
        "analysis": response,
    }
