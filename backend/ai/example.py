# Import claude_agent
from claude_agent import create_haircut_agent, get_haircut_analysis

def example_usage():
    # Example 1: Use the agent directly
    agent = create_haircut_agent()
    response = agent("What haircut style would you recommend for someone with a round face who wants low maintenance?")
    print("Direct agent response:")
    print(response)
    print("\n" + "-"*50 + "\n")
    
    # Example 2: Use the helper function
    result = get_haircut_analysis(
        "Can you explain the difference between a fade and a taper haircut?"
    )
    print("Helper function response:")
    print(result["analysis"])

if __name__ == "__main__":
    # Run the example
    example_usage()
