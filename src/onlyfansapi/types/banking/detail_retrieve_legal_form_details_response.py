# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DetailRetrieveLegalFormDetailsResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataDocumentType",
    "DataDocumentTypeValue",
]


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


class DataDocumentTypeValue(BaseModel):
    code: Optional[str] = None

    name: Optional[str] = None


class DataDocumentType(BaseModel):
    values: Optional[List[DataDocumentTypeValue]] = None


class Data(BaseModel):
    date_of_birth: Optional[str] = FieldInfo(alias="dateOfBirth", default=None)

    document_type: Optional[DataDocumentType] = FieldInfo(alias="documentType", default=None)

    is_allowed_dl: Optional[bool] = FieldInfo(alias="isAllowedDL", default=None)

    private_website: Optional[str] = FieldInfo(alias="privateWebsite", default=None)

    real_address: Optional[str] = FieldInfo(alias="realAddress", default=None)

    real_business_name: Optional[str] = FieldInfo(alias="realBusinessName", default=None)

    real_city: Optional[str] = FieldInfo(alias="realCity", default=None)

    real_first_name: Optional[str] = FieldInfo(alias="realFirstName", default=None)

    real_instagram: Optional[str] = FieldInfo(alias="realInstagram", default=None)

    real_last_name: Optional[str] = FieldInfo(alias="realLastName", default=None)

    real_postal: Optional[str] = FieldInfo(alias="realPostal", default=None)

    real_state: Optional[str] = FieldInfo(alias="realState", default=None)

    real_twitter: Optional[str] = FieldInfo(alias="realTwitter", default=None)


class DetailRetrieveLegalFormDetailsResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
