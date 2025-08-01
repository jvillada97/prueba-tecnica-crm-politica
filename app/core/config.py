from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # JWT Configuration
    jwt_secret_key: str = "your-secret-key-here"
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 60
    
    # Firestore Configuration
    firestore_project_id: str = "your-project-id"
    firestore_credentials_path: Optional[str] = None
    use_firestore_emulator: bool = False
    
    # Development/Production mode
    environment: str = "development"  # development, staging, production
    
    # API Configuration
    api_title: str = "CRM Político API"
    api_version: str = "1.0.0"
    api_description: str = "API para métricas de usuarios políticos"
    
    # Performance Configuration
    max_response_time_ms: int = 300
    
    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def use_mock_data(self) -> bool:
        """
        Determina si usar datos mock basado en el entorno y disponibilidad de credenciales
        """
        if self.environment == "development" and not self.firestore_credentials_path:
            return True
        return False

settings = Settings()
