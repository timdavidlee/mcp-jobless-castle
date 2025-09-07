from mcp.server.fastmcp
import FastMCP

mcp = FastMCP("ad-pricing-service")


@mcp.tool()
def greet(name: str) -> str:
    """Greets the given name."""
    return f"Hello, {name}!"


if __name__ == '__main__':
    mcp.run()