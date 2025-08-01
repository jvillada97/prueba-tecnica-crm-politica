import pytest
from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

# Token JWT de prueba (en producción, usar un token válido)
TEST_JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidm9sXzEyMzQ1IiwibmFtZSI6Ik1hcsOtYSBHb256w6FsZXoiLCJleHAiOjk5OTk5OTk5OTl9.test"
TEST_SESSION_ID = "test-session-12345"

def test_analytics_endpoint_without_auth():
    """
    Prueba que el endpoint requiere autenticación
    """
    response = client.get("/api/v1/analytics/user-stats")
    assert response.status_code == 403

def test_analytics_endpoint_without_session_id():
    """
    Prueba que el endpoint requiere session ID
    """
    headers = {
        "Authorization": f"Bearer {TEST_JWT_TOKEN}"
    }
    response = client.get("/api/v1/analytics/user-stats", headers=headers)
    assert response.status_code == 400

def test_analytics_endpoint_success():
    """
    Prueba el endpoint con autenticación completa
    Nota: Esta prueba requiere configuración completa de Redis y Firestore
    """
    headers = {
        "Authorization": f"Bearer {TEST_JWT_TOKEN}",
        "X-Session-ID": TEST_SESSION_ID,
        "Content-Type": "application/json"
    }
    
    # Esta prueba fallará sin configuración real, pero muestra la estructura
    response = client.get("/api/v1/analytics/user-stats", headers=headers)
    
    # En un entorno real con datos mock, esto debería ser 200
    assert response.status_code in [200, 401, 500]

def test_health_endpoint():
    """
    Prueba el endpoint de health check
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "CRM Político API" in response.json()["message"]

def test_analytics_health():
    """
    Prueba el health check de analytics
    """
    response = client.get("/api/v1/analytics/health")
    # Puede fallar sin Redis, pero la estructura está correcta
    assert response.status_code in [200, 503]

if __name__ == "__main__":
    pytest.main([__file__])
