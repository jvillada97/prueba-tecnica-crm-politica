#!/bin/bash

# Script para ejecutar el servidor de desarrollo
echo "🚀 Iniciando servidor CRM Político API..."

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "📚 Instalando dependencias..."
pip install -r requirements.txt

# Verificar que existe el archivo .env
if [ ! -f ".env" ]; then
    echo "⚠️  Archivo .env no encontrado. Copiando desde .env.example..."
    cp .env.example .env
    echo "🔑 Por favor, edita el archivo .env con tus configuraciones reales"
fi

# Ejecutar servidor
echo "🌟 Iniciando servidor FastAPI..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
