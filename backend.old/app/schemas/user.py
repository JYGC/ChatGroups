from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Union

from .address import AddressSchema, UnitAddressSchema


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserDetailsSchema(UserLoginSchema):
    phone_no: str
    address: Union[AddressSchema, UnitAddressSchema]
    dob: date
