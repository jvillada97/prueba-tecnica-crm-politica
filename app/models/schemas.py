from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RegionStats(BaseModel):
    position: int
    total_participants: int
    percentile: float

class CityStats(BaseModel):
    position: int
    total_participants: int
    percentile: float

class RankingPeriod(BaseModel):
    position: int
    points: int

class Ranking(BaseModel):
    today: RankingPeriod
    week: RankingPeriod
    month: RankingPeriod

class Referrals(BaseModel):
    total_invited: int
    active_volunteers: int
    referrals_this_month: int
    conversion_rate: float
    referral_points: int

class Metadata(BaseModel):
    last_updated: datetime
    cache_ttl_seconds: int
    data_freshness: str

class UserStatsResponse(BaseModel):
    user_id: str
    name: str
    region: RegionStats
    city: CityStats
    ranking: Ranking
    referrals: Referrals
    metadata: Metadata

class ErrorResponse(BaseModel):
    error: str
    message: str
    timestamp: datetime
