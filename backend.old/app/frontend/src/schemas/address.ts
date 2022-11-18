export type AustralianStateEnum = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8;

export interface AddressSchema {
  address_no: number;
  street: string;
  suburb: string;
  state: AustralianStateEnum;
  postcode: string;
}

export interface UnitAddressSchema extends AddressSchema {
  unit_no: number;
}
