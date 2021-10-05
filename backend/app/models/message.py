from datetime import datetime
from pony.orm import PrimaryKey, Optional, Required, Set
from uuid import UUID, uuid4

from app.core.config import settings
from app.database.connection import db

class Message(db.Entity):
    _table_ = (settings.POSTGRES_SCHEMA, "message")
    id = PrimaryKey(UUID, default=uuid4)
    # values
    content = Required(str)
    # Foreign keys
    chat = Required("Chat")
    chat_users = Required("ChatUser")
    reply = Set("Message")
    parent = Optional("Message")
    # Date created
    date_created = Required(datetime, default=datetime.now)