#!/usr/bin/env python3
"""
Script para crear datos de prueba en Firestore
"""

import sys
import os
import asyncio
from datetime import datetime

# Agregar el directorio raíz al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.firestore_service import firestore_service

async def create_test_data():
    if firestore_service.use_mock:
        print("⚠️ Está en modo mock, cambiar ENVIRONMENT=production en .env")
        return
    
    print('📝 Creando datos de prueba en Firestore...')
    
    user_id = "vol_12345"
    
    try:
        # 1. Crear usuario
        user_data = {
            "name": "María González",
            "email": "maria.gonzalez@ejemplo.com",
            "region": "Bogotá",
            "city": "Chapinero",
            "created_at": datetime.utcnow()
        }
        firestore_service.db.collection('users').document(user_id).set(user_data)
        print(f"✅ Usuario creado: {user_data['name']}")
        
        # 2. Ranking diario
        daily_ranking = {
            "position": 2,
            "points": 850,
            "date": datetime.utcnow()
        }
        firestore_service.db.collection('daily_rankings').document(user_id).set(daily_ranking)
        print(f"✅ Ranking diario: Posición {daily_ranking['position']}")
        
        # 3. Ranking semanal
        weekly_ranking = {
            "position": 4,
            "points": 3200,
            "week": datetime.utcnow().isocalendar()[1]
        }
        firestore_service.db.collection('weekly_rankings').document(user_id).set(weekly_ranking)
        print(f"✅ Ranking semanal: Posición {weekly_ranking['position']}")
        
        # 4. Ranking mensual
        monthly_ranking = {
            "position": 5,
            "points": 12500,
            "month": datetime.utcnow().month
        }
        firestore_service.db.collection('monthly_rankings').document(user_id).set(monthly_ranking)
        print(f"✅ Ranking mensual: Posición {monthly_ranking['position']}")
        
        # 5. Estadísticas geográficas
        geo_stats = {
            "region_position": 3,
            "region_total": 150,
            "region_percentile": 98.0,
            "city_position": 1,
            "city_total": 45,
            "city_percentile": 100.0
        }
        firestore_service.db.collection('geographical_stats').document(user_id).set(geo_stats)
        print(f"✅ Estadísticas geográficas: Región #{geo_stats['region_position']}, Ciudad #{geo_stats['city_position']}")
        
        # 6. Estadísticas de referidos
        referral_stats = {
            "total_invited": 23,
            "active_volunteers": 18,
            "referrals_this_month": 7,
            "conversion_rate": 78.3,
            "referral_points": 4600
        }
        firestore_service.db.collection('referral_stats').document(user_id).set(referral_stats)
        print(f"✅ Estadísticas de referidos: {referral_stats['total_invited']} invitados")
        
        print("\n🎉 ¡Datos de prueba creados exitosamente!")
        print(f"👤 Usuario: {user_id}")
        print("🔗 Ahora puedes probar el endpoint con datos reales")
        
    except Exception as e:
        print(f"❌ Error creando datos: {e}")

if __name__ == "__main__":
    asyncio.run(create_test_data())
