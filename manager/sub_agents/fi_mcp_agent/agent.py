from google.adk.agents import Agent

# Import all the tools
from .mcp_tools import (
    fetch_net_worth,
    fetch_credit_report,
    fetch_epf_details,
    fetch_mf_transactions,
    fetch_bank_transactions,
    fetch_stock_transactions
)

# Create a list containing all the tool functions
all_mcp_tools = [
    fetch_net_worth,
    fetch_credit_report,
    fetch_epf_details,
    fetch_mf_transactions,
    fetch_bank_transactions,
    fetch_stock_transactions
]

fi_mcp_agent = Agent(
    name="fi_mcp_agent",
    model="gemini-1.5-flash",
    description="Fetches and manages a user's financial data from the Fi MCP server after they have logged in.",
    
    # --- Start of Corrected Instructions ---
    instruction="""
You are a financial assistant agent that retrieves data from the Fi MCP server.
- The user must first log in. The tools will handle the login process.
- If a tool call response indicates that login is required, inform the user that they need to follow the login URL printed in the terminal.
- Once logged in, you can use the tools to answer questions about the user's financial data.
- You DO NOT need to ask the user for a user_id.
""",
    # --- End of Corrected Instructions ---

    tools=all_mcp_tools,
)