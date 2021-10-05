from datetime import datetime
from pony.orm import PrimaryKey, Optional, Required, Set
from uuid import UUID, uuid4

from app.core.config import settings
from app.database.connection import db
from app.schemas.address import AddressSchema, AustralianStateEnum


class Address(db.Entity):
    _table_ = (settings.POSTGRES_SCHEMA, "address")
    id = PrimaryKey(UUID, default=uuid4)
    # values
    address_no = Required(int)
    street = Required(str)
    suburb = Required(str)
    state = Required(AustralianStateEnum)
    postcode = Required(str)
    # Foreign keys
    user = Optional("User")
    # Date created
    date_created = Required(datetime, default=datetime.now)
    # Histories
    address_histories = Set("AddressHistory")

    def create_history(self, action: str):
        return AddressHistory(
            address_no=self.address_no,
            street=self.street,
            suburb=self.suburb,
            state=self.state,
            postcode=self.postcode,
            address=self,
            action=action
        )

    @staticmethod
    def from_schema(address_schema: AddressSchema):
        return Address(
            address_no=address_schema.address_no,
            street=address_schema.street,
            suburb=address_schema.suburb,
            state=address_schema.state,
            postcode=address_schema.postcode
        )


class AddressHistory(db.Entity):
    _table_ = (settings.POSTGRES_SCHEMA, "address_history")
    id = PrimaryKey(UUID, default=uuid4)
    # values
    address_no = Required(int)
    street = Required(str)
    suburb = Required(str)
    state = Required(AustralianStateEnum)
    postcode = Required(str)
    # Foreign keys
    user = Optional("UserHistory")
    # History columns
    address = Required(Address)
    action = Required(str)
    date_changed = Required(datetime, default=datetime.now)

# class AustralianState(db.Entity):
#     value = Required(str)
