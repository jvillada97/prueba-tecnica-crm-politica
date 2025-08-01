#!/usr/bin/env python3
"""
Script para explorar la base de datos Firestore real
"""

import asyncio
import json
from datetime import datetime
from google.cloud import firestore
from app.core.config import settings

def connect_to_firestore():
    """Conecta a Firestore usando las credenciales del service account"""
    try:
        print(f"🔄 Conectando a Firestore...")
        print(f"   Project ID: {settings.firestore_project_id}")
        print(f"   Credentials: {settings.firestore_credentials_path}")
        
        # Conectar usando el archivo de credenciales
        db = firestore.Client.from_service_account_json(
            settings.firestore_credentials_path,
            project=settings.firestore_project_id
        )
        
        print("✅ Conexión a Firestore exitosa")
        return db
        
    except Exception as e:
        print(f"❌ Error conectando a Firestore: {e}")
        return None

def explore_collections(db):
    """Explora todas las colecciones disponibles"""
    try:
        print("\n📁 Explorando colecciones disponibles...")
        
        collections = list(db.collections())
        
        if not collections:
            print("   ⚠️  No se encontraron colecciones en la base de datos")
            return []
        
        collection_names = []
        for collection in collections:
            collection_names.append(collection.id)
            print(f"   📂 {collection.id}")
        
        return collection_names
        
    except Exception as e:
        print(f"❌ Error explorando colecciones: {e}")
        return []

def explore_collection_documents(db, collection_name, limit=5):
    """Explora documentos en una colección específica"""
    try:
        print(f"\n📄 Explorando documentos en '{collection_name}' (límite: {limit})...")
        
        collection_ref = db.collection(collection_name)
        docs = collection_ref.limit(limit).stream()
        
        documents = []
        for doc in docs:
            doc_data = doc.to_dict()
            documents.append({
                'id': doc.id,
                'data': doc_data
            })
            
            print(f"   📝 Documento ID: {doc.id}")
            print(f"      Campos: {list(doc_data.keys()) if doc_data else 'Vacío'}")
            
            # Mostrar algunos valores de ejemplo (sin datos sensibles)
            if doc_data:
                for key, value in list(doc_data.items())[:3]:  # Solo primeros 3 campos
                    if isinstance(value, str) and len(value) > 50:
                        value = f"{value[:47]}..."
                    print(f"      {key}: {value}")
                if len(doc_data) > 3:
                    print(f"      ... y {len(doc_data) - 3} campos más")
            print()
        
        if not documents:
            print(f"   ⚠️  No se encontraron documentos en '{collection_name}'")
        
        return documents
        
    except Exception as e:
        print(f"❌ Error explorando documentos en '{collection_name}': {e}")
        return []

def search_user_related_collections(db):
    """Busca colecciones que podrían contener datos de usuarios"""
    print("\n🔍 Buscando colecciones relacionadas con usuarios...")
    
    user_related_terms = ['user', 'profile', 'member', 'participant', 'ranking', 'stats', 'metric']
    
    try:
        collections = list(db.collections())
        user_collections = []
        
        for collection in collections:
            collection_name = collection.id.lower()
            if any(term in collection_name for term in user_related_terms):
                user_collections.append(collection.id)
                print(f"   🎯 {collection.id} (posiblemente relacionada con usuarios)")
        
        if not user_collections:
            print("   ⚠️  No se encontraron colecciones obviamente relacionadas con usuarios")
        
        return user_collections
        
    except Exception as e:
        print(f"❌ Error buscando colecciones de usuarios: {e}")
        return []

def get_sample_document_structure(db, collection_name):
    """Obtiene la estructura de un documento de muestra"""
    try:
        print(f"\n🏗️  Analizando estructura de documentos en '{collection_name}'...")
        
        collection_ref = db.collection(collection_name)
        docs = collection_ref.limit(1).stream()
        
        for doc in docs:
            doc_data = doc.to_dict()
            if doc_data:
                print(f"   📋 Estructura del documento '{doc.id}':")
                
                def analyze_field(key, value, indent="      "):
                    if isinstance(value, dict):
                        print(f"{indent}{key}: {{")
                        for sub_key, sub_value in value.items():
                            analyze_field(sub_key, sub_value, indent + "  ")
                        print(f"{indent}}}")
                    elif isinstance(value, list):
                        print(f"{indent}{key}: [{type(value[0]).__name__ if value else 'empty'}] (array)")
                    else:
                        print(f"{indent}{key}: {type(value).__name__}")
                
                for key, value in doc_data.items():
                    analyze_field(key, value)
                
                return doc_data
        
        print(f"   ⚠️  No se encontraron documentos en '{collection_name}'")
        return None
        
    except Exception as e:
        print(f"❌ Error analizando estructura: {e}")
        return None

def main():
    """Función principal de exploración"""
    print("🚀 Explorando Base de Datos Firestore Real")
    print("=" * 50)
    
    # Conectar a Firestore
    db = connect_to_firestore()
    if not db:
        return
    
    # Explorar colecciones
    collections = explore_collections(db)
    if not collections:
        return
    
    # Buscar colecciones relacionadas con usuarios
    user_collections = search_user_related_collections(db)
    
    # Explorar cada colección
    for collection_name in collections:
        print(f"\n{'='*60}")
        documents = explore_collection_documents(db, collection_name, limit=3)
        
        if documents:
            get_sample_document_structure(db, collection_name)
    
    # Resumen
    print(f"\n{'='*60}")
    print("📊 RESUMEN DE LA EXPLORACIÓN")
    print(f"   • Total colecciones encontradas: {len(collections)}")
    print(f"   • Colecciones: {', '.join(collections)}")
    
    if user_collections:
        print(f"   • Colecciones relevantes para usuarios: {', '.join(user_collections)}")
    
    print(f"\n✅ Exploración completada - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
