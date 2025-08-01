# 🚨 GUÍA DE TROUBLESHOOTING POSTMAN

## 🔍 PROBLEMA: curl funciona, Postman no

### ✅ CURL QUE FUNCIONA:
```bash
curl -X GET "http://localhost:8000/api/v1/analytics/user-stats" \
     -H "Authorization: Bearer YOUR_GENERATED_JWT_TOKEN_HERE" \
     -H "x-session-id: test-session-12345" \
     -H "Content-Type: application/json"
```

---

## 🔧 SOLUCIONES PASO A PASO

### **OPCIÓN 1: Usar Colección Simple (Recomendado)**

1. **Importar**: `CRM_Politico_Debug_Collection.json`
2. **Probar**: Request "TEST - User Stats HARDCODED"
3. **Verificar**: Que devuelva los datos del usuario

### **OPCIÓN 2: Configurar Manualmente**

1. **Crear nuevo request en Postman:**
   - **Method**: `GET`
   - **URL**: `http://localhost:8000/api/v1/analytics/user-stats`

2. **Agregar Headers exactos:**
   ```
   Authorization: Bearer YOUR_GENERATED_JWT_TOKEN_HERE
   
   x-session-id: test-session-12345
   
   Content-Type: application/json
   ```

### **OPCIÓN 3: Verificar Variables de Entorno**

Si usas la colección original:

1. **Ir a**: Collection → Variables
2. **Verificar**:
   - `base_url`: `http://localhost:8000`
   - `jwt_token`: `YOUR_GENERATED_JWT_TOKEN_HERE`
   - `session_id`: `test-session-12345`

---

## 🕵️ DEBUGGING EN POSTMAN

### **Verificar que el request se construye correctamente:**

1. **Abrir**: Console en Postman (View → Show Postman Console)
2. **Enviar**: Request
3. **Revisar**: Headers reales enviados
4. **Comparar**: Con el curl que funciona

### **Buscar diferencias comunes:**

- ❌ **Headers duplicados** (Authorization aparece 2 veces)
- ❌ **Variables mal resueltas** ({{variable}} no se expande)
- ❌ **URL malformada** (espacios extra, caracteres especiales)
- ❌ **Case sensitivity** (X-Session-ID vs x-session-id)

---

## 🎯 RESPUESTA ESPERADA

Si todo está correcto, deberías ver:

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
    "today": {"position": 1, "points": 700},
    "week": {"position": 2, "points": 800}, 
    "month": {"position": 1, "points": 1200}
  },
  "referrals": {
    "total_invited": 0,
    "active_volunteers": 0,
    "referrals_this_month": 0,
    "conversion_rate": 0.0,
    "referral_points": 0
  },
  "metadata": {
    "last_updated": "2025-08-01T...",
    "cache_ttl_seconds": 300,
    "data_freshness": "realtime"
  }
}
```

---

## 🚨 SI SIGUE FALLANDO

### **Captura de pantalla de:**
1. Headers en Postman (pestaña Headers)
2. URL completa 
3. Error exacto recibido
4. Console de Postman

### **Información adicional:**
- ¿Qué status code recibes? (401, 400, 500, etc.)
- ¿Cuál es el mensaje de error exacto?
- ¿Aparece algo en el Console de Postman?

**El request DEBE funcionar si está configurado exactamente igual que el curl exitoso.**
