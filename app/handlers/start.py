from telebot.async_telebot import AsyncTeleBot
from telebot import types

from app.db.functions import User
from app.utils.questions import questions

import logging

logger = logging.getLogger(__name__)


async def start_handler(message: types.Message, bot: AsyncTeleBot):
    """/start command handler"""
    user_id = message.from_user.id
    user = await User.is_registered(user_id)

    text = (
        "✨ <b>Привет, как тебе идея пройти тест на знание Python?</b>\n"
        "<u>Напиши что-нибудь в чат, что бы начать)))</u>\n\n"
        "P.S. тест пройти можно ТОЛЬКО 1 раз, по итогу вы получите результат и доступ к топу."
    )

    if not user:
        await User.register(user_id, message.from_user.first_name)
        logger.info(f"New user #{user_id}")
    elif user.step >= len(questions):
        text = "✨ Вы уже прошли викторину\n/top - получить топ"

    await bot.send_message(message.chat.id, text, parse_mode="HTML")
