from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
import uvicorn
from app.routers import analytics
from app.core.config import settings
from app.middleware.audit import audit_middleware
from app.utils import mock_structlog as structlog

# Configurar logging
structlog.configure()

logger = structlog.get_logger()

app = FastAPI(
    title="CRM Político - API de Métricas",
    description="API para consultar métricas de rendimiento de usuarios",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios permitidos
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Agregar middleware de auditoría
app.middleware("http")(audit_middleware)

# Incluir routers
app.include_router(analytics.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "CRM Político API - Analytics Service"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
