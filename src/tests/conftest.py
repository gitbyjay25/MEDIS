"""
Test configuration for the MEDIS system.
"""

import pytest
from ..api import app as flask_app

@pytest.fixture
def app():
    """Create and configure a test Flask application."""
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test CLI runner for the Flask application."""
    return app.test_cli_runner() 