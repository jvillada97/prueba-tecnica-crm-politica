# Mock simple para structlog para desarrollo
import logging

class MockLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def info(self, message, **kwargs):
        self.logger.info(f"{message} - {kwargs}")
        
    def error(self, message, **kwargs):
        self.logger.error(f"{message} - {kwargs}")
        
    def warning(self, message, **kwargs):
        self.logger.warning(f"{message} - {kwargs}")

def get_logger():
    return MockLogger()

def configure(**kwargs):
    pass
