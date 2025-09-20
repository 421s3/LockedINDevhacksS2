import webScrapeASU.scraperHelper as sh
import asyncio

print("hello world")


async def schedule():
    x = await sh.get_schedule("CSE",240,2251)
    print(x)
asyncio.run(schedule())