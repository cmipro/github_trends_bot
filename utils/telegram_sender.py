from config_data.config import bot, config
from keyboards.project_kb import get_project_url
from services.structures import ProjectInfo


async def send_message_to_channel(
    project_info: ProjectInfo,
    rating_type: str
) -> None:
    """Send message to the channel."""
    message = (
        f'✅ New Project in <i>{rating_type} [{project_info.language}]</i>\n\n'
        f'<b>{project_info.header}</b>\n'
        f'<code>{project_info.description}</code>'
    )
    await bot.send_message(
        config.tg_channel.id,
        message,
        reply_markup=get_project_url(project_info.url),
    )
