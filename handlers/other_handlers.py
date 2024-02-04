from aiogram import Router
from aiogram.types import Message

from config_data.config import config
from lexicon.lexicon import LEXICON

router = Router()


@router.message()
async def other_answer(message: Message):
    """Default answer."""
    await message.reply(
        text=LEXICON['other_answer'].format(config.tg_channel.name))
