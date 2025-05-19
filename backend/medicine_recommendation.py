class MedicineRecommender:
    def __init__(self):
        self.recommendations = {
            'Common Cold': [
                {'medicine': 'Paracetamol', 'dosage': '500-1000mg every 4-6 hours', 'purpose': 'Fever and pain relief', 'contraindications': 'Liver disease', 'side_effects': 'Rare liver problems in high doses'},
                {'medicine': 'Chlorpheniramine', 'dosage': '4mg every 4-6 hours', 'purpose': 'Runny nose and sneezing', 'contraindications': 'Glaucoma, prostate problems', 'side_effects': 'Drowsiness'},
                {'medicine': 'Guaifenesin', 'dosage': '200-400mg every 4 hours', 'purpose': 'Cough and congestion', 'contraindications': 'None significant', 'side_effects': 'Mild nausea'}
            ],
            'Flu': [
                {'medicine': 'Oseltamivir', 'dosage': 'As prescribed', 'purpose': 'Antiviral medication'},
                {'medicine': 'Ibuprofen', 'dosage': '400mg every 6-8 hours', 'purpose': 'Fever and pain relief'},
                {'medicine': 'Decongestant', 'dosage': 'As directed', 'purpose': 'Nasal congestion'}
            ],
            'Migraine': [
                {'medicine': 'Sumatriptan', 'dosage': '50-100mg as needed', 'purpose': 'Acute migraine relief', 'contraindications': 'Heart disease', 'side_effects': 'Chest tightness, fatigue'},
                {'medicine': 'Rizatriptan', 'dosage': '5-10mg as needed', 'purpose': 'Migraine treatment', 'contraindications': 'Hypertension', 'side_effects': 'Dizziness, drowsiness'},
                {'medicine': 'Propranolol', 'dosage': '40-80mg daily', 'purpose': 'Prevention', 'contraindications': 'Asthma', 'side_effects': 'Fatigue, cold hands'}
            ],
            'COVID-19': [
                {'medicine': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever and pain relief'},
                {'medicine': 'Vitamin C', 'dosage': '500mg twice daily', 'purpose': 'Immune support'},
                {'medicine': 'Zinc', 'dosage': '50mg daily', 'purpose': 'Immune support'}
            ],
            'Bronchitis': [
                {'medicine': 'Dextromethorphan', 'dosage': '15-30mg every 6-8 hours', 'purpose': 'Cough suppression'},
                {'medicine': 'Guaifenesin', 'dosage': '200-400mg every 4 hours', 'purpose': 'Expectorant'},
                {'medicine': 'Salbutamol inhaler', 'dosage': '2 puffs every 4-6 hours', 'purpose': 'Breathing relief'}
            ],
            'Gastritis': [
                {'medicine': 'Omeprazole', 'dosage': '20mg once daily', 'purpose': 'Reduce acid production'},
                {'medicine': 'Antacid', 'dosage': 'As needed', 'purpose': 'Immediate acid relief'},
                {'medicine': 'Sucralfate', 'dosage': '1g four times daily', 'purpose': 'Stomach lining protection'}
            ],
            'Sinusitis': [
                {'medicine': 'Pseudoephedrine', 'dosage': '60mg every 4-6 hours', 'purpose': 'Nasal decongestant'},
                {'medicine': 'Amoxicillin', 'dosage': '500mg three times daily', 'purpose': 'Bacterial infection'},
                {'medicine': 'Saline nasal spray', 'dosage': 'As needed', 'purpose': 'Nasal congestion relief'}
            ],
            'Pneumonia': [
                {'medicine': 'Azithromycin', 'dosage': 'As prescribed', 'purpose': 'Bacterial infection'},
                {'medicine': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever relief'},
                {'medicine': 'Guaifenesin', 'dosage': '200-400mg every 4 hours', 'purpose': 'Expectorant'}
            ],
            'Asthma': [
                {'medicine': 'Salbutamol inhaler', 'dosage': '2 puffs every 4-6 hours when needed', 'purpose': 'Quick relief', 'contraindications': 'Heart problems', 'side_effects': 'Tremors, fast heartbeat'},
                {'medicine': 'Budesonide inhaler', 'dosage': '1-2 puffs twice daily', 'purpose': 'Prevention', 'contraindications': 'Active TB', 'side_effects': 'Throat irritation'},
                {'medicine': 'Montelukast', 'dosage': '10mg once daily', 'purpose': 'Prevention', 'contraindications': 'Liver disease', 'side_effects': 'Mood changes'},
                {'medicine': 'Ipratropium inhaler', 'dosage': '2 puffs 4 times daily', 'purpose': 'Bronchodilation', 'contraindications': 'Glaucoma', 'side_effects': 'Dry mouth'},
                {'medicine': 'Prednisolone', 'dosage': '40-60mg daily for flares', 'purpose': 'Severe attacks', 'contraindications': 'Active infection', 'side_effects': 'Weight gain'}
            ],
            'Acute Sinusitis': [
                {'medicine': 'Amoxicillin', 'dosage': '500mg three times daily', 'purpose': 'Bacterial infection', 'contraindications': 'Penicillin allergy', 'side_effects': 'Diarrhea'},
                {'medicine': 'Pseudoephedrine', 'dosage': '60mg every 4-6 hours', 'purpose': 'Decongestant', 'contraindications': 'High blood pressure', 'side_effects': 'Insomnia'},
                {'medicine': 'Fluticasone nasal', 'dosage': '1-2 sprays each nostril daily', 'purpose': 'Inflammation', 'contraindications': 'Recent nasal surgery', 'side_effects': 'Nosebleeds'},
                {'medicine': 'Saline nasal spray', 'dosage': 'Use as needed', 'purpose': 'Congestion relief', 'contraindications': 'None', 'side_effects': 'None significant'}
            ],
            'Chronic Sinusitis': [
                {'medicine': 'Mometasone nasal', 'dosage': '2 sprays each nostril daily', 'purpose': 'Long-term control', 'contraindications': 'Nasal perforation', 'side_effects': 'Nose irritation'},
                {'medicine': 'Doxycycline', 'dosage': '100mg twice daily', 'purpose': 'Infection', 'contraindications': 'Pregnancy', 'side_effects': 'Sun sensitivity'},
                {'medicine': 'Montelukast', 'dosage': '10mg daily', 'purpose': 'Inflammation', 'contraindications': 'Liver disease', 'side_effects': 'Headache'},
                {'medicine': 'Mupirocin nasal', 'dosage': 'Apply twice daily', 'purpose': 'Bacterial colonization', 'contraindications': 'None significant', 'side_effects': 'Local irritation'}
            ],
            'Bronchial Asthma': [
                {'medicine': 'Formoterol inhaler', 'dosage': '12mcg twice daily', 'purpose': 'Long-acting relief', 'contraindications': 'Severe heart disease', 'side_effects': 'Muscle cramps'},
                {'medicine': 'Fluticasone/Salmeterol inhaler', 'dosage': '1 puff twice daily', 'purpose': 'Maintenance', 'contraindications': 'TB', 'side_effects': 'Throat irritation'},
                {'medicine': 'Tiotropium inhaler', 'dosage': '18mcg once daily', 'purpose': 'Long-term control', 'contraindications': 'Glaucoma', 'side_effects': 'Dry mouth'},
                {'medicine': 'Theophylline', 'dosage': '200-400mg twice daily', 'purpose': 'Bronchodilation', 'contraindications': 'Heart arrhythmias', 'side_effects': 'Nausea'}
            ],
            'Exercise-Induced Asthma': [
                {'medicine': 'Salbutamol inhaler', 'dosage': '2 puffs 15-30 min before exercise', 'purpose': 'Prevention', 'contraindications': 'Heart problems', 'side_effects': 'Tremors'},
                {'medicine': 'Montelukast', 'dosage': '10mg 2 hours before exercise', 'purpose': 'Prevention', 'contraindications': 'Liver disease', 'side_effects': 'Headache'},
                {'medicine': 'Cromolyn inhaler', 'dosage': '2 puffs before exercise', 'purpose': 'Prevention', 'contraindications': 'None significant', 'side_effects': 'Cough'}
            ],
            'Allergic Bronchitis': [
                {'medicine': 'Dextromethorphan', 'dosage': '15-30mg every 6-8 hours', 'purpose': 'Cough relief', 'contraindications': 'MAO inhibitors', 'side_effects': 'Drowsiness'},
                {'medicine': 'Montelukast', 'dosage': '10mg daily', 'purpose': 'Inflammation', 'contraindications': 'Liver disease', 'side_effects': 'Headache'},
                {'medicine': 'Budesonide inhaler', 'dosage': '1-2 puffs twice daily', 'purpose': 'Inflammation', 'contraindications': 'Active infection', 'side_effects': 'Throat irritation'}
            ],
            'Chronic Bronchitis': [
                {'medicine': 'Tiotropium inhaler', 'dosage': '18mcg once daily', 'purpose': 'Bronchodilation', 'contraindications': 'Glaucoma', 'side_effects': 'Dry mouth'},
                {'medicine': 'N-acetylcysteine', 'dosage': '600mg twice daily', 'purpose': 'Mucus thinning', 'contraindications': 'Asthma', 'side_effects': 'Nausea'},
                {'medicine': 'Roflumilast', 'dosage': '500mcg daily', 'purpose': 'Inflammation', 'contraindications': 'Liver disease', 'side_effects': 'Weight loss'},
                {'medicine': 'Azithromycin', 'dosage': '250mg three times weekly', 'purpose': 'Prevention', 'contraindications': 'Heart rhythm problems', 'side_effects': 'Hearing changes'}
            ],
            'Hypertension': [
                {'medicine': 'Amlodipine', 'dosage': '5-10mg once daily', 'purpose': 'Blood pressure control', 'contraindications': 'Severe hypotension', 'side_effects': 'Ankle swelling, headache'},
                {'medicine': 'Lisinopril', 'dosage': '10-20mg once daily', 'purpose': 'ACE inhibitor', 'contraindications': 'Pregnancy, angioedema', 'side_effects': 'Dry cough, dizziness'},
                {'medicine': 'Hydrochlorothiazide', 'dosage': '12.5-25mg once daily', 'purpose': 'Diuretic', 'contraindications': 'Gout', 'side_effects': 'Frequent urination, electrolyte imbalance'}
            ],
            'Diabetes Type 2': [
                {'medicine': 'Metformin', 'dosage': '500-1000mg twice daily', 'purpose': 'Blood sugar control', 'contraindications': 'Kidney disease', 'side_effects': 'Nausea, diarrhea'},
                {'medicine': 'Glimepiride', 'dosage': '1-4mg once daily', 'purpose': 'Increase insulin production', 'contraindications': 'Type 1 diabetes', 'side_effects': 'Low blood sugar'},
                {'medicine': 'Sitagliptin', 'dosage': '100mg once daily', 'purpose': 'DPP-4 inhibitor', 'contraindications': 'Pancreatitis', 'side_effects': 'Joint pain, upper respiratory infection'}
            ],
            'Arthritis': [
                {'medicine': 'Naproxen', 'dosage': '250-500mg twice daily', 'purpose': 'Pain and inflammation', 'contraindications': 'Stomach ulcers', 'side_effects': 'Stomach upset, heartburn'},
                {'medicine': 'Meloxicam', 'dosage': '7.5-15mg once daily', 'purpose': 'Joint pain relief', 'contraindications': 'Bleeding disorders', 'side_effects': 'Stomach pain, dizziness'},
                {'medicine': 'Glucosamine', 'dosage': '1500mg once daily', 'purpose': 'Joint health support', 'contraindications': 'Shellfish allergy', 'side_effects': 'Mild stomach upset'}
            ],
            'Depression': [
                {'medicine': 'Sertraline', 'dosage': '50-100mg once daily', 'purpose': 'Antidepressant', 'contraindications': 'MAO inhibitors', 'side_effects': 'Nausea, sleep changes'},
                {'medicine': 'Escitalopram', 'dosage': '10-20mg once daily', 'purpose': 'Mood stabilizer', 'contraindications': 'Bipolar disorder', 'side_effects': 'Headache, insomnia'},
                {'medicine': 'Bupropion', 'dosage': '150-300mg daily', 'purpose': 'Depression treatment', 'contraindications': 'Seizure disorders', 'side_effects': 'Dry mouth, weight loss'}
            ],
            'Anxiety': [
                {'medicine': 'Alprazolam', 'dosage': '0.25-0.5mg as needed', 'purpose': 'Acute anxiety relief', 'contraindications': 'Alcohol use', 'side_effects': 'Drowsiness, coordination problems'},
            ],
            'Osteoporosis': [
                {'medicine': 'Alendronate', 'dosage': '70mg once weekly', 'purpose': 'Bone strengthening', 'contraindications': 'Esophageal problems', 'side_effects': 'Heartburn, joint pain'},
                {'medicine': 'Calcium + Vitamin D', 'dosage': '1000mg/800IU daily', 'purpose': 'Bone health support', 'contraindications': 'Kidney stones', 'side_effects': 'Constipation'},
                {'medicine': 'Zoledronic acid', 'dosage': '5mg yearly IV', 'purpose': 'Bone density improvement', 'contraindications': 'Kidney disease', 'side_effects': 'Flu-like symptoms'}
            ],
            'Hypothyroidism': [
                {'medicine': 'Levothyroxine', 'dosage': '25-200mcg daily', 'purpose': 'Thyroid hormone replacement', 'contraindications': 'Heart arrhythmia', 'side_effects': 'Weight changes, anxiety'},
                {'medicine': 'Liothyronine', 'dosage': '5-25mcg daily', 'purpose': 'T3 supplementation', 'contraindications': 'Heart disease', 'side_effects': 'Palpitations, insomnia'},
                {'medicine': 'Selenium', 'dosage': '200mcg daily', 'purpose': 'Thyroid support', 'contraindications': 'None significant', 'side_effects': 'Rare at normal doses'}
            ],
            'Psoriasis': [
                {'medicine': 'Methotrexate', 'dosage': '7.5-25mg weekly', 'purpose': 'Reduce inflammation', 'contraindications': 'Liver disease', 'side_effects': 'Nausea, fatigue'},
                {'medicine': 'Adalimumab', 'dosage': '40mg every 2 weeks', 'purpose': 'Immune modulation', 'contraindications': 'Active infection', 'side_effects': 'Injection site reactions'},
                {'medicine': 'Calcipotriene', 'dosage': 'Apply twice daily', 'purpose': 'Skin treatment', 'contraindications': 'Hypercalcemia', 'side_effects': 'Skin irritation'}
            ],
            'Fibromyalgia': [
                {'medicine': 'Duloxetine', 'dosage': '30-60mg daily', 'purpose': 'Pain management', 'contraindications': 'Liver disease', 'side_effects': 'Nausea, dry mouth'},
                {'medicine': 'Pregabalin', 'dosage': '150-450mg daily', 'purpose': 'Pain relief', 'contraindications': 'Kidney disease', 'side_effects': 'Dizziness, weight gain'},
                {'medicine': 'Amitriptyline', 'dosage': '10-50mg at bedtime', 'purpose': 'Sleep improvement', 'contraindications': 'Heart problems', 'side_effects': 'Morning drowsiness'}
            ],
            'Rheumatoid Arthritis': [
                {'medicine': 'Methotrexate', 'dosage': '7.5-20mg weekly', 'purpose': 'Disease-modifying drug', 'contraindications': 'Pregnancy, liver disease', 'side_effects': 'Nausea, fatigue'},
                {'medicine': 'Prednisone', 'dosage': '5-10mg daily', 'purpose': 'Reduce inflammation', 'contraindications': 'Active infections', 'side_effects': 'Weight gain, mood changes'},
                {'medicine': 'Hydroxychloroquine', 'dosage': '200-400mg daily', 'purpose': 'Joint protection', 'contraindications': 'Eye problems', 'side_effects': 'Vision changes, rash'}
            ],
            'Multiple Sclerosis': [
                {'medicine': 'Interferon beta-1a', 'dosage': 'As prescribed', 'purpose': 'Reduce relapses', 'contraindications': 'Liver disease', 'side_effects': 'Flu-like symptoms'},
                {'medicine': 'Dimethyl fumarate', 'dosage': '240mg twice daily', 'purpose': 'Disease modification', 'contraindications': 'Active infection', 'side_effects': 'Flushing, stomach upset'},
                {'medicine': 'Baclofen', 'dosage': '10-20mg 3 times daily', 'purpose': 'Muscle spasticity', 'contraindications': 'Seizure disorders', 'side_effects': 'Drowsiness, weakness'}
            ],
            'Parkinsons Disease': [
                {'medicine': 'Levodopa/Carbidopa', 'dosage': '25/100mg 3-4 times daily', 'purpose': 'Motor symptoms', 'contraindications': 'Glaucoma', 'side_effects': 'Nausea, dyskinesia'},
                {'medicine': 'Ropinirole', 'dosage': '0.25-4mg 3 times daily', 'purpose': 'Dopamine agonist', 'contraindications': 'Heart disease', 'side_effects': 'Sleep attacks, compulsive behavior'},
                {'medicine': 'Amantadine', 'dosage': '100mg twice daily', 'purpose': 'Early symptoms', 'contraindications': 'Kidney disease', 'side_effects': 'Ankle swelling, skin mottling'}
            ],
            'Epilepsy': [
                {'medicine': 'Levetiracetam', 'dosage': '500-1500mg twice daily', 'purpose': 'Seizure control', 'contraindications': 'Kidney disease', 'side_effects': 'Irritability, dizziness'},
                {'medicine': 'Lamotrigine', 'dosage': '25-200mg twice daily', 'purpose': 'Seizure prevention', 'contraindications': 'Heart conduction problems', 'side_effects': 'Rash, double vision'},
                {'medicine': 'Valproate', 'dosage': '500-1000mg twice daily', 'purpose': 'Broad spectrum control', 'contraindications': 'Liver disease, pregnancy', 'side_effects': 'Weight gain, tremor'}
            ],
            'Chronic Kidney Disease': [
                {'medicine': 'Erythropoietin', 'dosage': 'As prescribed', 'purpose': 'Treat anemia', 'contraindications': 'Uncontrolled hypertension', 'side_effects': 'High blood pressure'},
                {'medicine': 'Calcitriol', 'dosage': '0.25-1mcg daily', 'purpose': 'Vitamin D supplement', 'contraindications': 'High calcium levels', 'side_effects': 'Increased calcium'},
                {'medicine': 'Sevelamer', 'dosage': '800-1600mg with meals', 'purpose': 'Phosphate control', 'contraindications': 'Bowel obstruction', 'side_effects': 'Constipation, nausea'}
            ],
            'Ulcerative Colitis': [
                {'medicine': 'Mesalamine', 'dosage': '2.4-4.8g daily', 'purpose': 'Reduce inflammation', 'contraindications': 'Salicylate allergy', 'side_effects': 'Headache, nausea'},
                {'medicine': 'Azathioprine', 'dosage': '50-150mg daily', 'purpose': 'Immune suppression', 'contraindications': 'Lymphoma history', 'side_effects': 'Increased infection risk'},
                {'medicine': 'Infliximab', 'dosage': 'As prescribed IV', 'purpose': 'Severe disease', 'contraindications': 'Active TB', 'side_effects': 'Infusion reactions'}
            ],
            'Schizophrenia': [
                {'medicine': 'Risperidone', 'dosage': '2-6mg daily', 'purpose': 'Antipsychotic', 'contraindications': 'Dementia', 'side_effects': 'Weight gain, movement disorders'},
                {'medicine': 'Olanzapine', 'dosage': '5-20mg daily', 'purpose': 'Symptom control', 'contraindications': 'Diabetes risk', 'side_effects': 'Metabolic changes'},
                {'medicine': 'Clozapine', 'dosage': '25-400mg daily', 'purpose': 'Treatment-resistant cases', 'contraindications': 'Low WBC', 'side_effects': 'Regular blood monitoring needed'}
            ],
            'Bipolar Disorder': [
                {'medicine': 'Lithium', 'dosage': '600-1200mg daily', 'purpose': 'Mood stabilizer', 'contraindications': 'Kidney disease', 'side_effects': 'Tremor, thirst'},
                {'medicine': 'Quetiapine', 'dosage': '300-800mg daily', 'purpose': 'Acute mania', 'contraindications': 'Heart problems', 'side_effects': 'Sedation, dry mouth'},
                {'medicine': 'Valproate', 'dosage': '750-2000mg daily', 'purpose': 'Mood stabilization', 'contraindications': 'Liver disease', 'side_effects': 'Weight gain, hair loss'}
            ],
            'Glaucoma': [
                {'medicine': 'Latanoprost', 'dosage': '1 drop daily', 'purpose': 'Reduce eye pressure', 'contraindications': 'Eye inflammation', 'side_effects': 'Eye color change'},
                {'medicine': 'Timolol', 'dosage': '1 drop twice daily', 'purpose': 'Decrease fluid', 'contraindications': 'Asthma', 'side_effects': 'Burning, stinging'},
                {'medicine': 'Brimonidine', 'dosage': '1 drop 3 times daily', 'purpose': 'Pressure control', 'contraindications': 'Depression', 'side_effects': 'Eye irritation'}
            ],
            'Allergic Rhinitis': [
                {'medicine': 'Cetirizine', 'dosage': '10mg once daily', 'purpose': 'Allergy relief', 'contraindications': 'Kidney disease', 'side_effects': 'Drowsiness, dry mouth'},
                {'medicine': 'Fluticasone nasal spray', 'dosage': '1-2 sprays per nostril daily', 'purpose': 'Nasal symptoms', 'contraindications': 'Nasal injury', 'side_effects': 'Nose irritation'},
                {'medicine': 'Montelukast', 'dosage': '10mg once daily', 'purpose': 'Allergy prevention', 'contraindications': 'Liver disease', 'side_effects': 'Headache, mood changes'}
            ],
            'Acne': [
                {'medicine': 'Benzoyl Peroxide', 'dosage': 'Apply 2.5-5% gel once daily', 'purpose': 'Kill bacteria', 'contraindications': 'Sensitive skin', 'side_effects': 'Dryness, peeling'},
                {'medicine': 'Tretinoin', 'dosage': 'Apply 0.025-0.05% cream at night', 'purpose': 'Unclog pores', 'contraindications': 'Pregnancy', 'side_effects': 'Sun sensitivity'},
                {'medicine': 'Doxycycline', 'dosage': '50-100mg twice daily', 'purpose': 'Severe acne', 'contraindications': 'Pregnancy', 'side_effects': 'Sun sensitivity, upset stomach'}
            ],
            'GERD': [
                {'medicine': 'Esomeprazole', 'dosage': '20-40mg once daily', 'purpose': 'Acid reduction', 'contraindications': 'Osteoporosis risk', 'side_effects': 'Headache, diarrhea'},
                {'medicine': 'Ranitidine', 'dosage': '150mg twice daily', 'purpose': 'Acid control', 'contraindications': 'Kidney disease', 'side_effects': 'Headache, constipation'},
                {'medicine': 'Sucralfate', 'dosage': '1g four times daily', 'purpose': 'Protect esophagus', 'contraindications': 'Kidney stones', 'side_effects': 'Constipation'}
            ],
            'Urinary Tract Infection': [
                {'medicine': 'Nitrofurantoin', 'dosage': '100mg twice daily', 'purpose': 'Bacterial infection', 'contraindications': 'Kidney disease', 'side_effects': 'Nausea, headache'},
                {'medicine': 'Trimethoprim', 'dosage': '200mg twice daily', 'purpose': 'Bacterial infection', 'contraindications': 'Pregnancy', 'side_effects': 'Rash, nausea'},
                {'medicine': 'Cranberry extract', 'dosage': '500mg daily', 'purpose': 'Prevention', 'contraindications': 'Blood thinners', 'side_effects': 'Mild stomach upset'}
            ],
            'Conjunctivitis': [
                {'medicine': 'Chloramphenicol eye drops', 'dosage': '1 drop 4 times daily', 'purpose': 'Bacterial infection', 'contraindications': 'Eye surgery', 'side_effects': 'Mild stinging'},
                {'medicine': 'Artificial tears', 'dosage': '1-2 drops as needed', 'purpose': 'Comfort', 'contraindications': 'None significant', 'side_effects': 'Temporary blurred vision'},
                {'medicine': 'Antihistamine eye drops', 'dosage': '1 drop twice daily', 'purpose': 'Allergic cases', 'contraindications': 'Contact lenses', 'side_effects': 'Brief stinging'}
            ],
            'Insomnia': [
                {'medicine': 'Melatonin', 'dosage': '2-5mg before bed', 'purpose': 'Sleep regulation', 'contraindications': 'Autoimmune conditions', 'side_effects': 'Morning grogginess'},
                {'medicine': 'Zolpidem', 'dosage': '5-10mg at bedtime', 'purpose': 'Sleep initiation', 'contraindications': 'Sleep apnea', 'side_effects': 'Dizziness, confusion'},
                {'medicine': 'Trazodone', 'dosage': '25-100mg at bedtime', 'purpose': 'Sleep maintenance', 'contraindications': 'Heart rhythm problems', 'side_effects': 'Morning drowsiness'}
            ],
            'Hemorrhoids': [
                {'medicine': 'Hydrocortisone cream', 'dosage': 'Apply 1% cream 2-3 times daily', 'purpose': 'Inflammation relief', 'contraindications': 'Fungal infection', 'side_effects': 'Skin thinning'},
                {'medicine': 'Witch hazel pads', 'dosage': 'Apply 3-4 times daily', 'purpose': 'Pain relief', 'contraindications': 'None significant', 'side_effects': 'Mild irritation'},
                {'medicine': 'Docusate sodium', 'dosage': '100mg twice daily', 'purpose': 'Stool softener', 'contraindications': 'Intestinal blockage', 'side_effects': 'Cramping'}
            ],
            'Vertigo': [
                {'medicine': 'Betahistine', 'dosage': '16mg three times daily', 'purpose': 'Balance improvement', 'contraindications': 'Asthma', 'side_effects': 'Headache, upset stomach'},
                {'medicine': 'Dimenhydrinate', 'dosage': '50mg every 4-6 hours', 'purpose': 'Motion sickness', 'contraindications': 'Glaucoma', 'side_effects': 'Drowsiness'},
                {'medicine': 'Meclizine', 'dosage': '25-50mg daily', 'purpose': 'Dizziness relief', 'contraindications': 'Prostate problems', 'side_effects': 'Dry mouth'}
            ],
            'Tonsillitis': [
                {'medicine': 'Phenoxymethylpenicillin', 'dosage': '500mg four times daily', 'purpose': 'Bacterial infection', 'contraindications': 'Penicillin allergy', 'side_effects': 'Nausea, rash'},
                {'medicine': 'Ibuprofen', 'dosage': '400mg three times daily', 'purpose': 'Pain relief', 'contraindications': 'Stomach ulcers', 'side_effects': 'Stomach upset'},
                {'medicine': 'Benzydamine gargle', 'dosage': '15ml every 1.5-3 hours', 'purpose': 'Pain relief', 'contraindications': 'None significant', 'side_effects': 'Numbness'}
            ],
            'Scabies': [
                {'medicine': 'Permethrin cream', 'dosage': 'Apply 5% cream once', 'purpose': 'Kill mites', 'contraindications': 'Sensitivity to chrysanthemums', 'side_effects': 'Skin irritation'},
                {'medicine': 'Ivermectin', 'dosage': '200mcg/kg single dose', 'purpose': 'Systemic treatment', 'contraindications': 'Pregnancy', 'side_effects': 'Nausea, dizziness'},
                {'medicine': 'Antihistamine', 'dosage': 'As directed', 'purpose': 'Itch relief', 'contraindications': 'Varies by medicine', 'side_effects': 'Drowsiness'}
            ],
            'Heart Attack': [
                {'medicine': 'Aspirin', 'dosage': '300mg immediately then 75mg daily', 'purpose': 'Blood thinning', 'contraindications': 'Bleeding disorders', 'side_effects': 'Stomach irritation'},
                {'medicine': 'Clopidogrel', 'dosage': '300mg loading then 75mg daily', 'purpose': 'Prevent clots', 'contraindications': 'Active bleeding', 'side_effects': 'Bruising'},
                {'medicine': 'Metoprolol', 'dosage': '25-100mg twice daily', 'purpose': 'Heart rate control', 'contraindications': 'Severe heart failure', 'side_effects': 'Fatigue, dizziness'},
                {'medicine': 'Atorvastatin', 'dosage': '40-80mg daily', 'purpose': 'Cholesterol control', 'contraindications': 'Liver disease', 'side_effects': 'Muscle pain'}
            ],
            'Anemia': [
                {'medicine': 'Ferrous Sulfate', 'dosage': '325mg 2-3 times daily', 'purpose': 'Iron deficiency', 'contraindications': 'Iron overload', 'side_effects': 'Constipation'},
                {'medicine': 'Vitamin B12', 'dosage': '1000mcg daily', 'purpose': 'B12 deficiency', 'contraindications': 'None significant', 'side_effects': 'Mild diarrhea'},
                {'medicine': 'Folic Acid', 'dosage': '400mcg daily', 'purpose': 'Folate deficiency', 'contraindications': 'B12 deficiency', 'side_effects': 'Rare side effects'}
            ],
            'Drug Allergy': [
                {'medicine': 'Epinephrine auto-injector', 'dosage': '0.3mg IM for severe reaction', 'purpose': 'Emergency treatment', 'contraindications': 'None in emergency', 'side_effects': 'Anxiety, palpitations'},
                {'medicine': 'Diphenhydramine', 'dosage': '25-50mg every 4-6 hours', 'purpose': 'Allergy symptoms', 'contraindications': 'Glaucoma', 'side_effects': 'Drowsiness'},
                {'medicine': 'Prednisone', 'dosage': '40-60mg daily taper', 'purpose': 'Severe reactions', 'contraindications': 'Systemic infections', 'side_effects': 'Mood changes, insomnia'}
            ],
            'Severe Allergic Reaction': [
                {'medicine': 'Epinephrine auto-injector', 'dosage': '0.3mg IM', 'purpose': 'Emergency treatment', 'contraindications': 'None in emergency', 'side_effects': 'Tremors, anxiety'},
                {'medicine': 'Chlorpheniramine', 'dosage': '4mg every 4-6 hours', 'purpose': 'Antihistamine', 'contraindications': 'Glaucoma', 'side_effects': 'Drowsiness'},
                {'medicine': 'Hydrocortisone', 'dosage': '100mg IV', 'purpose': 'Reduce inflammation', 'contraindications': 'Active infection', 'side_effects': 'Blood sugar increase'}
            ],
            'Angina': [
                {'medicine': 'Nitroglycerin', 'dosage': '0.4mg sublingual PRN', 'purpose': 'Immediate relief', 'contraindications': 'Low blood pressure', 'side_effects': 'Headache'},
                {'medicine': 'Isosorbide Mononitrate', 'dosage': '30-60mg daily', 'purpose': 'Prevention', 'contraindications': 'Severe anemia', 'side_effects': 'Dizziness'},
                {'medicine': 'Amlodipine', 'dosage': '5-10mg daily', 'purpose': 'Blood pressure control', 'contraindications': 'Severe hypotension', 'side_effects': 'Ankle swelling'}
            ],
            'Iron Deficiency': [
                {'medicine': 'Ferrous Sulfate', 'dosage': '325mg 2-3 times daily', 'purpose': 'Iron replacement', 'contraindications': 'Iron overload', 'side_effects': 'Constipation'},
                {'medicine': 'Vitamin C', 'dosage': '500mg with iron', 'purpose': 'Iron absorption', 'contraindications': 'Kidney stones', 'side_effects': 'Stomach upset'},
                {'medicine': 'Iron Complex', 'dosage': '150mg daily', 'purpose': 'Gentle iron replacement', 'contraindications': 'Hemochromatosis', 'side_effects': 'Nausea'}
            ],
            'Atrial Fibrillation': [
                {'medicine': 'Warfarin', 'dosage': 'As per INR', 'purpose': 'Prevent clots', 'contraindications': 'Active bleeding', 'side_effects': 'Bleeding risk'},
                {'medicine': 'Diltiazem', 'dosage': '120-360mg daily', 'purpose': 'Rate control', 'contraindications': 'Heart block', 'side_effects': 'Low blood pressure'},
                {'medicine': 'Amiodarone', 'dosage': '200mg daily', 'purpose': 'Rhythm control', 'contraindications': 'Thyroid disease', 'side_effects': 'Organ toxicity'}
            ],
            'Deep Vein Thrombosis': [
                {'medicine': 'Rivaroxaban', 'dosage': '15mg twice daily', 'purpose': 'Blood thinner', 'contraindications': 'Active bleeding', 'side_effects': 'Bleeding risk'},
                {'medicine': 'Enoxaparin', 'dosage': '1mg/kg twice daily', 'purpose': 'Initial treatment', 'contraindications': 'Severe kidney disease', 'side_effects': 'Bruising'},
                {'medicine': 'Compression stockings', 'dosage': 'Wear during day', 'purpose': 'Prevent complications', 'contraindications': 'Arterial disease', 'side_effects': 'Skin irritation'}
            ],
            'Pulmonary Embolism': [
                {'medicine': 'Heparin', 'dosage': 'As per protocol', 'purpose': 'Immediate treatment', 'contraindications': 'Active bleeding', 'side_effects': 'Bleeding risk'},
                {'medicine': 'Apixaban', 'dosage': '10mg twice daily', 'purpose': 'Long-term prevention', 'contraindications': 'Severe liver disease', 'side_effects': 'Bleeding'},
                {'medicine': 'Oxygen therapy', 'dosage': 'As needed', 'purpose': 'Oxygen support', 'contraindications': 'None', 'side_effects': 'Dry nose'}
            ],
            'Severe Pneumonia': [
                {'medicine': 'Ceftriaxone', 'dosage': '2g daily IV', 'purpose': 'Bacterial infection', 'contraindications': 'Severe allergy', 'side_effects': 'Diarrhea'},
                {'medicine': 'Azithromycin', 'dosage': '500mg daily', 'purpose': 'Atypical coverage', 'contraindications': 'Liver disease', 'side_effects': 'GI upset'},
                {'medicine': 'Oxygen therapy', 'dosage': 'As needed', 'purpose': 'Oxygen support', 'contraindications': 'None', 'side_effects': 'Dry mucosa'}
            ],
            'Food Allergy': [
                {'medicine': 'Epinephrine auto-injector', 'dosage': '0.3mg IM if needed', 'purpose': 'Emergency treatment', 'contraindications': 'None in emergency', 'side_effects': 'Anxiety, tremors'},
                {'medicine': 'Fexofenadine', 'dosage': '180mg daily', 'purpose': 'Prevention', 'contraindications': 'Kidney disease', 'side_effects': 'Headache'},
                {'medicine': 'Ranitidine', 'dosage': '150mg twice daily', 'purpose': 'Histamine blocker', 'contraindications': 'Liver disease', 'side_effects': 'Constipation'}
            ],
            'Seasonal Allergies': [
                {'medicine': 'Loratadine', 'dosage': '10mg daily', 'purpose': 'Allergy relief', 'contraindications': 'None significant', 'side_effects': 'Mild drowsiness'},
                {'medicine': 'Fluticasone nasal', 'dosage': '1-2 sprays each nostril daily', 'purpose': 'Nasal symptoms', 'contraindications': 'Nasal injury', 'side_effects': 'Nosebleeds'},
                {'medicine': 'Cromolyn eye drops', 'dosage': '1-2 drops 4-6 times daily', 'purpose': 'Eye symptoms', 'contraindications': 'None significant', 'side_effects': 'Burning sensation'}
            ],
            'Congestive Heart Failure': [
                {'medicine': 'Furosemide', 'dosage': '20-80mg daily', 'purpose': 'Fluid removal', 'contraindications': 'Severe dehydration', 'side_effects': 'Frequent urination'},
                {'medicine': 'Carvedilol', 'dosage': '3.125-25mg twice daily', 'purpose': 'Heart function', 'contraindications': 'Severe asthma', 'side_effects': 'Dizziness'},
                {'medicine': 'Lisinopril', 'dosage': '2.5-40mg daily', 'purpose': 'Heart protection', 'contraindications': 'Pregnancy', 'side_effects': 'Dry cough'}
            ],
            'Pericarditis': [
                {'medicine': 'Ibuprofen', 'dosage': '600-800mg three times daily', 'purpose': 'Inflammation', 'contraindications': 'Bleeding risk', 'side_effects': 'Stomach upset'},
                {'medicine': 'Colchicine', 'dosage': '0.6mg twice daily', 'purpose': 'Prevention', 'contraindications': 'Kidney disease', 'side_effects': 'Diarrhea'},
                {'medicine': 'Prednisone', 'dosage': '0.25-0.5mg/kg daily', 'purpose': 'Severe cases', 'contraindications': 'Active infection', 'side_effects': 'Weight gain'}
            ],
            'Unstable Angina': [
                {'medicine': 'Morphine', 'dosage': '2-4mg IV PRN', 'purpose': 'Pain relief', 'contraindications': 'Respiratory depression', 'side_effects': 'Drowsiness'},
                {'medicine': 'Heparin', 'dosage': 'As per protocol', 'purpose': 'Blood thinner', 'contraindications': 'Active bleeding', 'side_effects': 'Bleeding risk'},
                {'medicine': 'Nitroglycerin', 'dosage': '0.4mg SL every 5 min PRN', 'purpose': 'Chest pain', 'contraindications': 'Low BP', 'side_effects': 'Headache'}
            ]
        }
        
        # Add age-specific dosage adjustments
        self.age_adjustments = {
            'child': {
                'dosage_factor': 0.5,
                'special_instructions': 'Consult pediatrician for exact dosing',
                'contraindications': ['Adult strength medications', 'Certain antihistamines']
            },
            'elderly': {
                'dosage_factor': 0.75,
                'special_instructions': 'Monitor for side effects closely',
                'contraindications': ['High-dose NSAIDs', 'Certain antihistamines']
            }
        }
        
        # Add condition-based restrictions
        self.condition_restrictions = {
            'pregnancy': {
                'avoid_medicines': ['NSAIDs in third trimester', 'Certain antihistamines'],
                'special_instructions': 'Consult healthcare provider before taking any medication'
            },
            'liver_disease': {
                'avoid_medicines': ['High-dose paracetamol', 'Certain NSAIDs'],
                'special_instructions': 'Regular liver function monitoring required'
            },
            'kidney_disease': {
                'avoid_medicines': ['NSAIDs', 'High-dose medications'],
                'special_instructions': 'Dose adjustment may be required'
            }
        }

    def get_recommendations(self, disease, age=None, gender=None, conditions=None):
        """Get medicine recommendations for a specific disease"""
        
        # Initialize recommendations dictionary
        recommendations = {
            'medicines': [],
            'warnings': []
        }
        
        # Check if we have recommendations for this disease
        if disease not in self.recommendations:
            recommendations['warnings'].append(f"No specific medicine recommendations available for {disease}. Please consult a healthcare provider.")
            return recommendations
            
        # Get medicines for the specific disease only
        recommendations['medicines'] = self.recommendations[disease]
        
        # Add age-specific warnings if age is provided
        if age:
            age_group = self._get_age_group(age)
            if age_group == 'infant':
                recommendations['warnings'].append("Special dosing required for infants. Consult pediatrician.")
            elif age_group == 'child':
                recommendations['warnings'].append("Child dosing required. Consult pediatrician.")
            elif age_group == 'elderly':
                recommendations['warnings'].append("Elderly patients may need dose adjustments. Monitor closely.")
        
        # Add condition-specific warnings
        if conditions:
            for condition in conditions:
                if condition.lower() == 'pregnancy':
                    recommendations['warnings'].append("Some medications may not be safe during pregnancy. Consult healthcare provider.")
                elif condition.lower() in ['liver disease', 'kidney disease']:
                    recommendations['warnings'].append(f"Dose adjustments may be needed due to {condition}. Consult healthcare provider.")
        
        return recommendations

    def _get_age_group(self, age):
        if age < 2:
            return 'infant'
        elif age < 12:
            return 'child'
        elif age < 18:
            return 'teen'
        elif age < 65:
            return 'adult'
        else:
            return 'elderly'

    def get_alternative_medicines(self, medicine, conditions=None):
        """Get alternative medicines for a given medicine considering patient conditions"""
        alternatives = {
            'Paracetamol': ['Ibuprofen', 'Aspirin'],
            'Ibuprofen': ['Paracetamol', 'Naproxen'],
            'Chlorpheniramine': ['Loratadine', 'Cetirizine'],
            # Add more alternatives
        }
        
        if medicine not in alternatives:
            return []
            
        if not conditions:
            return alternatives[medicine]
            
        # Filter alternatives based on conditions
        return [
            alt for alt in alternatives[medicine]
            if not any(
                alt in self.condition_restrictions.get(condition, {}).get('avoid_medicines', [])
                for condition in conditions
            )
        ]

    def get_precautions(self, disease):
        """Get precautions for a disease"""
        return self.precautions.get(disease, []) 