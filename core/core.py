import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config_data.config import UPDATE_TIME_MINUTES
from services.github_service import find_new_projects


def init_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s',
    )


def init_scheduler():
    bot_scheduler = AsyncIOScheduler()
    bot_scheduler.start()
    bot_scheduler.add_job(
        func=find_new_projects,
        trigger='interval',
        minutes=UPDATE_TIME_MINUTES,
    )
