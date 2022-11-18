from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class ChatSchema(BaseModel):
    name: str
    description: Optional[str]
    number_of_participants: int


class MyChatSchema(ChatSchema):
    visible_to_all: bool


class JoinedChatSchema(ChatSchema):
    user_is_admin: bool
