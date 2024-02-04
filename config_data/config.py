from dataclasses import dataclass

from aiogram import Bot, Dispatcher
from environs import Env

from database.dao import ProjectDAO

import os

from pathlib import Path


@dataclass
class TgBot:
    token: str


@dataclass
class TgChannel:
    id: int
    name: str


@dataclass
class Config:
    tg_bot: TgBot
    tg_channel: TgChannel


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
        ),
        tg_channel=TgChannel(
            id=env('CHANNEL_ID'),
            name=env('CHANNEL_NAME'),
        ),
    )


UPDATE_TIME_MINUTES = 60
DATABASE_PATH = Path(os.path.abspath(__file__)).parent.parent / 'sql.db'
DATABASE_DRIVER = f'sqlite:///{DATABASE_PATH}'

PROJECTS_LIMIT = 10

GITHUB_URLS = [
    ('https://github.com/trending/python?since=daily', 'Python Daily'),
    ('https://github.com/trending/python?since=weekly', 'Python Weekly'),
    ('https://github.com/trending/python?since=monthly', 'Python Monthly'),
    ('https://github.com/trending?since=daily', 'All Daily'),
    ('https://github.com/trending?since=weekly', 'All Weekly'),
    ('https://github.com/trending?since=monthly', 'All Monthly'),
]

GITHUB_BASE_URL = 'https://github.com/'

config: Config = load_config()
project_dao = ProjectDAO(DATABASE_DRIVER)
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher()
