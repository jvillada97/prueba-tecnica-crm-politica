#!/usr/bin/env python3
"""
Generador interactivo de tokens JWT
"""

from jose import jwt
from datetime import datetime, timedelta
import sys

# Configuración
SECRET_KEY = "your-super-secret-jwt-key-here-change-in-production"
ALGORITHM = "HS256"

def generate_token(user_id: str, name: str = "Usuario", hours: int = 24):
    """
    Genera un token JWT personalizado
    """
    payload = {
        "user_id": user_id,
        "name": name,
        "exp": datetime.utcnow() + timedelta(hours=hours)
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def main():
    print("🔑 GENERADOR DE TOKENS JWT")
    print("=" * 40)
    
    # Si se pasan argumentos por línea de comandos
    if len(sys.argv) >= 2:
        user_id = sys.argv[1]
        name = sys.argv[2] if len(sys.argv) >= 3 else "Usuario CLI"
        hours = int(sys.argv[3]) if len(sys.argv) >= 4 else 24
    else:
        # Modo interactivo
        print("\nOpciones de usuarios disponibles:")
        print("1. 573100000001 (Referente de Prueba)")
        print("2. 573227281752 (Usuario Buitrago)")
        print("3. Personalizado")
        
        choice = input("\nSelecciona opción (1-3): ").strip()
        
        if choice == "1":
            user_id = "573100000001"
            name = "Referente de Prueba"
        elif choice == "2":
            user_id = "573227281752"
            name = "Usuario Buitrago"
        elif choice == "3":
            user_id = input("Ingresa user_id: ").strip()
            name = input("Ingresa nombre (opcional): ").strip() or "Usuario Personalizado"
        else:
            print("❌ Opción inválida, usando usuario por defecto")
            user_id = "573100000001"
            name = "Usuario Por Defecto"
        
        hours = input("Horas de duración (24): ").strip()
        hours = int(hours) if hours.isdigit() else 24
    
    # Generar token
    token = generate_token(user_id, name, hours)
    
    print(f"\n✅ TOKEN GENERADO:")
    print("-" * 30)
    print(f"Usuario: {name}")
    print(f"ID: {user_id}")
    print(f"Duración: {hours} horas")
    print(f"\nToken:")
    print(f"Bearer {token}")
    
    print(f"\n📋 PARA POSTMAN:")
    print("-" * 20)
    print(f"Authorization: Bearer {token}")
    print(f"X-Session-ID: test-session-12345")
    
    print(f"\n🔧 COMANDO CURL:")
    print("-" * 15)
    print(f"""curl -X GET "http://localhost:8000/api/v1/analytics/user-stats" \\
     -H "Authorization: Bearer {token}" \\
     -H "X-Session-ID: test-session-12345" \\
     -H "Content-Type: application/json"
""")

if __name__ == "__main__":
    main()
