# app/services/dashboard_service.py
from app.persistence.repositories.dashboard_repository import DashboardRepository
from app.services.dto.dashboard_dto import (
    DashboardDTO,
    GlobalStatsDTO,
    CategoryProgressDTO,
)


class DashboardService:
    def __init__(self, dashboard_repository: DashboardRepository):
        self._repo = dashboard_repository

    def get_dashboard_data(self) -> DashboardDTO:
        global_data = self._repo.get_global_stats()

        total = global_data["total"] or 0
        acquired = global_data["acquired"] or 0
        to_learn = global_data["to_learn"] or 0

        progression = (acquired / total * 100) if total > 0 else 0

        global_stats = GlobalStatsDTO(
            total=total,
            acquired=acquired,
            to_learn=to_learn,
            progression_percent=round(progression, 1),
        )

        categories_rows = self._repo.get_category_progress()

        categories_progress = []

        for row in categories_rows:
            total_cat = row["total"] or 0
            acquired_cat = row["acquired"] or 0

            percent = (
                acquired_cat / total_cat * 100 if total_cat > 0 else 0
            )

            categories_progress.append(
                CategoryProgressDTO(
                    category_title=row["category_title"],
                    total=total_cat,
                    acquired=acquired_cat,
                    percent=round(percent, 1),
                )
            )

        return DashboardDTO(
            global_stats=global_stats,
            categories_progress=categories_progress,
        )