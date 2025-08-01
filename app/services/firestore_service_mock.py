from typing import Optional, Dict, List
from datetime import datetime, timedelta
from app.utils import mock_structlog as structlog
from app.core.config import settings

logger = structlog.get_logger()

class FirestoreService:
    def __init__(self):
        # Para desarrollo, usamos datos mock
        self.mock_mode = True
        logger.info("FirestoreService iniciado en modo mock para desarrollo")
    
    def _get_mock_data(self, user_id: str) -> Dict:
        """
        Datos mock para desarrollo y testing
        """
        return {
            "users": {
                user_id: {
                    "name": "María González",
                    "email": "maria.gonzalez@ejemplo.com",
                    "region": "Bogotá",
                    "city": "Chapinero",
                    "created_at": datetime.utcnow()
                }
            },
            "daily_rankings": {
                user_id: {
                    "position": 2,
                    "points": 850,
                    "date": datetime.utcnow().date()
                }
            },
            "weekly_rankings": {
                user_id: {
                    "position": 4,
                    "points": 3200,
                    "week": datetime.utcnow().isocalendar()[1]
                }
            },
            "monthly_rankings": {
                user_id: {
                    "position": 5,
                    "points": 12500,
                    "month": datetime.utcnow().month
                }
            },
            "geographical_stats": {
                user_id: {
                    "region_position": 3,
                    "region_total": 150,
                    "region_percentile": 98.0,
                    "city_position": 1,
                    "city_total": 45,
                    "city_percentile": 100.0
                }
            },
            "referral_stats": {
                user_id: {
                    "total_invited": 23,
                    "active_volunteers": 18,
                    "referrals_this_month": 7,
                    "conversion_rate": 78.3,
                    "referral_points": 4600
                }
            }
        }
    
    async def get_user_profile(self, user_id: str) -> Optional[Dict]:
        """
        Obtiene el perfil básico del usuario
        """
        try:
            mock_data = self._get_mock_data(user_id)
            return mock_data["users"].get(user_id)
        except Exception as e:
            logger.error("Error al obtener perfil de usuario", user_id=user_id, error=str(e))
            return None
    
    async def get_user_ranking_stats(self, user_id: str) -> Dict:
        """
        Obtiene las estadísticas de ranking del usuario
        """
        try:
            mock_data = self._get_mock_data(user_id)
            return {
                "today": mock_data["daily_rankings"][user_id],
                "week": mock_data["weekly_rankings"][user_id],
                "month": mock_data["monthly_rankings"][user_id]
            }
        except Exception as e:
            logger.error("Error al obtener estadísticas de ranking", user_id=user_id, error=str(e))
            raise
    
    async def get_geographical_stats(self, user_id: str) -> Dict:
        """
        Obtiene estadísticas geográficas (región y ciudad)
        """
        try:
            mock_data = self._get_mock_data(user_id)
            data = mock_data["geographical_stats"][user_id]
            
            return {
                "region": {
                    "position": data["region_position"],
                    "total_participants": data["region_total"],
                    "percentile": data["region_percentile"]
                },
                "city": {
                    "position": data["city_position"],
                    "total_participants": data["city_total"],
                    "percentile": data["city_percentile"]
                }
            }
        except Exception as e:
            logger.error("Error al obtener estadísticas geográficas", user_id=user_id, error=str(e))
            raise
    
    async def get_referral_stats(self, user_id: str) -> Dict:
        """
        Obtiene estadísticas de referidos
        """
        try:
            mock_data = self._get_mock_data(user_id)
            return mock_data["referral_stats"][user_id]
        except Exception as e:
            logger.error("Error al obtener estadísticas de referidos", user_id=user_id, error=str(e))
            raise

# Instancia global del servicio
firestore_service = FirestoreService()
