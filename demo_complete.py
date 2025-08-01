#!/usr/bin/env python3
"""
Demostración completa del servicio con datos reales
"""

import asyncio
import json
from datetime import datetime
import sys
import os

# Agregar el directorio del proyecto al path
sys.path.append('/Users/jcvillada/Documents/crm-politica/prueba-tecnica-crm-politica')

from app.services.analytics_service import AnalyticsService

async def demo_complete_service():
    """
    Demostración completa del servicio de analytics con datos reales
    """
    print("🚀 DEMOSTRACIÓN COMPLETA - CRM POLÍTICO API")
    print("=" * 70)
    print("🔥 Usando datos REALES de Firestore")
    print("📊 Proyecto: intreasoft-daniel")
    print("=" * 70)
    
    try:
        # Inicializar servicio
        analytics_service = AnalyticsService()
        
        # Usuario real de Firestore
        user_id = "573100000001"
        
        print(f"\n🎯 OBTENIENDO MÉTRICAS COMPLETAS PARA USUARIO: {user_id}")
        print("-" * 50)
        
        # Obtener estadísticas completas
        start_time = datetime.now()
        user_stats = await analytics_service.get_user_stats(user_id)
        end_time = datetime.now()
        
        response_time = (end_time - start_time).total_seconds() * 1000
        
        print(f"⚡ Tiempo de respuesta: {response_time:.2f}ms (objetivo: <300ms)")
        print(f"✅ Estado: {'EXITOSO' if response_time < 300 else 'LENTO'}")
        
        print(f"\n📋 RESPUESTA ESTRUCTURADA:")
        print("-" * 30)
        
        # Mostrar respuesta de manera organizada
        print(f"👤 USUARIO:")
        print(f"   ID: {user_stats.user_id}")
        print(f"   Nombre: {user_stats.name}")
        
        print(f"\n🏆 RANKING:")
        print(f"   Hoy: Posición {user_stats.ranking.today.position} ({user_stats.ranking.today.points} puntos)")
        print(f"   Semana: Posición {user_stats.ranking.week.position} ({user_stats.ranking.week.points} puntos)")
        print(f"   Mes: Posición {user_stats.ranking.month.position} ({user_stats.ranking.month.points} puntos)")
        
        print(f"\n🌍 GEOGRAFÍA:")
        print(f"   Región: Pos. {user_stats.region.position}/{user_stats.region.total_participants} (percentil {user_stats.region.percentile}%)")
        print(f"   Ciudad: Pos. {user_stats.city.position}/{user_stats.city.total_participants} (percentil {user_stats.city.percentile}%)")
        
        print(f"\n👥 REFERIDOS:")
        print(f"   Total invitados: {user_stats.referrals.total_invited}")
        print(f"   Voluntarios activos: {user_stats.referrals.active_volunteers}")
        print(f"   Referidos este mes: {user_stats.referrals.referrals_this_month}")
        print(f"   Tasa de conversión: {user_stats.referrals.conversion_rate}%")
        print(f"   Puntos por referidos: {user_stats.referrals.referral_points}")
        
        print(f"\n📊 METADATA:")
        print(f"   Última actualización: {user_stats.metadata.last_updated}")
        print(f"   TTL de cache: {user_stats.metadata.cache_ttl_seconds}s")
        print(f"   Frescura de datos: {user_stats.metadata.data_freshness}")
        
        # Mostrar JSON completo
        print(f"\n🔧 RESPUESTA JSON COMPLETA:")
        print("-" * 35)
        
        # Convertir a dict para mostrar como JSON
        response_dict = {
            "user_id": user_stats.user_id,
            "name": user_stats.name,
            "region": {
                "position": user_stats.region.position,
                "total_participants": user_stats.region.total_participants,
                "percentile": user_stats.region.percentile
            },
            "city": {
                "position": user_stats.city.position,
                "total_participants": user_stats.city.total_participants,
                "percentile": user_stats.city.percentile
            },
            "ranking": {
                "today": {
                    "position": user_stats.ranking.today.position,
                    "points": user_stats.ranking.today.points
                },
                "week": {
                    "position": user_stats.ranking.week.position,
                    "points": user_stats.ranking.week.points
                },
                "month": {
                    "position": user_stats.ranking.month.position,
                    "points": user_stats.ranking.month.points
                }
            },
            "referrals": {
                "total_invited": user_stats.referrals.total_invited,
                "active_volunteers": user_stats.referrals.active_volunteers,
                "referrals_this_month": user_stats.referrals.referrals_this_month,
                "conversion_rate": user_stats.referrals.conversion_rate,
                "referral_points": user_stats.referrals.referral_points
            },
            "metadata": {
                "last_updated": user_stats.metadata.last_updated.isoformat(),
                "cache_ttl_seconds": user_stats.metadata.cache_ttl_seconds,
                "data_freshness": user_stats.metadata.data_freshness
            }
        }
        
        print(json.dumps(response_dict, indent=2, ensure_ascii=False))
        
        print(f"\n" + "=" * 70)
        print("🎉 DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
        print("✅ El servicio está funcionando perfectamente con datos reales")
        print("🔥 Listo para usarse en producción con Firestore")
        print("📊 Sin creación de datos de prueba en la base de datos real")
        print("=" * 70)
        
        # Instrucciones para uso
        print(f"\n📖 INSTRUCCIONES PARA USAR EL ENDPOINT:")
        print("-" * 40)
        print("1. Ejecutar servidor: python main.py")
        print("2. Generar token: python generate_test_token.py")
        print("3. Usar token con curl:")
        print(f'   curl -X GET "http://localhost:8000/api/v1/analytics/user-stats" \\')
        print(f'        -H "Authorization: Bearer {{TOKEN}}" \\')
        print(f'        -H "X-Session-ID: test-session-12345"')
        
    except Exception as e:
        print(f"\n❌ ERROR durante la demostración: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(demo_complete_service())
