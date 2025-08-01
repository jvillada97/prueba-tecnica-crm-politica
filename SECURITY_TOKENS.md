# 🔐 GESTIÓN SEGURA DE TOKENS JWT

## ⚠️ IMPORTANTE - SEGURIDAD

Los tokens JWT han sido removidos de todos los archivos por razones de seguridad. 

## 🛠️ CÓMO GENERAR TOKENS VÁLIDOS

### Opción 1: Generación Automática
```bash
python generate_test_token.py
```

### Opción 2: Generación Interactiva  
```bash
python generate_token_interactive.py
```

### Opción 3: Verificar Token Existente
```bash
python verify_token.py YOUR_TOKEN_HERE
```

## 📋 ARCHIVOS LIMPIADOS

Los siguientes archivos fueron limpiados de tokens hardcodeados:

- ✅ `CRM_Politico_Debug_Collection.json`
- ✅ `CRM_Politico_Postman_Collection.json` 
- ✅ `diagnose_config.py`
- ✅ `POSTMAN_GUIDE.md`
- ✅ `POSTMAN_TROUBLESHOOTING.md`

## 🔒 BUENAS PRÁCTICAS

1. **Nunca** commits tokens reales en git
2. **Siempre** usa variables de entorno para producción
3. **Genera** tokens frescos para cada sesión de testing
4. **Verifica** la expiración antes de usar un token

## 🚀 PROCESO RECOMENDADO

1. Generar token: `python generate_test_token.py`
2. Copiar el token generado
3. Reemplazar `YOUR_JWT_TOKEN_HERE` en Postman
4. Probar el endpoint

## 📞 SOPORTE

Si tienes problemas generando tokens, verifica:
- ✅ Variables de entorno configuradas (`.env`)
- ✅ Secret key coincide entre generación y verificación  
- ✅ Token no expirado (check con `verify_token.py`)
