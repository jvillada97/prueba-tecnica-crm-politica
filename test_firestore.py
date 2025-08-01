#!/usr/bin/env python3
"""
Script para probar la conexión a Firestore
"""

import sys
import os
import asyncio

# Agregar el directorio raíz al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.firestore_service import firestore_service

async def test_firestore():
    print('🔗 Probando conexión a Firestore...')
    health = firestore_service.health_check()
    print(f'Estado: {health}')
    
    if not firestore_service.use_mock:
        print('✅ Usando Firestore REAL')
        # Probar obtener perfil de usuario
        try:
            profile = await firestore_service.get_user_profile('vol_12345')
            print(f'Perfil de usuario: {profile}')
        except Exception as e:
            print(f'Error al obtener perfil: {e}')
    else:
        print('⚠️ Usando datos MOCK')
        profile = await firestore_service.get_user_profile('vol_12345')
        print(f'Perfil mock: {profile}')

if __name__ == "__main__":
    asyncio.run(test_firestore())
