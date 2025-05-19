"""
Disease recommendations including medicines, precautions, diet, exercise and lifestyle changes.
"""

DISEASE_RECOMMENDATIONS = {
    "Hypertension": {
        "medicines": [
            {"name": "Amlodipine", "dosage": "5-10mg once daily", "purpose": "Blood pressure control"},
            {"name": "Losartan", "dosage": "50-100mg once daily", "purpose": "Blood pressure control"},
            {"name": "Hydrochlorothiazide", "dosage": "12.5-25mg once daily", "purpose": "Diuretic"}
        ],
        "precautions": [
            "Monitor blood pressure regularly",
            "Reduce salt intake",
            "Avoid excessive alcohol",
            "Stop smoking",
            "Regular exercise"
        ],
        "diet": [
            "Follow DASH diet (rich in fruits, vegetables, and low-fat dairy)",
            "Limit sodium to less than 2,300mg per day",
            "Increase potassium-rich foods",
            "Avoid processed foods",
            "Eat more whole grains"
        ],
        "exercise": [
            "30 minutes of moderate aerobic activity daily",
            "Regular walking",
            "Swimming",
            "Cycling",
            "Light weight training under supervision"
        ],
        "lifestyle": [
            "Maintain healthy weight",
            "Practice stress management",
            "Get adequate sleep (7-8 hours)",
            "Regular blood pressure monitoring",
            "Limit alcohol consumption"
        ],
        "emergency_signs": [
            "Severe headache",
            "Vision problems",
            "Chest pain",
            "Difficulty breathing",
            "Irregular heartbeat"
        ]
    },
    "Heart Attack": {
        "medicines": [
            {"name": "Aspirin", "dosage": "As directed by doctor", "purpose": "Blood thinner"},
            {"name": "Nitroglycerin", "dosage": "As needed under tongue", "purpose": "Chest pain relief"},
            {"name": "Beta blockers", "dosage": "As prescribed", "purpose": "Heart protection"}
        ],
        "precautions": [
            "Call emergency services immediately",
            "Take prescribed medications",
            "Rest and avoid stress",
            "Monitor vital signs",
            "Regular medical check-ups"
        ],
        "diet": [
            "Low-fat and low-cholesterol diet",
            "Increase fiber intake",
            "Reduce sodium intake",
            "Eat more fruits and vegetables",
            "Avoid trans fats"
        ],
        "exercise": [
            "Cardiac rehabilitation program",
            "Supervised exercise program",
            "Gradual return to activity",
            "Light walking as advised",
            "Breathing exercises"
        ],
        "lifestyle": [
            "Quit smoking",
            "Stress management",
            "Regular health check-ups",
            "Weight management",
            "Adequate rest periods"
        ],
        "emergency_signs": [
            "Severe chest pain",
            "Shortness of breath",
            "Cold sweats",
            "Nausea",
            "Left arm pain"
        ]
    },
    "Malaria": {
        "medicines": [
            {"name": "Artemether-lumefantrine", "dosage": "As prescribed", "purpose": "Anti-malarial"},
            {"name": "Paracetamol", "dosage": "500-1000mg every 6 hours", "purpose": "Fever and pain"},
            {"name": "ORS", "dosage": "As needed", "purpose": "Hydration"}
        ],
        "precautions": [
            "Complete full course of medication",
            "Rest adequately",
            "Stay hydrated",
            "Use mosquito nets",
            "Regular temperature monitoring"
        ],
        "diet": [
            "High fluid intake",
            "Light and easily digestible foods",
            "Fruits rich in Vitamin C",
            "Clear soups and broths",
            "Small, frequent meals"
        ],
        "exercise": [
            "Complete bed rest during fever",
            "Light movements when fever subsides",
            "Gentle stretching during recovery",
            "Short walks when strength returns",
            "Gradual return to normal activity"
        ],
        "lifestyle": [
            "Use mosquito repellents",
            "Wear full-sleeved clothing",
            "Keep surroundings clean",
            "Avoid mosquito-prone areas",
            "Regular follow-up with doctor"
        ],
        "emergency_signs": [
            "Very high fever",
            "Severe headache",
            "Extreme weakness",
            "Confusion",
            "Dark or bloody urine"
        ]
    },
    "Typhoid": {
        "medicines": [
            {"name": "Ciprofloxacin", "dosage": "500mg twice daily", "purpose": "Antibiotic"},
            {"name": "Paracetamol", "dosage": "500-1000mg every 6 hours", "purpose": "Fever"},
            {"name": "ORS", "dosage": "As needed", "purpose": "Hydration"}
        ],
        "precautions": [
            "Complete antibiotic course",
            "Maintain hygiene",
            "Drink boiled water",
            "Avoid solid foods initially",
            "Rest adequately"
        ],
        "diet": [
            "Clear broths and soups",
            "Soft, well-cooked foods",
            "Mashed vegetables",
            "Rice porridge",
            "Fresh fruit juices"
        ],
        "exercise": [
            "Complete bed rest during fever",
            "Light movements as tolerated",
            "Gentle walking during recovery",
            "Avoid strenuous activity",
            "Gradual return to routine"
        ],
        "lifestyle": [
            "Maintain personal hygiene",
            "Use clean drinking water",
            "Proper hand washing",
            "Safe food practices",
            "Regular medical monitoring"
        ],
        "emergency_signs": [
            "Severe abdominal pain",
            "High persistent fever",
            "Extreme weakness",
            "Mental confusion",
            "Severe dehydration"
        ]
    },
    "Jaundice": {
        "medicines": [
            {"name": "Ursodeoxycholic acid", "dosage": "As prescribed", "purpose": "Liver support"},
            {"name": "Vitamin supplements", "dosage": "As directed", "purpose": "Nutritional support"},
            {"name": "Antivirals", "dosage": "If prescribed", "purpose": "For viral cause"}
        ],
        "precautions": [
            "Avoid alcohol completely",
            "Rest adequately",
            "Follow dietary restrictions",
            "Regular liver function tests",
            "Avoid hepatotoxic medicines"
        ],
        "diet": [
            "Low-fat diet",
            "High-fiber foods",
            "Fresh fruits and vegetables",
            "Avoid oily and spicy foods",
            "Plenty of water"
        ],
        "exercise": [
            "Light walking",
            "Gentle stretching",
            "Deep breathing exercises",
            "Yoga under guidance",
            "Avoid strenuous activities"
        ],
        "lifestyle": [
            "Avoid processed foods",
            "No alcohol consumption",
            "Regular sleep schedule",
            "Stress management",
            "Regular medical check-ups"
        ],
        "emergency_signs": [
            "Severe abdominal pain",
            "Mental confusion",
            "Dark urine",
            "Extreme fatigue",
            "Severe itching"
        ]
    },
    "Gastroenteritis": {
        "medicines": [
            {"name": "ORS", "dosage": "As needed", "purpose": "Hydration"},
            {"name": "Probiotics", "dosage": "As directed", "purpose": "Gut health"},
            {"name": "Loperamide", "dosage": "As needed", "purpose": "Diarrhea control"}
        ],
        "precautions": [
            "Stay hydrated",
            "Rest adequately",
            "Avoid solid foods initially",
            "Maintain hygiene",
            "Gradual diet introduction"
        ],
        "diet": [
            "BRAT diet (Bananas, Rice, Applesauce, Toast)",
            "Clear broths",
            "Yogurt with probiotics",
            "Boiled potatoes",
            "Avoid dairy initially"
        ],
        "exercise": [
            "Rest during acute phase",
            "Light walking when improving",
            "Gentle stretching",
            "Avoid strenuous activity",
            "Return to normal activity gradually"
        ],
        "lifestyle": [
            "Proper hand washing",
            "Food hygiene",
            "Clean drinking water",
            "Regular meal times",
            "Adequate rest"
        ],
        "emergency_signs": [
            "Severe dehydration",
            "Bloody stools",
            "High fever",
            "Severe abdominal pain",
            "Inability to keep fluids down"
        ]
    },
    "Pneumonia": {
        "medicines": [
            {"name": "Amoxicillin", "dosage": "500mg three times daily", "purpose": "Bacterial infection treatment"},
            {"name": "Azithromycin", "dosage": "500mg once daily", "purpose": "Alternative antibiotic"},
            {"name": "Paracetamol", "dosage": "500-1000mg every 4-6 hours", "purpose": "Fever and pain relief"},
            {"name": "Cough expectorant", "dosage": "As directed", "purpose": "Loosen mucus"},
            {"name": "Inhaled bronchodilators", "dosage": "As prescribed", "purpose": "Ease breathing"}
        ],
        "precautions": [
            "Complete full course of antibiotics",
            "Get plenty of rest",
            "Stay hydrated",
            "Use a humidifier",
            "Monitor temperature regularly",
            "Avoid smoking and second-hand smoke",
            "Keep head elevated while sleeping"
        ],
        "diet": [
            "Drink plenty of fluids",
            "Eat protein-rich foods",
            "Include vitamin C rich fruits",
            "Have warm soups and broths",
            "Small, frequent meals",
            "Avoid cold drinks and foods",
            "Include garlic and ginger in diet"
        ],
        "exercise": [
            "Deep breathing exercises",
            "Chest physiotherapy if prescribed",
            "Gradual return to activity",
            "Light walking when fever subsides",
            "Avoid strenuous activities"
        ],
        "lifestyle": [
            "Stop smoking",
            "Avoid exposure to cold",
            "Practice deep breathing exercises",
            "Get adequate sleep (8-10 hours)",
            "Maintain good hygiene",
            "Regular follow-up with doctor"
        ],
        "emergency_signs": [
            "Difficulty breathing",
            "Chest pain",
            "High persistent fever",
            "Coughing up blood",
            "Blue lips or face",
            "Mental confusion"
        ]
    },
    "Chicken Pox": {
        "medicines": [
            {"name": "Acyclovir", "dosage": "As prescribed", "purpose": "Antiviral medication"},
            {"name": "Calamine lotion", "dosage": "Apply as needed", "purpose": "Relieve itching"},
            {"name": "Paracetamol", "dosage": "500-1000mg every 6 hours", "purpose": "Fever and pain relief"},
            {"name": "Antihistamine", "dosage": "As directed", "purpose": "Reduce itching"}
        ],
        "precautions": [
            "Isolate from others until blisters crust over",
            "Avoid scratching blisters",
            "Keep skin clean and dry",
            "Wear loose, cotton clothing",
            "Trim fingernails to prevent skin damage",
            "Stay home until recovery"
        ],
        "diet": [
            "Soft, cool foods",
            "High protein foods for healing",
            "Vitamin C rich fruits",
            "Cold soups and smoothies",
            "Plenty of fluids",
            "Avoid salty and spicy foods"
        ],
        "exercise": [
            "Rest during fever phase",
            "Light activities when comfortable",
            "Gentle stretching",
            "Short walks when recovering",
            "Avoid sweating excessively"
        ],
        "lifestyle": [
            "Keep cool environment",
            "Use soft cotton bedding",
            "Regular oatmeal baths",
            "Maintain good hygiene",
            "Avoid public places",
            "Get adequate rest"
        ],
        "emergency_signs": [
            "High fever above 102°F (39°C)",
            "Severe headache",
            "Difficulty breathing",
            "Confusion or drowsiness",
            "Severe skin infection",
            "Blisters near eyes"
        ]
    },
    "Dengue": {
        "medicines": [
            {"name": "Paracetamol", "dosage": "500-1000mg every 6 hours", "purpose": "Fever and pain relief"},
            {"name": "ORS", "dosage": "As needed", "purpose": "Prevent dehydration"}
        ],
        "precautions": [
            "Monitor platelet count regularly",
            "Watch for warning signs",
            "Prevent mosquito bites",
            "Stay hydrated",
            "Get adequate rest"
        ],
        "diet": [
            "Drink plenty of fluids",
            "Consume papaya leaf juice",
            "Eat light, easily digestible foods",
            "Include foods rich in vitamin C",
            "Avoid spicy and oily foods"
        ],
        "lifestyle": [
            "Use mosquito nets",
            "Wear full-sleeve clothes",
            "Remove stagnant water sources",
            "Use mosquito repellents",
            "Keep surroundings clean"
        ]
    },
    "Tuberculosis": {
        "medicines": [
            {"name": "Isoniazid", "dosage": "As prescribed", "purpose": "Primary TB treatment"},
            {"name": "Rifampicin", "dosage": "As prescribed", "purpose": "Primary TB treatment"},
            {"name": "Pyrazinamide", "dosage": "As prescribed", "purpose": "Primary TB treatment"},
            {"name": "Ethambutol", "dosage": "As prescribed", "purpose": "Primary TB treatment"}
        ],
        "precautions": [
            "Complete full course of medication",
            "Wear mask when in public",
            "Cover mouth while coughing",
            "Maintain good ventilation",
            "Regular follow-up with doctor"
        ],
        "diet": [
            "High protein diet",
            "Vitamin-rich foods",
            "Adequate calorie intake",
            "Include dairy products",
            "Avoid alcohol"
        ],
        "lifestyle": [
            "Stop smoking",
            "Get adequate rest",
            "Isolate during initial phase",
            "Regular exercise after recovery",
            "Maintain good hygiene"
        ]
    },
    "Anemia": {
        "medicines": [
            {"name": "Iron supplements", "dosage": "As prescribed", "purpose": "Iron deficiency treatment"},
            {"name": "Folic acid", "dosage": "400mcg daily", "purpose": "Blood cell production"},
            {"name": "Vitamin B12", "dosage": "As prescribed", "purpose": "Blood cell production"}
        ],
        "precautions": [
            "Regular blood tests",
            "Take supplements with food",
            "Avoid tea/coffee with meals",
            "Monitor symptoms",
            "Report unusual symptoms"
        ],
        "diet": [
            "Iron-rich foods (leafy greens, meat)",
            "Vitamin C rich fruits",
            "Whole grains",
            "Lean proteins",
            "Avoid caffeine with meals"
        ],
        "lifestyle": [
            "Regular moderate exercise",
            "Adequate sleep",
            "Stress management",
            "Regular medical check-ups",
            "Avoid overexertion"
        ]
    },
    "Bronchitis": {
        "medicines": [
            {"name": "Amoxicillin", "dosage": "500mg three times daily", "purpose": "If bacterial infection"},
            {"name": "Guaifenesin", "dosage": "As directed", "purpose": "Mucus thinning"},
            {"name": "Salbutamol inhaler", "dosage": "As needed", "purpose": "Breathing relief"}
        ],
        "precautions": [
            "Avoid smoking",
            "Stay away from irritants",
            "Use humidifier",
            "Rest adequately",
            "Stay hydrated"
        ],
        "diet": [
            "Warm liquids",
            "Honey and ginger tea",
            "Vitamin C rich foods",
            "Avoid dairy temporarily",
            "Light, nutritious meals"
        ],
        "lifestyle": [
            "Stop smoking",
            "Avoid air pollution",
            "Practice breathing exercises",
            "Regular steam inhalation",
            "Keep surroundings clean"
        ]
    },
    "Sinusitis": {
        "medicines": [
            {"name": "Amoxicillin", "dosage": "500mg three times daily", "purpose": "If bacterial infection"},
            {"name": "Nasal decongestant", "dosage": "As directed", "purpose": "Relieve congestion"},
            {"name": "Saline nasal spray", "dosage": "As needed", "purpose": "Nasal irrigation"}
        ],
        "precautions": [
            "Avoid allergens",
            "Use humidifier",
            "Regular nasal irrigation",
            "Keep head elevated while sleeping",
            "Avoid sudden temperature changes"
        ],
        "diet": [
            "Spicy foods (natural decongestant)",
            "Vitamin C rich foods",
            "Warm liquids",
            "Avoid dairy products",
            "Stay hydrated"
        ],
        "lifestyle": [
            "Regular steam inhalation",
            "Nasal exercises",
            "Avoid smoking",
            "Keep surroundings clean",
            "Manage allergies"
        ]
    },
    "Hepatitis": {
        "medicines": [
            {"name": "Antiviral medications", "dosage": "As prescribed", "purpose": "Viral treatment"},
            {"name": "Ursodeoxycholic acid", "dosage": "As prescribed", "purpose": "Liver function support"},
            {"name": "Vitamin supplements", "dosage": "As directed", "purpose": "Nutritional support"}
        ],
        "precautions": [
            "Avoid alcohol completely",
            "No over-the-counter medications",
            "Regular liver function tests",
            "Avoid fatty foods",
            "Practice safe sex"
        ],
        "diet": [
            "Low-fat diet",
            "High-fiber foods",
            "Avoid processed foods",
            "Limited salt intake",
            "Plenty of fruits and vegetables"
        ],
        "lifestyle": [
            "Complete rest during acute phase",
            "Avoid alcohol",
            "Practice good hygiene",
            "Regular medical check-ups",
            "Stress management"
        ]
    },
    "Common Cold": {
        "medicines": [
            {"name": "Paracetamol", "dosage": "500-1000mg every 6 hours", "purpose": "Fever and pain relief"},
            {"name": "Antihistamine", "dosage": "As directed", "purpose": "Runny nose"},
            {"name": "Throat lozenges", "dosage": "As needed", "purpose": "Sore throat relief"}
        ],
        "precautions": [
            "Rest adequately",
            "Stay hydrated",
            "Cover mouth when coughing",
            "Use disposable tissues",
            "Avoid close contact with others"
        ],
        "diet": [
            "Hot soups and broths",
            "Warm herbal teas",
            "Vitamin C rich fruits",
            "Honey and lemon drinks",
            "Light, easily digestible foods"
        ],
        "exercise": [
            "Rest during acute symptoms",
            "Light walking when feeling better",
            "Gentle stretching",
            "Deep breathing exercises",
            "Gradual return to normal activity"
        ],
        "lifestyle": [
            "Get adequate sleep",
            "Use humidifier",
            "Practice good hygiene",
            "Avoid cold exposure",
            "Stay warm"
        ]
    },
    "Gastritis": {
        "medicines": [
            {"name": "Omeprazole", "dosage": "20mg once daily", "purpose": "Reduce acid production"},
            {"name": "Antacids", "dosage": "As needed", "purpose": "Quick acid relief"},
            {"name": "Sucralfate", "dosage": "As directed", "purpose": "Stomach coating"}
        ],
        "precautions": [
            "Avoid spicy foods",
            "Eat smaller meals",
            "Don't lie down after eating",
            "Avoid alcohol",
            "Stop smoking"
        ],
        "diet": [
            "Bland foods",
            "Low-fat foods",
            "Yogurt and probiotics",
            "Bananas and rice",
            "Avoid caffeine"
        ],
        "exercise": [
            "Light walking after meals",
            "Gentle yoga",
            "Avoid strenuous exercise",
            "Light stretching",
            "Regular but moderate activity"
        ],
        "lifestyle": [
            "Eat at regular times",
            "Manage stress",
            "Avoid late night eating",
            "Stay upright after meals",
            "Regular meal schedule"
        ]
    },
    "Migraine": {
        "medicines": [
            {"name": "Sumatriptan", "dosage": "As prescribed", "purpose": "Acute migraine relief"},
            {"name": "Ibuprofen", "dosage": "400mg as needed", "purpose": "Pain relief"},
            {"name": "Anti-nausea medication", "dosage": "As prescribed", "purpose": "Nausea relief"}
        ],
        "precautions": [
            "Identify and avoid triggers",
            "Stay in a quiet, dark room",
            "Get regular sleep",
            "Avoid bright lights",
            "Manage stress"
        ],
        "diet": [
            "Regular meals",
            "Stay hydrated",
            "Avoid trigger foods",
            "Limit caffeine",
            "Avoid alcohol"
        ],
        "exercise": [
            "Regular moderate exercise",
            "Gentle yoga",
            "Walking in fresh air",
            "Stretching exercises",
            "Avoid high-intensity during attacks"
        ],
        "lifestyle": [
            "Regular sleep schedule",
            "Stress management",
            "Keep a migraine diary",
            "Regular breaks from screens",
            "Good posture maintenance"
        ]
    },
    "Asthma": {
        "medicines": [
            {"name": "Salbutamol inhaler", "dosage": "As needed", "purpose": "Quick relief"},
            {"name": "Corticosteroid inhaler", "dosage": "As prescribed", "purpose": "Long-term control"},
            {"name": "Montelukast", "dosage": "As prescribed", "purpose": "Prevention"}
        ],
        "precautions": [
            "Avoid triggers",
            "Keep rescue inhaler handy",
            "Monitor peak flow",
            "Regular check-ups",
            "Follow action plan"
        ],
        "diet": [
            "Anti-inflammatory foods",
            "Vitamin D rich foods",
            "Omega-3 rich foods",
            "Fresh fruits and vegetables",
            "Stay hydrated"
        ],
        "exercise": [
            "Warm up properly",
            "Swimming",
            "Walking",
            "Gentle yoga",
            "Breathing exercises"
        ],
        "lifestyle": [
            "Keep environment clean",
            "Use air purifier",
            "Avoid smoke exposure",
            "Regular medication",
            "Stress management"
        ]
    },
    "Arthritis": {
        "medicines": [
            {"name": "NSAIDs", "dosage": "As prescribed", "purpose": "Pain and inflammation"},
            {"name": "Paracetamol", "dosage": "500-1000mg as needed", "purpose": "Pain relief"},
            {"name": "Joint supplements", "dosage": "As directed", "purpose": "Joint health"}
        ],
        "precautions": [
            "Protect joints",
            "Use assistive devices",
            "Avoid overexertion",
            "Regular exercise",
            "Maintain healthy weight"
        ],
        "diet": [
            "Anti-inflammatory foods",
            "Omega-3 rich foods",
            "Calcium rich foods",
            "Vitamin D sources",
            "Avoid processed foods"
        ],
        "exercise": [
            "Low-impact exercises",
            "Swimming",
            "Gentle stretching",
            "Range of motion exercises",
            "Water aerobics"
        ],
        "lifestyle": [
            "Joint protection",
            "Regular movement",
            "Good posture",
            "Stress management",
            "Adequate rest"
        ]
    },
    "Diabetes": {
        "medicines": [
            {"name": "Metformin", "dosage": "As prescribed", "purpose": "Blood sugar control"},
            {"name": "Insulin", "dosage": "As prescribed", "purpose": "Blood sugar control"},
            {"name": "Blood sugar testing supplies", "dosage": "Regular use", "purpose": "Monitoring"}
        ],
        "precautions": [
            "Regular blood sugar monitoring",
            "Foot care",
            "Regular check-ups",
            "Carry glucose source",
            "Medical ID bracelet"
        ],
        "diet": [
            "Low glycemic foods",
            "Controlled portions",
            "Regular meal times",
            "Fiber-rich foods",
            "Limited sugars"
        ],
        "exercise": [
            "Regular walking",
            "Swimming",
            "Resistance training",
            "Aerobic exercises",
            "Monitor sugar during exercise"
        ],
        "lifestyle": [
            "Regular monitoring",
            "Stress management",
            "Good sleep habits",
            "Regular medical check-ups",
            "Foot care routine"
        ]
    },
    "Fever": {
        "medicines": [
            {"name": "Paracetamol", "dosage": "500-1000mg every 6 hours", "purpose": "Fever reduction"},
            {"name": "Ibuprofen", "dosage": "400mg as needed", "purpose": "Pain and fever"},
            {"name": "ORS", "dosage": "As needed", "purpose": "Hydration"}
        ],
        "precautions": [
            "Rest adequately",
            "Stay hydrated",
            "Monitor temperature",
            "Wear light clothing",
            "Keep room well-ventilated"
        ],
        "diet": [
            "Light and easily digestible foods",
            "Clear soups and broths",
            "Fresh fruit juices",
            "Plenty of fluids",
            "Avoid heavy meals"
        ],
        "exercise": [
            "Complete rest during high fever",
            "Light movements when fever reduces",
            "Gentle stretching",
            "Short walks when recovering",
            "Gradual return to activity"
        ],
        "lifestyle": [
            "Get adequate sleep",
            "Stay in cool environment",
            "Regular temperature checks",
            "Avoid overexertion",
            "Keep surroundings clean"
        ]
    },
    "Allergies": {
        "medicines": [
            {"name": "Antihistamines", "dosage": "As directed", "purpose": "Allergy relief"},
            {"name": "Nasal spray", "dosage": "As prescribed", "purpose": "Nasal congestion"},
            {"name": "Eye drops", "dosage": "As needed", "purpose": "Eye irritation"}
        ],
        "precautions": [
            "Avoid known triggers",
            "Keep windows closed during high pollen",
            "Use air purifiers",
            "Regular cleaning",
            "Monitor air quality"
        ],
        "diet": [
            "Anti-inflammatory foods",
            "Local honey",
            "Vitamin C rich foods",
            "Avoid trigger foods",
            "Stay hydrated"
        ],
        "exercise": [
            "Indoor exercises during high pollen",
            "Regular walking",
            "Swimming in indoor pools",
            "Yoga and stretching",
            "Light aerobic activities"
        ],
        "lifestyle": [
            "Regular cleaning",
            "Use HEPA filters",
            "Shower before bed",
            "Change clothes after outdoors",
            "Track allergy levels"
        ]
    },
    "Food Poisoning": {
        "medicines": [
            {"name": "ORS", "dosage": "As needed", "purpose": "Hydration"},
            {"name": "Probiotics", "dosage": "As directed", "purpose": "Gut health"},
            {"name": "Anti-emetics", "dosage": "As prescribed", "purpose": "Nausea relief"}
        ],
        "precautions": [
            "Stay hydrated",
            "Rest adequately",
            "Monitor symptoms",
            "Avoid solid foods initially",
            "Maintain hygiene"
        ],
        "diet": [
            "Clear fluids",
            "BRAT diet (Bananas, Rice, Applesauce, Toast)",
            "Electrolyte solutions",
            "Light broths",
            "Avoid dairy and spicy foods"
        ],
        "exercise": [
            "Complete rest initially",
            "Light walking when improving",
            "Gentle movements",
            "Avoid strenuous activity",
            "Gradual return to normal"
        ],
        "lifestyle": [
            "Food safety practices",
            "Hand hygiene",
            "Clean cooking surfaces",
            "Proper food storage",
            "Regular hand washing"
        ]
    },
    "Chicken Pox": {
        "medicines": [
            {"name": "Calamine lotion", "dosage": "Apply to affected areas as needed", "purpose": "Relieve itching"},
            {"name": "Paracetamol", "dosage": "500-1000mg every 6 hours", "purpose": "Reduce fever and pain"},
            {"name": "Antihistamines", "dosage": "As directed", "purpose": "Reduce itching and help sleep"},
            {"name": "Acyclovir", "dosage": "As prescribed", "purpose": "Antiviral (for severe cases)"}
        ],
        "precautions": [
            "Isolate until all blisters have crusted over",
            "Avoid scratching to prevent scarring",
            "Keep skin clean and dry",
            "Use calamine lotion for itch relief",
            "Take lukewarm baths with baking soda or colloidal oatmeal",
            "Wear loose-fitting, cotton clothing"
        ],
        "diet": [
            "Soft, bland foods that are easy to eat",
            "Cold foods like smoothies and popsicles to soothe throat",
            "Plenty of fluids to prevent dehydration",
            "Foods rich in vitamin C to boost immune system",
            "Avoid spicy or acidic foods that may irritate blisters in mouth"
        ],
        "exercise": [
            "Rest during the illness",
            "Light activities when feeling better",
            "Avoid strenuous exercise until recovery",
            "Gentle stretching during recovery phase",
            "Return to normal activity gradually after all blisters crust over"
        ],
        "lifestyle": [
            "Maintain good hygiene",
            "Keep fingernails short to minimize damage from scratching",
            "Use separate towels and bedding",
            "Avoid contact with pregnant women and immunocompromised people",
            "Monitor for signs of secondary infection"
        ]
    },
    "Depression": {
        "medicines": [
            {"name": "Consult doctor", "dosage": "As prescribed", "purpose": "Proper treatment"},
            {"name": "Antidepressants", "dosage": "As prescribed by psychiatrist", "purpose": "Mood regulation"},
            {"name": "Supplements", "dosage": "As advised by doctor", "purpose": "Support treatment"}
        ],
        "precautions": [
            "Follow treatment plan consistently",
            "Attend all therapy sessions",
            "Monitor mood changes",
            "Avoid alcohol and drugs",
            "Reach out during crisis"
        ],
        "diet": [
            "Omega-3 rich foods (fatty fish, flaxseed)",
            "Foods rich in B vitamins (whole grains, leafy greens)",
            "Foods with tryptophan (turkey, eggs, cheese)",
            "Anti-inflammatory foods (berries, turmeric)",
            "Regular meal pattern to stabilize mood"
        ],
        "exercise": [
            "30 minutes of moderate activity daily",
            "Mindful walking in nature",
            "Yoga and stretching",
            "Group exercise classes",
            "Dance or other enjoyable movement"
        ],
        "lifestyle": [
            "Establish regular sleep schedule",
            "Practice mindfulness or meditation",
            "Maintain social connections",
            "Engage in enjoyable activities",
            "Set small, achievable daily goals"
        ]
    }
}

