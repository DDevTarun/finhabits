import requests
import json
import uuid

# The address of your locally running MCP server
MCP_SERVER_URL = "http://localhost:8080"

# --- CRITICAL CHANGE ---
# We generate ONE session ID and reuse it, just like a real user session.
# This ensures all our tool calls are part of the same login session.
SESSION_ID = f"mcp-session-{uuid.uuid4()}"
print(f"✅ New user session created. Session ID: {SESSION_ID}")


def _call_mcp_tool(tool_name: str, arguments: dict = None) -> dict:
    """Helper function to call a specific tool on the MCP server."""
    if arguments is None:
        arguments = {}
        
    print(f"🛠️ Calling MCP Tool '{tool_name}'...")
    
    try:
        # Headers now use our persistent session ID
        headers = {
            "Content-Type": "application/json",
            "Mcp-Session-Id": SESSION_ID
        }
        
        # --- CRITICAL CHANGE ---
        # Per the README's curl example, the 'arguments' field must be a
        # JSON object, NOT a string. The `json=` parameter handles this.
        request_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments # Pass the dictionary directly
            }
        }

        response = requests.post(
            f"{MCP_SERVER_URL}/mcp/stream",
            headers=headers,
            json=request_payload
        )
        response.raise_for_status()
        
        data = response.json()
        
        # --- CRITICAL CHANGE ---
        # Handle the two-step login flow
        if isinstance(data, dict) and data.get("status") == "login_required":
            login_url = data.get("login_url")
            print("\n" + "="*50)
            print("🚨 ACTION REQUIRED: Server requires login.")
            print(f"1. Open this URL in your browser: {login_url}")
            print("2. Enter a valid phone number (e.g., 1111111111) and any OTP.")
            print("3. After the browser shows 'Login Successful', run your request again.")
            print("="*50 + "\n")
            return {"status": "login_required", "message": "Please log in using the URL printed in the terminal."}

        return data
        
    except requests.exceptions.RequestException as e:
        return {"error": f"API request for tool '{tool_name}' failed: {e}"}

# The actual tool functions no longer need the user_id, as it's handled by the login step.
def fetch_net_worth() -> dict:
    """Fetches the comprehensive net worth for the logged-in user."""
    return _call_mcp_tool("fetch_net_worth")

def fetch_credit_report() -> dict:
    """Fetches the credit report and score for the logged-in user."""
    return _call_mcp_tool("fetch_credit_report")

def fetch_epf_details() -> dict:
    """Fetches the logged-in user's Employee Provident Fund (EPF) details."""
    return _call_mcp_tool("fetch_epf_details")

def fetch_mf_transactions() -> dict:
    """Fetches the logged-in user's mutual fund (MF) transaction history."""
    return _call_mcp_tool("fetch_mf_transactions")

def fetch_bank_transactions() -> dict:
    """Fetches the logged-in user's bank transaction history."""
    return _call_mcp_tool("fetch_bank_transactions")

def fetch_stock_transactions() -> dict:
    """Fetches the logged-in user's stock market transaction history."""
    return _call_mcp_tool("fetch_stock_transactions")