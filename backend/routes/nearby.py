from flask import Blueprint, request, jsonify
import requests

nearby_bp = Blueprint('nearby', __name__)

@nearby_bp.route('/api/nearby-hospitals', methods=['POST'])
def nearby_hospitals():
    data = request.get_json()
    lat = data.get('lat')
    lng = data.get('lng')
    # Use OpenStreetMap Nominatim API to fetch real hospitals nearby
    url = f"https://nominatim.openstreetmap.org/search?format=json&q=hospital&limit=10&lat={lat}&lon={lng}"
    response = requests.get(url, headers={"User-Agent": "MEDIS/1.0"})
    results = response.json()
    hospitals = []
    for r in results:
        hospitals.append({
            'name': r.get('display_name', 'Hospital'),
            'lat': float(r['lat']),
            'lng': float(r['lon']),
            'verified': True,
            'address': r.get('display_name', ''),
            'type': 'hospital'
        })
    return jsonify({'hospitals': hospitals})

@nearby_bp.route('/api/verified-professionals', methods=['POST'])
def verified_professionals():
    data = request.get_json()
    lat = data.get('lat')
    lng = data.get('lng')
    # TODO: Integrate HPR API for real verified professionals
    professionals = [
        {
            'name': 'Dr. A. Sharma',
            'specialty': 'Cardiologist',
            'lat': lat + 0.0015,
            'lng': lng + 0.0015,
            'verified': True,
            'address': '789 Heart Lane',
            'contact': '+91-9876543210'
        },
        {
            'name': 'Dr. P. Verma',
            'specialty': 'General Physician',
            'lat': lat - 0.0012,
            'lng': lng - 0.0012,
            'verified': True,
            'address': '321 Wellness Rd',
            'contact': '+91-9123456780'
        }
    ]
    return jsonify({'professionals': professionals}) 