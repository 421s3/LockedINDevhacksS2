import webScrapeASU.scraperHelper as sh
import asyncio



classType = input("Please enter 3 digit class type")
classNumber = input("Please enter 3 digit class number")
classTerm = input("Please enter class term, in format 2XXY with XX being the last 2 digits of the year and Y being the term (1 is fall, 4 is summer, and 7 is spring)")
async def schedule():
    x = await sh.get_schedule(classType,classNumber,classTerm)
asyncio.run(schedule())