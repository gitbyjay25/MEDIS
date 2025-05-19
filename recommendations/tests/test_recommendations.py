import sys
import os
import json

# Add the backend directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Import the function
from disease_recommendations import get_recommendations

def test_recommendations():
    print("Testing get_recommendations function...")
    
    # Test different diseases
    test_diseases = [
        "Chicken Pox",
        "Depression", 
        "Hypertension", 
        "Malaria", 
        "Typhoid",
        "Non-existent Disease"
    ]
    
    for disease in test_diseases:
        print(f"\nTesting recommendations for: {disease}")
        recommendations = get_recommendations(disease)
        if recommendations:
            print(f"✅ Got recommendations with keys: {list(recommendations.keys())}")
            if "medicines" in recommendations:
                print(f"  - Medicines: {len(recommendations['medicines'])} items")
            if "diet" in recommendations:
                print(f"  - Diet: {len(recommendations['diet'])} items")
            if "exercise" in recommendations:
                print(f"  - Exercise: {len(recommendations['exercise'])} items")
        else:
            print(f"❌ No recommendations found for {disease}")

if __name__ == "__main__":
    test_recommendations() 