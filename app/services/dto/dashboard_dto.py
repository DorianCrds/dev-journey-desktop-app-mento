# app/services/dto/dashboard_dto.py
from dataclasses import dataclass
from typing import List


@dataclass
class GlobalStatsDTO:
    total: int
    acquired: int
    to_learn: int
    progression_percent: float


@dataclass
class CategoryProgressDTO:
    category_title: str
    total: int
    acquired: int
    percent: float


@dataclass
class DashboardDTO:
    global_stats: GlobalStatsDTO
    categories_progress: List[CategoryProgressDTO]
