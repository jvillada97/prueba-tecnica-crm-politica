from fastapi import Request, Response
from datetime import datetime
from app.utils import mock_structlog as structlog
import time

logger = structlog.get_logger()

async def audit_middleware(request: Request, call_next):
    """
    Middleware para auditoría de accesos sensibles
    """
    start_time = time.time()
    
    # Extraer información de la solicitud
    client_ip = request.client.host
    user_agent = request.headers.get("user-agent", "")
    session_id = request.headers.get("x-session-id", "")
    auth_header = request.headers.get("authorization", "")
    
    # Información de auditoría
    audit_data = {
        "timestamp": datetime.utcnow(),
        "method": request.method,
        "url": str(request.url),
        "client_ip": client_ip,
        "user_agent": user_agent,
        "session_id": session_id,
        "has_auth": bool(auth_header),
        "endpoint": request.url.path
    }
    
    # Procesar solicitud
    response = await call_next(request)
    
    # Calcular tiempo de respuesta
    process_time = time.time() - start_time
    process_time_ms = round(process_time * 1000, 2)
    
    # Agregar información de respuesta
    audit_data.update({
        "status_code": response.status_code,
        "response_time_ms": process_time_ms,
        "success": 200 <= response.status_code < 300
    })
    
    # Log de auditoría para endpoints sensibles
    if "/analytics/" in request.url.path:
        logger.info("Analytics access audit", **audit_data)
    
    # Agregar header de tiempo de respuesta
    response.headers["X-Process-Time"] = str(process_time_ms)
    
    return response
