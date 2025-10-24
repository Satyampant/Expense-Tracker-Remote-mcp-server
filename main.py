from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Expense-Tracker")

@mcp.tool
async def add(a:int, b:int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool
async def random_number(min_val: int=1, max_val: int=100) -> int:
    """Generate random number within a range"""
    return random.randint(min_val, max_val)

@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server"""
    info = {
        "name": "Simple Calculator server",
        "version": "1.0.0",
        "description": "A basic mcp server with math tools"
    }
    return json.dumps(info, indent=2)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
