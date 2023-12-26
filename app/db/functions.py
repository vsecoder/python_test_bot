from typing import Union

from tortoise.exceptions import DoesNotExist

from app.db import models


def _(text):
    return text.replace('<', '').replace('>', '')


class User(models.User):
    """
    User model, contains all methods for working with users.
    """

    @classmethod
    async def is_registered(cls, telegram_id: int) -> Union[models.User, bool]:
        try:
            return await cls.get(telegram_id=telegram_id)
        except DoesNotExist:
            return False

    @classmethod
    async def register(
            cls,
            telegram_id: int,
            name: str = "Unknown"
    ):
        await User(
            telegram_id=telegram_id,
            name=_(name),
            score=0,
        ).save()

    @classmethod
    async def get_count(cls) -> int:
        users_count = await cls.all()
        return len(users_count)

    @classmethod
    async def add_score(cls, telegram_id: int) -> bool:
        user = await cls.get(telegram_id=telegram_id)
        if not user:
            return False

        user.score += 1
        await user.save()

        return True

    @classmethod
    async def add_step(cls, telegram_id: int) -> bool:
        user = await cls.get(telegram_id=telegram_id)
        if not user:
            return False

        user.step += 1
        await user.save()

        return True

    @classmethod
    async def get_top(cls) -> list:
        users = await cls.all().order_by("-score").limit(10)
        return users
