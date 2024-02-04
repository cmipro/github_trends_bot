import asyncio
from typing import Optional

import aiohttp

from bs4 import BeautifulSoup, ResultSet, Tag

from config_data import config
from config_data.config import project_dao, GITHUB_URLS, GITHUB_BASE_URL
from services.structures import ProjectInfo
from utils.telegram_sender import send_message_to_channel


async def find_new_projects() -> None:
    """Finding new projects in GitHub trends."""
    for url in GITHUB_URLS:
        soup = await get_soup(url[0])
        projects = await get_projects(soup)
        for project in projects:
            project_info = await get_project_info(project)
            if project_dao.check_project_exists(project_info.header):
                continue
            await send_message_to_channel(project_info, url[1])
            project_dao.add_project(project_info.header)


async def get_soup(url: str) -> Optional[BeautifulSoup]:
    """Get Response from url."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            html = await response.text()
            soup = BeautifulSoup(html, 'lxml')
            return soup


async def get_projects(soup: BeautifulSoup) -> ResultSet:
    """Get projects from soup."""
    projects = soup.find_all(
        'article', class_='Box-row')[:config.PROJECTS_LIMIT]
    return projects


async def get_project_info(project: Tag) -> ProjectInfo:
    """Get project info."""
    link = project.select('h2 a')[0]

    header = clean_text(link.text.strip())

    description = project.select('p')
    description = description[0].text.strip() if description else ''

    language = project.find('span', itemprop='programmingLanguage')
    language = language.text if language else 'No Language'

    url = link.get('href')
    return ProjectInfo(header, description, language, GITHUB_BASE_URL + url)


def clean_text(text: str) -> str:
    """Clean text."""
    return text.replace('\n', '').replace('\t', '').replace(' ', '')


if __name__ == "__main__":
    asyncio.run(find_new_projects())
