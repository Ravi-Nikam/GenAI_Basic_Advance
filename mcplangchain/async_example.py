import asyncio

async def task1():
    print("Task 1 शुरू")
    await asyncio.sleep(3)
    print("Task 1 पूरा")

async def task2():
    print("Task 2 शुरू")
    await asyncio.sleep(2)
    print("Task 2 पूरा")

async def main():
    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())