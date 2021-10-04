from datetime import datetime
from pony.orm import Optional, PrimaryKey, Required, Set

from app.core.config import settings
from app.database.connection import db

class Chatgroup(db.Entity):
    _table_ = (settings.POSTGRES_SCHEMA, "chatgroup")
    id = PrimaryKey(int, auto=True)
    # values
    # Foreign keys
    chatgroup_users = Set("ChatgroupUser")
    messages = Set("Message")
    # Date created
    date_created = Required(datetime, default=datetime.now)


class ChatgroupUser(db.Entity):
    _table_ = (settings.POSTGRES_SCHEMA, "chatgroup_user")
    id = PrimaryKey(int, auto=True)
    # values
    chatgroup_admin = Required(bool, default=False, sql_default=False)
    join_request_pending = Required(bool, default=False, sql_default=False)
    invitation_pending = Required(bool, default=False, sql_default=False)
    is_deleted = Required(bool, default=False, sql_default=False)
    # Foreign keys
    chatgroup = Required("Chatgroup")
    messages = Optional("Message")
    user = Required("User")
    # Date created
    date_created = Required(datetime, default=datetime.now)
