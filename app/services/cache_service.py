import redis
from typing import Optional, Any
import json
from app.core.config import settings
import structlog

logger = structlog.get_logger()

class CacheService:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            password=settings.redis_password,
            decode_responses=True
        )
    
    def get(self, key: str) -> Optional[dict]:
        """
        Obtiene un valor del cache
        """
        try:
            cached_data = self.redis_client.get(key)
            if cached_data:
                return json.loads(cached_data)
            return None
        except Exception as e:
            logger.error("Error al obtener datos del cache", key=key, error=str(e))
            return None
    
    def set(self, key: str, value: dict, ttl: int = None) -> bool:
        """
        Guarda un valor en el cache con TTL
        """
        try:
            ttl = ttl or settings.cache_ttl_seconds
            serialized_value = json.dumps(value, default=str)
            self.redis_client.setex(key, ttl, serialized_value)
            logger.info("Datos guardados en cache", key=key, ttl=ttl)
            return True
        except Exception as e:
            logger.error("Error al guardar en cache", key=key, error=str(e))
            return False
    
    def delete(self, key: str) -> bool:
        """
        Elimina una clave del cache
        """
        try:
            result = self.redis_client.delete(key)
            logger.info("Clave eliminada del cache", key=key, deleted=bool(result))
            return bool(result)
        except Exception as e:
            logger.error("Error al eliminar del cache", key=key, error=str(e))
            return False
    
    def generate_user_stats_key(self, user_id: str) -> str:
        """
        Genera la clave para las estadísticas del usuario
        """
        return f"user_stats:{user_id}"
    
    def health_check(self) -> bool:
        """
        Verifica la conectividad con Redis
        """
        try:
            self.redis_client.ping()
            return True
        except Exception as e:
            logger.error("Redis health check failed", error=str(e))
            return False

# Instancia global del servicio de cache
cache_service = CacheService()
