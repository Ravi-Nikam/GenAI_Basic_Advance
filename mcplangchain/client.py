from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
import asyncio
from dotenv import load_dotenv
load_dotenv()



async def main():    # Async (asynchronous) means a way for your code to pause while waiting for a slow task to finish, allowing the program to do other work in the meantime instead of freezing
    mcp_client = MultiServerMCPClient(
        {
            "math":{ # key value pair
                "command":"python", # command to run the python file
                "args":["mathserver.py"], # give relative path of the python file
                "transport":"stdio" # we are using stdio for communication
            },
            "weather":{
                "url":"http://localhost:8000/mcp", # url of the mcp server
                "transport": "streamable_http" # we are using streamable http for communication
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
    tools=await mcp_client.get_tools()  # this will give list of tools

    model = ChatGroq(
        model="openai/gpt-oss-20b"
    )

    agent = create_agent(
        model=model,
        tools=tools, 
        system_prompt="You are a helpful assistant."
    )
    """
    • async def: Defines a special function called a coroutine that can pause and resume.
    • await: Tells Python to pause the current task and switch to other work while waiting for a result.
    
    """
    response = await agent.ainvoke({
        "messages": [{"role":"user","content":"what is (3 + 5) * 9 "}]
    })
    print("math response ",response['messages'][-1].content)
    # for m in response["messages"]:
    #     m.pretty_print()

    response=await agent.ainvoke({
        "messages":[{"role":"user","content":"What is the whether of Ahmedabad ? "}]
    })

    print("weather response ",response['messages'][-1].content)


if __name__ == "__main__":
    asyncio.run(main())