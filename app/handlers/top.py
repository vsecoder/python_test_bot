from telebot.async_telebot import AsyncTeleBot
from telebot import types

from app.db.functions import User

import logging

logger = logging.getLogger(__name__)


async def top_handler(message: types.Message, bot: AsyncTeleBot):
    """top handler"""
    top = await User.get_top()

    text = "Топ 10 игроков:\n"
    for user in top:
        text += f"{user.name} - {user.score}\n"

    await bot.send_message(message.chat.id, text, parse_mode="HTML")
