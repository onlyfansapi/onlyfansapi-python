# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DetailRetrieveBankDetailsResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataPayout",
    "DataPayoutFields",
    "DataPayoutFieldsAddress",
    "DataPayoutFieldsAddressLabel",
    "DataPayoutFieldsBankName",
    "DataPayoutFieldsBankNameLabel",
    "DataPayoutFieldsBic",
    "DataPayoutFieldsBicLabel",
    "DataPayoutFieldsCity",
    "DataPayoutFieldsCityLabel",
    "DataPayoutFieldsCountry",
    "DataPayoutFieldsCountryLabel",
    "DataPayoutFieldsFirstName",
    "DataPayoutFieldsFirstNameLabel",
    "DataPayoutFieldsFirstNameOninput",
    "DataPayoutFieldsFirstNameOninputReplace",
    "DataPayoutFieldsIban",
    "DataPayoutFieldsIbanLabel",
    "DataPayoutFieldsIbanRegex",
    "DataPayoutFieldsLastName",
    "DataPayoutFieldsLastNameLabel",
    "DataPayoutFieldsLastNameOninput",
    "DataPayoutFieldsLastNameOninputReplace",
    "DataPayoutFieldsPostal",
    "DataPayoutFieldsPostalLabel",
    "DataPayoutUiMapping",
    "DataPayoutUiMappingAlert",
    "DataPayoutUiMappingAlertText",
    "DataPayoutUiMappingBtnSubmit",
    "DataPayoutUiMappingTitle",
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


class DataPayoutFieldsAddressLabel(BaseModel):
    key: Optional[str] = None


class DataPayoutFieldsAddress(BaseModel):
    label: Optional[DataPayoutFieldsAddressLabel] = None

    maxlength: Optional[int] = None

    required: Optional[bool] = None

    value: Optional[str] = None


class DataPayoutFieldsBankNameLabel(BaseModel):
    key: Optional[str] = None


class DataPayoutFieldsBankName(BaseModel):
    label: Optional[DataPayoutFieldsBankNameLabel] = None

    maxlength: Optional[int] = None

    required: Optional[bool] = None

    value: Optional[str] = None


class DataPayoutFieldsBicLabel(BaseModel):
    key: Optional[str] = None


class DataPayoutFieldsBic(BaseModel):
    label: Optional[DataPayoutFieldsBicLabel] = None

    maxlength: Optional[int] = None

    required: Optional[bool] = None

    value: Optional[str] = None


class DataPayoutFieldsCityLabel(BaseModel):
    key: Optional[str] = None


class DataPayoutFieldsCity(BaseModel):
    label: Optional[DataPayoutFieldsCityLabel] = None

    maxlength: Optional[int] = None

    required: Optional[bool] = None

    value: Optional[str] = None


class DataPayoutFieldsCountryLabel(BaseModel):
    key: Optional[str] = None


class DataPayoutFieldsCountry(BaseModel):
    label: Optional[DataPayoutFieldsCountryLabel] = None

    readonly: Optional[bool] = None

    uionly: Optional[bool] = None

    value: Optional[str] = None


class DataPayoutFieldsFirstNameLabel(BaseModel):
    key: Optional[str] = None


class DataPayoutFieldsFirstNameOninputReplace(BaseModel):
    flag: Optional[str] = None

    pattern: Optional[str] = None


class DataPayoutFieldsFirstNameOninput(BaseModel):
    replace: Optional[DataPayoutFieldsFirstNameOninputReplace] = None


class DataPayoutFieldsFirstName(BaseModel):
    label: Optional[DataPayoutFieldsFirstNameLabel] = None

    maxlength: Optional[int] = None

    oninput: Optional[DataPayoutFieldsFirstNameOninput] = None

    readonly: Optional[bool] = None

    value: Optional[str] = None


class DataPayoutFieldsIbanLabel(BaseModel):
    key: Optional[str] = None


class DataPayoutFieldsIbanRegex(BaseModel):
    flag: Optional[str] = None

    pattern: Optional[str] = None


class DataPayoutFieldsIban(BaseModel):
    label: Optional[DataPayoutFieldsIbanLabel] = None

    regex: Optional[DataPayoutFieldsIbanRegex] = None

    required: Optional[bool] = None

    value: Optional[str] = None


class DataPayoutFieldsLastNameLabel(BaseModel):
    key: Optional[str] = None


class DataPayoutFieldsLastNameOninputReplace(BaseModel):
    flag: Optional[str] = None

    pattern: Optional[str] = None


class DataPayoutFieldsLastNameOninput(BaseModel):
    replace: Optional[DataPayoutFieldsLastNameOninputReplace] = None


class DataPayoutFieldsLastName(BaseModel):
    label: Optional[DataPayoutFieldsLastNameLabel] = None

    maxlength: Optional[int] = None

    oninput: Optional[DataPayoutFieldsLastNameOninput] = None

    readonly: Optional[bool] = None

    value: Optional[str] = None


class DataPayoutFieldsPostalLabel(BaseModel):
    key: Optional[str] = None


class DataPayoutFieldsPostal(BaseModel):
    label: Optional[DataPayoutFieldsPostalLabel] = None

    maxlength: Optional[int] = None

    required: Optional[bool] = None

    value: Optional[str] = None


class DataPayoutFields(BaseModel):
    address: Optional[DataPayoutFieldsAddress] = None

    bank_name: Optional[DataPayoutFieldsBankName] = None

    bic: Optional[DataPayoutFieldsBic] = None

    city: Optional[DataPayoutFieldsCity] = None

    country: Optional[DataPayoutFieldsCountry] = None

    first_name: Optional[DataPayoutFieldsFirstName] = None

    iban: Optional[DataPayoutFieldsIban] = None

    last_name: Optional[DataPayoutFieldsLastName] = None

    postal: Optional[DataPayoutFieldsPostal] = None


class DataPayoutUiMappingAlertText(BaseModel):
    key: Optional[str] = None


class DataPayoutUiMappingAlert(BaseModel):
    class_: Optional[str] = FieldInfo(alias="class", default=None)

    text: Optional[DataPayoutUiMappingAlertText] = None


class DataPayoutUiMappingBtnSubmit(BaseModel):
    key: Optional[str] = None


class DataPayoutUiMappingTitle(BaseModel):
    key: Optional[str] = None


class DataPayoutUiMapping(BaseModel):
    alert: Optional[DataPayoutUiMappingAlert] = None

    btn_submit: Optional[DataPayoutUiMappingBtnSubmit] = None

    title: Optional[DataPayoutUiMappingTitle] = None


class DataPayout(BaseModel):
    code: Optional[str] = None

    description: Optional[str] = None

    fields: Optional[DataPayoutFields] = None

    fields_order: Optional[List[str]] = FieldInfo(alias="fieldsOrder", default=None)

    min_payout_summ: Optional[int] = FieldInfo(alias="minPayoutSumm", default=None)

    payout_time: Optional[str] = FieldInfo(alias="payoutTime", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    ui_mapping: Optional[DataPayoutUiMapping] = FieldInfo(alias="uiMapping", default=None)


class Data(BaseModel):
    is_payout_data_filled: Optional[bool] = FieldInfo(alias="isPayoutDataFilled", default=None)

    payout_code: Optional[str] = FieldInfo(alias="payoutCode", default=None)

    payouts: Optional[List[DataPayout]] = None


class DetailRetrieveBankDetailsResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
