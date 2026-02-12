from fastmcp import FastMCP

app = FastMCP("My MCP Server")
# 提供一個加法工具
@app.tool()
def add(n1:int, n2:int) -> int:
    """Add two numbers"""
    return n1 + n2