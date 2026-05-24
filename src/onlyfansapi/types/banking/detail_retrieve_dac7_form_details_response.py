# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DetailRetrieveDac7FormDetailsResponse", "_Meta", "_Meta_Cache", "_Meta_Credits", "_Meta_RateLimits", "Data"]


class _Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class _Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class _Meta_RateLimits(BaseModel):
    limit_day: Optional[int] = None

    limit_minute: Optional[int] = None

    remaining_day: Optional[int] = None

    remaining_minute: Optional[int] = None


class _Meta(BaseModel):
    api_cache: Optional[_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class Data(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    city_of_birth: Optional[str] = FieldInfo(alias="cityOfBirth", default=None)

    country_id: Optional[int] = FieldInfo(alias="countryId", default=None)

    country_of_birth_id: Optional[int] = FieldInfo(alias="countryOfBirthId", default=None)

    country_of_residence_id: Optional[int] = FieldInfo(alias="countryOfResidenceId", default=None)

    dob: Optional[str] = FieldInfo(alias="DOB", default=None)

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    issuing_country_id: Optional[int] = FieldInfo(alias="issuingCountryId", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    state: Optional[str] = None

    status: Optional[str] = None

    tax_id: Optional[str] = FieldInfo(alias="taxId", default=None)

    type: Optional[str] = None

    vat_number: Optional[str] = FieldInfo(alias="vatNumber", default=None)

    zip: Optional[str] = None


class DetailRetrieveDac7FormDetailsResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
