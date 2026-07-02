# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProfitabilityGetProfitabilityResponse", "Data"]


class Data(BaseModel):
    active_milestones: Optional[str] = FieldInfo(alias="activeMilestones", default=None)

    agency_earnings: Optional[str] = FieldInfo(alias="agencyEarnings", default=None)

    commission_amount: Optional[str] = FieldInfo(alias="commissionAmount", default=None)

    commission_rate: Optional[str] = FieldInfo(alias="commissionRate", default=None)

    costs: Optional[List[object]] = None

    creator_name: Optional[str] = FieldInfo(alias="creatorName", default=None)

    has_commission_for_period: Optional[bool] = FieldInfo(alias="hasCommissionForPeriod", default=None)

    has_costs_for_period: Optional[bool] = FieldInfo(alias="hasCostsForPeriod", default=None)

    margin_percentage: Optional[str] = FieldInfo(alias="marginPercentage", default=None)

    month: Optional[int] = None

    only_fans_user_id: Optional[int] = FieldInfo(alias="onlyFansUserId", default=None)

    profit: Optional[str] = None

    projected_net: Optional[str] = FieldInfo(alias="projectedNet", default=None)

    rate_periods: Optional[List[object]] = FieldInfo(alias="ratePeriods", default=None)

    referral_note: Optional[str] = FieldInfo(alias="referralNote", default=None)

    total_costs: Optional[str] = FieldInfo(alias="totalCosts", default=None)

    year: Optional[int] = None


class ProfitabilityGetProfitabilityResponse(BaseModel):
    data: Optional[List[Data]] = None
