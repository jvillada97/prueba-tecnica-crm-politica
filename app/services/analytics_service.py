from datetime import datetime
from typing import Dict
from app.models.schemas import UserStatsResponse, RegionStats, CityStats, Ranking, RankingPeriod, Referrals, Metadata
from app.services.firestore_service import firestore_service
from app.utils import mock_structlog as structlog

logger = structlog.get_logger()

class AnalyticsService:
    
    async def get_user_stats(self, user_id: str) -> UserStatsResponse:
        """
        Obtiene las estadísticas completas del usuario
        """
        logger.info("Obteniendo datos de Firestore", user_id=user_id)
        
        try:
            # Obtener datos del usuario en paralelo
            user_profile = await firestore_service.get_user_profile(user_id)
            ranking_stats = await firestore_service.get_user_ranking_stats(user_id)
            geographical_stats = await firestore_service.get_geographical_stats(user_id)
            referral_stats = await firestore_service.get_referral_stats(user_id)
            
            if not user_profile:
                raise ValueError(f"Usuario {user_id} no encontrado")
            
            # Construir respuesta
            response_data = self._build_user_stats_response(
                user_id=user_id,
                user_profile=user_profile,
                ranking_stats=ranking_stats,
                geographical_stats=geographical_stats,
                referral_stats=referral_stats
            )
            
            return response_data
            
        except Exception as e:
            logger.error("Error al obtener estadísticas del usuario", user_id=user_id, error=str(e))
            raise
    
    def _build_user_stats_response(
        self,
        user_id: str,
        user_profile: Dict,
        ranking_stats: Dict,
        geographical_stats: Dict,
        referral_stats: Dict
    ) -> UserStatsResponse:
        """
        Construye la respuesta estructurada de estadísticas del usuario
        """
        
        # Región
        region = RegionStats(
            position=geographical_stats["region"]["position"],
            total_participants=geographical_stats["region"]["total_participants"],
            percentile=geographical_stats["region"]["percentile"]
        )
        
        # Ciudad
        city = CityStats(
            position=geographical_stats["city"]["position"],
            total_participants=geographical_stats["city"]["total_participants"],
            percentile=geographical_stats["city"]["percentile"]
        )
        
        # Ranking
        ranking = Ranking(
            today=RankingPeriod(
                position=ranking_stats["today"]["position"],
                points=ranking_stats["today"]["points"]
            ),
            week=RankingPeriod(
                position=ranking_stats["week"]["position"],
                points=ranking_stats["week"]["points"]
            ),
            month=RankingPeriod(
                position=ranking_stats["month"]["position"],
                points=ranking_stats["month"]["points"]
            )
        )
        
        # Referidos
        referrals = Referrals(
            total_invited=referral_stats["total_invited"],
            active_volunteers=referral_stats["active_volunteers"],
            referrals_this_month=referral_stats["referrals_this_month"],
            conversion_rate=referral_stats["conversion_rate"],
            referral_points=referral_stats["referral_points"]
        )
        
        # Metadata
        metadata = Metadata(
            last_updated=datetime.utcnow(),
            cache_ttl_seconds=0,  # Sin cache
            data_freshness="real-time"
        )
        
        return UserStatsResponse(
            user_id=user_id,
            name=user_profile.get("name", "Usuario"),
            region=region,
            city=city,
            ranking=ranking,
            referrals=referrals,
            metadata=metadata
        )

# Instancia global del servicio
analytics_service = AnalyticsService()
