#!/usr/bin/env python3
"""
Script para generar tokens JWT de prueba
"""

from jose import jwt
from datetime import datetime, timedelta

# Configuración
SECRET_KEY = "your-super-secret-jwt-key-here-change-in-production"
ALGORITHM = "HS256"

def generate_test_token(user_id: str = "573100000001", name: str = "Usuario Real Firestore"):
    """
    Genera un token JWT de prueba con ID de usuario real
    """
    payload = {
        "user_id": user_id,
        "name": name,
        "exp": datetime.utcnow() + timedelta(hours=24)  # Expira en 24 horas
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

if __name__ == "__main__":
    # Generar tokens de prueba
    test_token = generate_test_token()
    print(f"Token de prueba generado:")
    print(f"Bearer {test_token}")
    print()
    
    # Comando curl de ejemplo
    print("Comando curl de ejemplo:")
    print(f"""curl -X GET "http://localhost:8000/api/v1/analytics/user-stats" \\
     -H "Authorization: Bearer {test_token}" \\
     -H "X-Session-ID: test-session-12345" \\
     -H "Content-Type: application/json"
""")
