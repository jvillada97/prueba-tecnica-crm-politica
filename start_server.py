#!/usr/bin/env python3
"""
Script simple para arrancar el servidor FastAPI
"""

import os
import sys

# Cambiar al directorio correcto
os.chdir('/Users/jcvillada/Documents/crm-politica/prueba-tecnica-crm-politica')

# Agregar el directorio al path
sys.path.insert(0, os.getcwd())

# Ejecutar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
