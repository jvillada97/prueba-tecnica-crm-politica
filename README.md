# CRM Político - API de Métricas

API REST para consultar métricas de rendimiento de usuarios políticos con autenticación JWT.

## 🚀 Características

- **Autenticación segura**: JWT tokens y validación de session ID
- **Métricas completas**: Rankings diarios, semanales y mensuales
- **Datos geográficos**: Posiciones por ciudad y región
- **Estadísticas de referidos**: Invitaciones y conversiones
- **Auditoría completa**: Logs de acceso para monitoreo
- **Respuesta rápida**: Optimizado para responder en <300ms

## 📋 Endpoint Principal

### GET /api/v1/analytics/user-stats

Obtiene las métricas completas del usuario autenticado.

**Headers requeridos:**
```
Authorization: Bearer {jwt_token}
X-Session-ID: {session_id}
Content-Type: application/json
```

**Respuesta de ejemplo:**
```json
{
  "user_id": "vol_12345",
  "name": "María González",
  "region": {
    "position": 3,
    "total_participants": 150,
    "percentile": 98.0
  },
  "city": {
    "position": 1,
    "total_participants": 45,
    "percentile": 100.0
  },
  "ranking": {
    "today": {
      "position": 2,
      "points": 850
    },
    "week": {
      "position": 4,
      "points": 3200
    },
    "month": {
      "position": 5,
      "points": 12500
    }
  },
  "referrals": {
    "total_invited": 23,
    "active_volunteers": 18,
    "referrals_this_month": 7,
    "conversion_rate": 78.3,
    "referral_points": 4600
  },
  "metadata": {
    "last_updated": "2024-01-20T10:28:45Z",
    "cache_ttl_seconds": 0,
    "data_freshness": "real-time"
  }
}
```

## 🛠️ Instalación y Ejecución

### Opción 1: Script automático
```bash
chmod +x run_server.sh
./run_server.sh
```

### Opción 2: Manual
```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones

# Ejecutar servidor
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 🧪 Tests

```bash
chmod +x run_tests.sh
./run_tests.sh
```

## 📁 Estructura del Proyecto

```
├── main.py                 # Aplicación principal FastAPI
├── requirements.txt        # Dependencias Python
├── .env.example           # Variables de entorno ejemplo
├── run_server.sh          # Script de ejecución
├── run_tests.sh           # Script de tests
├── app/
│   ├── core/
│   │   └── config.py      # Configuraciones
│   ├── dependencies/
│   │   └── auth.py        # Dependencias de autenticación
│   ├── middleware/
│   │   └── audit.py       # Middleware de auditoría
│   ├── models/
│   │   └── schemas.py     # Modelos Pydantic
│   ├── routers/
│   │   └── analytics.py   # Endpoints de analytics
│   └── services/
│       ├── analytics_service.py   # Lógica de negocio
│       ├── auth_service.py        # Servicios de autenticación
│       └── firestore_service.py   # Integración con Firestore
└── tests/
    └── test_analytics.py   # Tests unitarios
```

## 🔧 Configuración

### Variables de entorno requeridas:

- `JWT_SECRET_KEY`: Clave secreta para JWT
- `FIRESTORE_PROJECT_ID`: ID del proyecto Firestore
- `FIRESTORE_CREDENTIALS_PATH`: Ruta a las credenciales de servicio

## 📊 Monitoreo y Auditoría

- Logs estructurados con `structlog`
- Auditoría de accesos sensibles
- Health checks en `/health` y `/api/v1/analytics/health`
- Headers de tiempo de respuesta

## 🔒 Seguridad

- Validación JWT obligatoria
- Control de acceso por usuario (ningún usuario ve datos de otro)
- Validación de Session ID
- Logs de auditoría para accesos sensibles