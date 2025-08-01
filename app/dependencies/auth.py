from fastapi import Depends, HTTPException, status, Header
from fastapi.security import HTTPBearer
from typing import Optional
from app.services.auth_service import AuthService
from app.utils import mock_structlog as structlog

logger = structlog.get_logger()
security = HTTPBearer()

async def get_current_user(
    authorization: str = Depends(security),
    x_session_id: Optional[str] = Header(None, alias="x-session-id")
) -> dict:
    """
    Dependency para obtener el usuario actual autenticado
    """
    try:
        # Extraer token del header Authorization
        token = authorization.credentials
        
        # Validar session ID
        if not x_session_id or not AuthService.validate_session_id(x_session_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Header X-Session-ID es requerido y debe ser válido"
            )
        
        # Verificar y extraer datos del token JWT
        payload = AuthService.verify_jwt_token(token)
        user_id = payload.get("user_id")
        
        # Log de acceso para auditoría
        logger.info(
            "Usuario autenticado exitosamente",
            user_id=user_id,
            session_id=x_session_id
        )
        
        return {
            "user_id": user_id,
            "session_id": x_session_id,
            "token_payload": payload
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error en autenticación", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Error de autenticación"
        )
