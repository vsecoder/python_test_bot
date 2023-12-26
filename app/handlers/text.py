from telebot.async_telebot import AsyncTeleBot
from telebot import types

from app.db.functions import User
from app.utils.questions import questions
import logging
import random

logger = logging.getLogger(__name__)


async def text_handler(message: types.Message, bot: AsyncTeleBot):
    """all massages handler for questions"""
    user = await User.is_registered(message.chat.id)
    keyboard = types.ReplyKeyboardMarkup(True)

    if not user:
        return await bot.send_message(message.chat.id, "Вы не зарегистрированы\n/start")

    question_number = user.step

    if question_number > len(questions):
        return await bot.send_message(message.chat.id, "Вы уже прошли тест и получили результат.")

    # check last answer
    if question_number != 0:
        last_answer = questions[question_number - 1]["answer"]
        # check answer
        if last_answer == message.text:
            await User.add_score(message.chat.id)

    # check end of test
    if question_number == len(questions):
        await User.add_step(message.chat.id)
        user = await User.is_registered(message.chat.id)
        keyboard.row("/top")

        return await bot.send_message(message.chat.id, (
                f"Вы прошли тест!\n"
                f"Ваш результат: {user.score}/{len(questions)}\n"
                f"Это по нашей оценке {'джун' if user.score < 6 else 'мидл' if user.score < 8 else 'сеньор'}"
            ), parse_mode="HTML", reply_markup=keyboard
        )

    # send question
    question = questions[question_number]
    await User.add_step(message.chat.id)

    variants = question["variants"]
    random.shuffle(variants)

    keyboard.row(*variants)

    await bot.send_message(message.chat.id, question["text"], reply_markup=keyboard, parse_mode="HTML")
