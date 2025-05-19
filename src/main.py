"""
Main entry point for the MEDIS system.
"""

from api import app

if __name__ == "__main__":
    print("Starting MEDIS - Medical Diagnosis Prediction System")
    print("=" * 50)
    print("API server running at http://localhost:5000")
    print("Available endpoints:")
    print("  - POST /api/predict")
    print("  - POST /api/suggest-symptoms")
    print("  - GET  /api/info")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=True) 