import webScrapeASU.scheduleScraper as schedule_scraper




async def get_schedule(subject: str, course_number: int, term: int):
    schedule = await schedule_scraper.parse_classes(subject, course_number, term)
    if not schedule:
        return {"error": "No classes found"}
    return schedule