from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from app.core.config import settings
from app.utils import mock_structlog as structlog

logger = structlog.get_logger()

class AuthService:
    @staticmethod
    def verify_jwt_token(token: str) -> dict:
        """
        Verifica y decodifica un token JWT
        """
        try:
            payload = jwt.decode(
                token, 
                settings.jwt_secret_key, 
                algorithms=[settings.jwt_algorithm]
            )
            user_id: str = payload.get("user_id")
            if user_id is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token inválido: user_id no encontrado"
                )
            return payload
        except JWTError as e:
            logger.error("Error al decodificar JWT", error=str(e))
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )
    
    @staticmethod
    def extract_user_id_from_token(token: str) -> str:
        """
        Extrae el user_id del token JWT
        """
        payload = AuthService.verify_jwt_token(token)
        return payload.get("user_id")
    
    @staticmethod
    def validate_session_id(session_id: str) -> bool:
        """
        Valida que el session_id tenga el formato correcto
        """
        if not session_id or len(session_id) < 10:
            return False
        return True
