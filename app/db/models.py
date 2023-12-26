from tortoise import fields
from tortoise.models import Model


class User(Model):
    """
    DB model for users.

    Fields:
        id: int
        telegram_id: int
        name: str
        score: int
        step: int
    """
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField()
    name = fields.CharField(max_length=255, default="Unknown")

    score = fields.IntField(default=0)
    step = fields.IntField(default=0)
