# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DetailRetrieveLegalAndTaxStatusResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataDac7",
    "DataTax",
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


class DataDac7(BaseModel):
    country_ids: Optional[List[int]] = FieldInfo(alias="countryIds", default=None)

    error: Optional[str] = None

    required: Optional[bool] = None

    state: Optional[str] = None

    type: Optional[str] = None


class DataTax(BaseModel):
    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    editable: Optional[bool] = None

    is_banking_disabled: Optional[bool] = FieldInfo(alias="isBankingDisabled", default=None)


class Data(BaseModel):
    can_change_payout_type: Optional[bool] = FieldInfo(alias="canChangePayoutType", default=None)

    can_show_legal_form: Optional[bool] = FieldInfo(alias="canShowLegalForm", default=None)

    dac7: Optional[DataDac7] = FieldInfo(alias="DAC7", default=None)

    hide_banking: Optional[bool] = FieldInfo(alias="hideBanking", default=None)

    is_real_id_image: Optional[bool] = FieldInfo(alias="isRealIdImage", default=None)

    is_w9_exist: Optional[bool] = FieldInfo(alias="isW9Exist", default=None)

    is_w9_required: Optional[bool] = FieldInfo(alias="isW9Required", default=None)

    is_xxx: Optional[bool] = FieldInfo(alias="isXXX", default=None)

    iv_fail_reason: Optional[str] = FieldInfo(alias="ivFailReason", default=None)

    iv_status: Optional[str] = FieldInfo(alias="ivStatus", default=None)

    need_show_edit_w9: Optional[bool] = FieldInfo(alias="needShowEditW9", default=None)

    payout_legal_approve_reject_reason: Optional[str] = FieldInfo(alias="payoutLegalApproveRejectReason", default=None)

    show_iv_button: Optional[bool] = FieldInfo(alias="showIvButton", default=None)

    tax: Optional[DataTax] = None


class DetailRetrieveLegalAndTaxStatusResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
