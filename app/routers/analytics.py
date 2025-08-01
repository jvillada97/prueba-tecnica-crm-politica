from fastapi import APIRouter, Depends, HTTPException, status
from app.models.schemas import UserStatsResponse, ErrorResponse
from app.services.analytics_service import analytics_service
from app.dependencies.auth import get_current_user
from datetime import datetime
from app.utils import mock_structlog as structlog

logger = structlog.get_logger()

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
    responses={
        401: {"model": ErrorResponse, "description": "No autorizado"},
        403: {"model": ErrorResponse, "description": "Acceso denegado"},
        404: {"model": ErrorResponse, "description": "Usuario no encontrado"},
        500: {"model": ErrorResponse, "description": "Error interno del servidor"}
    }
)

@router.get(
    "/user-stats",
    response_model=UserStatsResponse,
    summary="Obtener métricas de rendimiento del usuario",
    description="""
    Obtiene las métricas completas de rendimiento para un usuario autenticado:
    
    - **Ranking**: Posiciones diarias, semanales y mensuales
    - **Geografía**: Posición en ciudad y región
    - **Referidos**: Estadísticas de invitaciones y conversiones
    
    Requiere autenticación JWT y Session ID válidos.
    """,
    response_description="Métricas completas del usuario"
)
async def get_user_stats(
    current_user: dict = Depends(get_current_user)
) -> UserStatsResponse:
    """
    Endpoint principal para obtener métricas de rendimiento del usuario
    """
    user_id = current_user["user_id"]
    session_id = current_user["session_id"]
    
    try:
        logger.info(
            "Solicitando estadísticas de usuario",
            user_id=user_id,
            session_id=session_id
        )
        
        # Obtener estadísticas del servicio
        user_stats = await analytics_service.get_user_stats(user_id)
        
        logger.info(
            "Estadísticas obtenidas exitosamente",
            user_id=user_id,
            response_time_target="<300ms"
        )
        
        return user_stats
        
    except ValueError as e:
        logger.warning("Usuario no encontrado", user_id=user_id, error=str(e))
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario {user_id} no encontrado"
        )
    
    except Exception as e:
        logger.error(
            "Error al obtener estadísticas",
            user_id=user_id,
            error=str(e)
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno al procesar las métricas"
        )

@router.get(
    "/health",
    summary="Health check del servicio de analytics",
    description="Verifica el estado de los servicios dependientes (Firestore)"
)
async def analytics_health():
    """
    Health check específico para el módulo de analytics
    """
    try:
        health_status = {
            "status": "healthy",
            "timestamp": datetime.utcnow(),
            "services": {
                "firestore": "healthy"
            }
        }
        
        return health_status
        
    except Exception as e:
        logger.error("Health check failed", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Servicio no disponible"
        )
