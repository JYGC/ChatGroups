from datetime import datetime
from pony.orm import PrimaryKey, Optional, Required, Set

from app.core.config import settings
from app.database.connection import db

class Message(db.Entity):
    _table_ = (settings.POSTGRES_SCHEMA, "message")
    id = PrimaryKey(int, auto=True)
    # values
    content = Required(str)
    # Foreign keys
    chatgroup = Required("Chatgroup")
    chatgroup_users = Required("ChatgroupUser")
    reply = Set("Message")
    parent = Optional("Message")
    # Date created
    date_created = Required(datetime, default=datetime.now)