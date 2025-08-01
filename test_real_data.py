#!/usr/bin/env python3
"""
Script para probar la funcionalidad con datos reales de Firestore
"""

import asyncio
import sys
import os

# Agregar el directorio del proyecto al path
sys.path.append('/Users/jcvillada/Documents/crm-politica/prueba-tecnica-crm-politica')

from app.services.firestore_service import FirestoreService
from app.services.analytics_service import AnalyticsService

async def test_real_firestore_data():
    """
    Prueba la funcionalidad con datos reales
    """
    print("🚀 Probando funcionalidad con datos reales de Firestore")
    print("=" * 60)
    
    try:
        # Inicializar servicios
        firestore_service = FirestoreService()
        analytics_service = AnalyticsService()
        
        # ID de usuario real encontrado en la exploración
        user_id = "573100000001"
        
        print(f"📊 Obteniendo estadísticas para usuario: {user_id}")
        print("-" * 40)
        
        # Probar obtención de perfil
        print("1. 👤 Obteniendo perfil de usuario...")
        user_profile = await firestore_service.get_user_profile(user_id)
        
        if user_profile:
            print(f"   ✅ Usuario encontrado: {user_profile.get('name', 'Sin nombre')}")
            print(f"   📍 Ciudad: {user_profile.get('city', 'No especificada')}")
            print(f"   📞 Teléfono: {user_profile.get('phone', 'No especificado')}")
            print(f"   🎫 Código de referido: {user_profile.get('referral_code', 'No tiene')}")
        else:
            print("   ❌ Usuario no encontrado")
            return
        
        # Probar estadísticas de ranking
        print("\n2. 🏆 Calculando estadísticas de ranking...")
        ranking_stats = await firestore_service.get_user_ranking_stats(user_id)
        print(f"   📈 Posición hoy: {ranking_stats['today']['position']} ({ranking_stats['today']['points']} puntos)")
        print(f"   📊 Posición semana: {ranking_stats['week']['position']} ({ranking_stats['week']['points']} puntos)")
        print(f"   📅 Posición mes: {ranking_stats['month']['position']} ({ranking_stats['month']['points']} puntos)")
        
        # Probar estadísticas geográficas
        print("\n3. 🌍 Calculando estadísticas geográficas...")
        geo_stats = await firestore_service.get_geographical_stats(user_id)
        
        region = geo_stats['region']
        city = geo_stats['city']
        
        print(f"   🏙️  Región: Posición {region['position']} de {region['total_participants']} (percentil {region['percentile']}%)")
        print(f"   🌆 Ciudad: Posición {city['position']} de {city['total_participants']} (percentil {city['percentile']}%)")
        
        # Probar estadísticas de referidos
        print("\n4. 👥 Calculando estadísticas de referidos...")
        referral_stats = await firestore_service.get_referral_stats(user_id)
        
        print(f"   📢 Total invitados: {referral_stats['total_invited']}")
        print(f"   ✅ Voluntarios activos: {referral_stats['active_volunteers']}")
        print(f"   📆 Referidos este mes: {referral_stats['referrals_this_month']}")
        print(f"   📊 Tasa de conversión: {referral_stats['conversion_rate']}%")
        print(f"   🎯 Puntos por referidos: {referral_stats['referral_points']}")
        
        # Probar servicio completo de analytics
        print("\n5. 🔄 Obteniendo respuesta completa del servicio de analytics...")
        complete_stats = await analytics_service.get_user_stats(user_id)
        
        print(f"   ✅ Respuesta generada exitosamente")
        print(f"   👤 Usuario: {complete_stats.user_id} - {complete_stats.name}")
        print(f"   📍 Región: {complete_stats.region.position}/{complete_stats.region.total_participants}")
        print(f"   🏆 Ranking hoy: {complete_stats.ranking.today.position}")
        print(f"   👥 Referidos: {complete_stats.referrals.total_invited}")
        
        print("\n" + "=" * 60)
        print("✅ PRUEBA COMPLETADA EXITOSAMENTE")
        print("🎉 El servicio está funcionando correctamente con datos reales de Firestore")
        
    except Exception as e:
        print(f"\n❌ ERROR durante la prueba: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_real_firestore_data())
