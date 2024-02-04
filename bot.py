import asyncio
import logging

from config_data.config import bot, dp
from core.core import init_logging, init_scheduler
from handlers import other_handlers

logger = logging.getLogger(__name__)


async def main():
    init_logging()
    init_scheduler()

    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