DEFAULT_RECOMMENDATIONS = {
    "exercise": [
        "Light walking as tolerated",
        "Gentle stretching exercises",
        "Deep breathing exercises",
        "Rest when tired",
        "Gradual return to normal activity"
    ]
}

def get_recommendations(disease, age_group=None):
    """Get recommendations for a disease with age-appropriate modifications."""
    if disease not in DISEASE_RECOMMENDATIONS:
        return None
        
    recommendations = DISEASE_RECOMMENDATIONS[disease].copy()
    
    # Add default exercise recommendations if not present
    if "exercise" not in recommendations:
        recommendations["exercise"] = DEFAULT_RECOMMENDATIONS["exercise"].copy()
    
    # Adjust dosages based on age group
    if age_group == "CHILD":
        for med in recommendations.get("medicines", []):
            med["dosage"] = "Consult pediatrician for dosage"
            
        # Modify exercise recommendations for children
            recommendations["exercise"] = [ex + " (under supervision)" for ex in recommendations["exercise"]]
            
    elif age_group == "ELDERLY":
        for med in recommendations.get("medicines", []):
            if "mg" in med["dosage"]:
                med["dosage"] = "Consult doctor for adjusted dosage"
                
        # Modify exercise recommendations for elderly
            recommendations["exercise"] = ["Light " + ex.lower() for ex in recommendations["exercise"]]
    
    return recommendations 