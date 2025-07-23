from google.adk.agents import Agent
from .mcp_tools import get_all_my_details,fetch_net_worth, logout_and_start_new_session

fi_mcp_agent = Agent(
    name="fi_mcp_agent",
    model="gemini-1.5-flash",
    description="Fetches a user's complete financial profile from the MCP server after they log in.",
    instruction="""
You have two primary functions:
1.  When the user asks to "get my details", call the `get_all_my_details` tool.
2.  When the user wants to "logout", "log in as someone else", or "start a new session", call the `logout_and_start_new_session` tool.

**Handling Login:**
If the `get_all_my_details` tool returns a JSON string containing `{"status": "login_required"}`, you must extract the `login_url` and `message` from it. Present this to the user in a clear, helpful way. For example: "To continue, please log in here: [URL]. Once you are done, please make your request again."

**Handling Data:**
If the tool returns any other JSON, provide the raw, unmodified JSON string as your final answer. Do not summarize or change it.
""",
    tools=[get_all_my_details,fetch_net_worth, logout_and_start_new_session],
)