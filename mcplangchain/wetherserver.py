from mcp.server.fastmcp import FastMCP


mcp=FastMCP("wether")

@mcp.tool()
async def get_wether(city:str)->str:
    """ get the wether of the city 
        city  is the name of the city
    """
    return f"the wether of {city} is sunny"

if __name__ =="__main__":
    print(mcp.run(transport="streamable-http"))
