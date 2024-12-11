from bs4 import BeautifulSoup
import aiohttp
from utils.models import TitleLink
import asyncio
import lxml

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Edge/118.0",
            "Referer": "https://metanit.com",  # Укажите, с какой страницы должен быть переход
}

async def parse_titles(soup: BeautifulSoup, base_url: str) -> list[TitleLink]:
    title_elements = soup.find('ol', class_='content')
    a_elements = title_elements.find_all('a')
    return [TitleLink(title=a.get_text(), link= base_url + a['href']) for a in a_elements]

async def get_titles(url: str) -> list[TitleLink]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if not response.ok:
                raise Exception ("Неккоректный url")
            html_content = await response.text()
            soup = BeautifulSoup(html_content, "lxml")
            return await parse_titles(soup, base_url=url)

async def parse_text_from_title(soup: BeautifulSoup) -> str:
    return soup.find('div', class_='item center menC').get_text().strip()


async def get_info_from_title(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if not response.ok:
                raise Exception("Неккоректный url")
            html_content = await response.text()
            soup = BeautifulSoup(html_content, "lxml")
            return await parse_text_from_title(soup)

async def main():
    titles = await get_titles('https://metanit.com/cpp/qt/')
    for title in titles:
        print(f'Тема: {title.title} : {title.link}')
    text = await get_info_from_title('https://metanit.com/cpp/qt/1.2.php')
    print(text)

if __name__ == "__main__":
    asyncio.run(main())
