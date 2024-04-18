import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def parse_book():
    url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                web_content = await response.text()
                beautiful_parse = BeautifulSoup(web_content, 'html.parser')
                title = beautiful_parse.find('h1').text
                description = beautiful_parse.find('p').text
                availability = beautiful_parse.find('p', class_='instock availability').text
                img_url = beautiful_parse.find('img')['src']
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"Availability: {availability}")
                print(f"Image URL: {img_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    await parse_book()

if __name__ == "__main__":
    asyncio.run(main())
