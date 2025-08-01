# 🚀 GUÍA COMPLETA PARA PROBAR EN POSTMAN

## 📋 CONFIGURACIÓN INICIAL

### 1. **Arrancar el Servidor**
```bash
# En terminal, ejecutar:
cd /Users/jcvillada/Documents/crm-politica/prueba-tecnica-crm-politica
chmod +x run_server.sh
./run_server.sh
```

**O ejecutar directamente:**
```bash
/Users/jcvillada/Documents/crm-politica/prueba-tecnica-crm-politica/venv/bin/python main.py
```

### 2. **Token JWT**
```
# Generar un token válido:
python generate_test_token.py

# Ejemplo de formato:
Bearer YOUR_GENERATED_JWT_TOKEN_HERE
```

---

## 🔧 CONFIGURACIÓN EN POSTMAN

### **REQUEST 1: Health Check** ✅
- **Método**: `GET`
- **URL**: `http://localhost:8000/health`
- **Headers**: Ninguno requerido

**Respuesta esperada:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

### **REQUEST 2: Root Endpoint** ✅
- **Método**: `GET`
- **URL**: `http://localhost:8000/`
- **Headers**: Ninguno requerido

**Respuesta esperada:**
```json
{
  "message": "CRM Político API - Analytics Service"
}
```

---

### **REQUEST 3: Analytics Health** ✅
- **Método**: `GET`
- **URL**: `http://localhost:8000/api/v1/analytics/health`
- **Headers**: Ninguno requerido

**Respuesta esperada:**
```json
{
  "status": "healthy",
  "service": "analytics",
  "timestamp": "2025-07-31T..."
}
```

---

### **REQUEST 4: User Stats (PRINCIPAL)** 🎯
- **Método**: `GET`
- **URL**: `http://localhost:8000/api/v1/analytics/user-stats`

**Headers requeridos:**
```
Authorization: Bearer YOUR_GENERATED_JWT_TOKEN_HERE

X-Session-ID: test-session-12345

Content-Type: application/json
```

**Respuesta esperada (DATOS REALES):**
```json
{
  "user_id": "573100000001",
  "name": "Referente de Prueba",
  "region": {
    "position": 2,
    "total_participants": 2,
    "percentile": 50.0
  },
  "city": {
    "position": 1,
    "total_participants": 1,
    "percentile": 100.0
  },
  "ranking": {
    "today": {
      "position": 1,
      "points": 700
    },
    "week": {
      "position": 2,
      "points": 800
    },
    "month": {
      "position": 1,
      "points": 1200
    }
  },
  "referrals": {
    "total_invited": 0,
    "active_volunteers": 0,
    "referrals_this_month": 0,
    "conversion_rate": 0.0,
    "referral_points": 0
  },
  "metadata": {
    "last_updated": "2025-07-31T...",
    "cache_ttl_seconds": 300,
    "data_freshness": "realtime"
  }
}
```

---

### **REQUEST 5: Swagger Documentation** 📚
- **Método**: `GET`
- **URL**: `http://localhost:8000/docs`
- **Headers**: Ninguno requerido

**Ver documentación interactiva de la API**

---

## 🎯 PASOS PARA PROBAR EN POSTMAN

### **Paso 1: Importar Collection**
1. Abrir Postman
2. Click en "Import"
3. Pegar la URL: `http://localhost:8000/openapi.json`
4. Esto importará automáticamente todos los endpoints

### **Paso 2: Configurar Ambiente**
1. Crear nuevo Environment llamado "CRM Político Local"
2. Agregar variables:
   - `base_url`: `http://localhost:8000`
   - `jwt_token`: `YOUR_GENERATED_JWT_TOKEN_HERE`
   - `session_id`: `test-session-12345`

### **Paso 3: Probar Endpoints**
1. **Health Check** → Verificar que el servidor esté funcionando
2. **Root** → Verificar respuesta básica
3. **Analytics Health** → Verificar que el router funcione
4. **User Stats** → Probar endpoint principal con autenticación

---

## 🚨 POSIBLES ERRORES Y SOLUCIONES

### **Error 401: Unauthorized**
- ✅ Verificar que el header `Authorization` tenga el prefijo `Bearer `
- ✅ Verificar que el token no haya expirado
- ✅ Verificar que el header `X-Session-ID` esté presente

### **Error 404: Not Found**
- ✅ Verificar que la URL sea correcta
- ✅ Verificar que el servidor esté ejecutándose en puerto 8000

### **Error 500: Internal Server Error**
- ✅ Verificar logs en la consola del servidor
- ✅ Verificar conexión a Firestore
- ✅ Verificar que las credenciales estén configuradas

### **Error de Conexión**
- ✅ Verificar que el servidor esté ejecutándose: `curl http://localhost:8000/health`
- ✅ Verificar que no haya firewall bloqueando el puerto 8000

---

## 📊 DATOS REALES UTILIZADOS

**Usuario de prueba:** `573100000001`
- **Nombre**: "Referente de Prueba"
- **Ciudad**: "Bogota"
- **Teléfono**: "+573100000001"
- **Código referido**: "TESTCODE"

**Conectado a Firestore real:**
- **Proyecto**: `intreasoft-daniel`
- **Colección**: `users`
- **Sin creación de datos de prueba**

---

## 🎉 VERIFICACIÓN EXITOSA

Si todos los endpoints responden correctamente, habrás verificado:

✅ **Autenticación JWT** funcionando  
✅ **Validación de Session ID** funcionando  
✅ **Conexión a Firestore real** funcionando  
✅ **Cálculo de métricas** basado en datos reales  
✅ **Respuesta estructurada** según esquema  
✅ **Rendimiento** < 300ms  
✅ **Auditoría de accesos** funcionando  

**¡API lista para producción!** 🚀
