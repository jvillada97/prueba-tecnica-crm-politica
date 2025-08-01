#!/usr/bin/env python3
"""
Script para verificar la validez de tokens JWT
"""

from jose import jwt, JWTError
from datetime import datetime
import sys

# Configuración (debe coincidir con el servidor)
SECRET_KEY = "your-super-secret-jwt-key-here-change-in-production"
ALGORITHM = "HS256"

def verify_token(token_string):
    """
    Verifica si un token JWT es válido
    """
    try:
        # Remover 'Bearer ' si está presente
        if token_string.startswith('Bearer '):
            token_string = token_string[7:]
        
        # Decodificar el token
        payload = jwt.decode(token_string, SECRET_KEY, algorithms=[ALGORITHM])
        
        print("✅ TOKEN VÁLIDO")
        print("-" * 20)
        print(f"User ID: {payload.get('user_id')}")
        print(f"Name: {payload.get('name')}")
        
        # Verificar expiración
        exp_timestamp = payload.get('exp')
        if exp_timestamp:
            exp_datetime = datetime.fromtimestamp(exp_timestamp)
            now = datetime.utcnow()
            
            print(f"Expira: {exp_datetime}")
            print(f"Ahora: {now}")
            
            if now < exp_datetime:
                time_left = exp_datetime - now
                print(f"⏰ Tiempo restante: {time_left}")
                print("🟢 Token NO expirado")
            else:
                print("🔴 Token EXPIRADO")
                return False
        
        return True
        
    except JWTError as e:
        print(f"❌ TOKEN INVÁLIDO: {e}")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
    print("🔍 VERIFICADOR DE TOKENS JWT")
    print("=" * 40)
    
    if len(sys.argv) > 1:
        # Token pasado como argumento
        token = sys.argv[1]
    else:
        # Solicitar token interactivamente
        print("\nPega el token JWT (con o sin 'Bearer '):")
        token = input().strip()
    
    if not token:
        print("❌ No se proporcionó ningún token")
        return
    
    print(f"\n🔍 Verificando token...")
    is_valid = verify_token(token)
    
    if is_valid:
        print("\n🎉 ¡El token es válido y se puede usar!")
    else:
        print("\n💡 Genera un nuevo token con:")
        print("   python generate_test_token.py")

if __name__ == "__main__":
    main()
