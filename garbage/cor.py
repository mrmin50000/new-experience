async def rocket():
    print(1)
    await asyncio.sleep(1)
    print(2)
    await asyncio.sleep(1)
    print(3)
    await asyncio.sleep(1)
    print("Go!")

await rocket()
