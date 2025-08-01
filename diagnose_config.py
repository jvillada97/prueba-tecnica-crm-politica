#!/usr/bin/env python3
"""
Script de diagnóstico para verificar la configuración del servidor
"""

import sys
import os

# Agregar el directorio del proyecto al path
sys.path.append('/Users/jcvillada/Documents/crm-politica/prueba-tecnica-crm-politica')

from app.core.config import settings
from app.services.auth_service import AuthService
from jose import jwt

def main():
    print("🔍 DIAGNÓSTICO DE CONFIGURACIÓN")
    print("=" * 50)
    
    # Verificar configuración
    print(f"\n📋 CONFIGURACIÓN ACTUAL:")
    print(f"   JWT Secret Key: {settings.jwt_secret_key}")
    print(f"   JWT Algorithm: {settings.jwt_algorithm}")
    print(f"   Environment: {settings.environment}")
    print(f"   Firestore Project: {settings.firestore_project_id}")
    print(f"   Firestore Credentials: {settings.firestore_credentials_path}")
    
    # Token removido por seguridad - usar generate_test_token.py
    print(f"\n❌ TOKEN REMOVIDO POR SEGURIDAD")
    print(f"   Usa 'python generate_test_token.py' para generar un token válido")
    return
    
    print(f"\n🧪 PRUEBA DE TOKEN:")
    try:
        payload = AuthService.verify_jwt_token(token)
        print(f"   ✅ Token válido")
        print(f"   User ID: {payload.get('user_id')}")
        print(f"   Name: {payload.get('name')}")
    except Exception as e:
        print(f"   ❌ Token inválido: {e}")
    
    # Verificar variables de entorno
    print(f"\n🌍 VARIABLES DE ENTORNO:")
    print(f"   JWT_SECRET_KEY: {os.getenv('JWT_SECRET_KEY', 'NO DEFINIDA')}")
    print(f"   ENVIRONMENT: {os.getenv('ENVIRONMENT', 'NO DEFINIDA')}")
    
    # Verificar Session ID
    print(f"\n🔑 VALIDACIÓN SESSION ID:")
    session_id = "test-session-12345"
    is_valid = AuthService.validate_session_id(session_id)
    print(f"   Session ID '{session_id}': {'✅ Válido' if is_valid else '❌ Inválido'}")

if __name__ == "__main__":
    main()
