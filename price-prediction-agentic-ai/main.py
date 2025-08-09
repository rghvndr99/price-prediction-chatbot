# server.py
from mcp.server.fastmcp import FastMCP
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import loadModel, get_price

# Create an MCP server
mcp = FastMCP("price-prediction-agentic-ai")

#load modal
loadModel()


# Add an addition tool
@mcp.tool()
def sum(a: int, b: int) -> int:
    """Add two numbers"""
    return a * b

# Get the price of area based on number of bedrooms, location and bathroom
@mcp.tool()
def housePrice(location: str, bedrooms: int, bathrooms:int,area: int) -> float:
    """use number of bedrooms, no of bathrooms and location to get the price of houses"""
    return get_price(location, area, bedrooms, bathrooms)


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"