from datetime import datetime
from pony.orm import Optional, PrimaryKey, Required, Set
from uuid import UUID, uuid4

from app.core.config import settings
from app.database.connection import db

class Chat(db.Entity):
    _table_ = (settings.POSTGRES_SCHEMA, "chat")
    id = PrimaryKey(UUID, default=uuid4)
    # values
    name = Required(str)
    description = Optional(str)
    visible_to_all = Required(bool, default=False, sql_default=False)
    # Foreign keys
    chat_users = Set("ChatUser")
    messages = Set("Message")
    # Date created
    date_created = Required(datetime, default=datetime.now)


class ChatUser(db.Entity):
    _table_ = (settings.POSTGRES_SCHEMA, "chat_user")
    id = PrimaryKey(UUID, default=uuid4)
    # values
    chat_admin = Required(bool, default=False, sql_default=False)
    join_request_pending = Required(bool, default=False, sql_default=False)
    invitation_pending = Required(bool, default=False, sql_default=False)
    is_deleted = Required(bool, default=False, sql_default=False)
    # Foreign keys
    chat = Required("Chat")
    messages = Optional("Message")
    user = Required("User")
    # Date created
    date_created = Required(datetime, default=datetime.now)
