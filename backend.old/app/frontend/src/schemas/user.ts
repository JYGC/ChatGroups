/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/
import type { AddressSchema, UnitAddressSchema } from "./address";

export interface UserLoginSchema {
  email: string;
  password: string;
}

export interface UserDetailsSchema extends UserLoginSchema {
  phone_no: string;
  address: AddressSchema | UnitAddressSchema;
  dob: string;
}
