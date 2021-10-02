from enum import IntEnum
from pydantic import BaseModel

class AustralianStateEnum(IntEnum):
    nsw = 1
    act = 2
    vic = 3
    qld = 4
    sa = 5
    wa = 6
    tas = 7
    nt = 8


class AddressSchema(BaseModel):
    address_no: int
    street: str
    suburb: str
    state: AustralianStateEnum
    postcode: str


class UnitAddressSchema(AddressSchema):
    unit_no: int
