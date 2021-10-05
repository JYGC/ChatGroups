from datetime import datetime, date
from pony.orm import db_session, Optional, PrimaryKey, Required, Set
from pydantic import EmailStr
from uuid import UUID, uuid4

from app.core.config import settings
from app.database.connection import db
from app.schemas.user import UserDetailsSchema
from app.models.address import Address


class User(db.Entity):
    _table_ = (settings.POSTGRES_SCHEMA, "user")
    id = PrimaryKey(UUID, default=uuid4)
    # values
    email = Required(EmailStr, unique=True)
    password = Required(str)
    phone_no = Required(str)
    dob = Required(date)
    banned = Required(bool, default=False, sql_default=False)
    deleted = Required(bool, default=False, sql_default=False)
    is_superuser = Required(bool, default=False, sql_default=False)
    # Foreign keys
    address = Optional("Address")
    chat_users = Set("ChatUser")
    # Date created
    date_created = Required(datetime, default=datetime.now)
    # Histories
    user_histories = Set("UserHistory")

    def create_history(self, action: str):
        return UserHistory(
            email=self.email,
            password=self.password,
            phone_no=self.phone_no,
            dob=self.dob,
            banned=self.banned,
            deleted=self.deleted,
            is_superuser=self.is_superuser,
            user=self,
            action=action
        )

    @staticmethod
    def from_schema(user_details: UserDetailsSchema):
        return User(
            email=user_details.email.lower(),
            password=user_details.password,
            phone_no=user_details.phone_no,
            dob=user_details.dob
        )


class UserHistory(db.Entity):
    _table_ = (settings.POSTGRES_SCHEMA, "user_history")
    id = PrimaryKey(UUID, default=uuid4)
    # values
    email = Required(EmailStr)
    password = Required(str)
    phone_no = Required(str)
    dob = Required(date)
    banned = Required(bool)
    deleted = Required(bool)
    is_superuser = Required(bool)
    # Foreign keys
    address = Optional("AddressHistory")
    # History columns
    user = Required(User)
    action = Required(str)
    date_changed = Required(datetime, default=datetime.now)
