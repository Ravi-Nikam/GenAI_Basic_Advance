
from mcp.server.fastmcp import FastMCP

mcp=FastMCP("math")

@mcp.tool()
def add(a:int,b:int)->int:
    """  addition of two number 
        a  is number 1 
        b is secound number
    """
    return a+b

@mcp.tool()
def mul(a:int,b:int)->int:
    """ multiplication of two number 
        a  is number 1 
        b is secound number
    """
    return a*b
    
if __name__ =="__main__":
    print(mcp.run(transport="stdio"))