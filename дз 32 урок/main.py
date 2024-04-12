import asyncio

async def red_light():
    print("Красный свет")
    await asyncio.sleep(5)

async def yellow_light():
    print("Жёлтый свет")
    await asyncio.sleep(2)

async def green_light():
    print("Зелёный свет")
    await asyncio.sleep(5)

async def traffic_light():
    while True:
        await asyncio.gather(
            red_light(),
            asyncio.sleep(5),
            yellow_light(),
            asyncio.sleep(2),
            green_light(),
            asyncio.sleep(5)
        )

asyncio.run(traffic_light())
