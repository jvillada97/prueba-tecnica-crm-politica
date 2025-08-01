#!/bin/bash

# Script para ejecutar tests
echo "🧪 Ejecutando tests para CRM Político API..."

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Instalar pytest si no está instalado
pip install pytest pytest-asyncio httpx

# Ejecutar tests
echo "🔍 Ejecutando tests..."
python -m pytest tests/ -v --tb=short

echo "✅ Tests completados"
