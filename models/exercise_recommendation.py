class ExerciseRecommender:
    def __init__(self):
        # Disease name mappings
        self.disease_mappings = {
            'common_cold': 'Common Cold',
            'bronchitis': 'Bronchitis',
            'hypertension': 'Hypertension',
            'high blood pressure': 'Hypertension',
            'diabetes': 'Diabetes',
            'diabetes type 2': 'Diabetes',
            'type 2 diabetes': 'Diabetes',
            'arthritis': 'Arthritis',
            'joint pain': 'Arthritis',
            'anxiety': 'Anxiety',
            'panic disorder': 'Anxiety',
            'asthma': 'Asthma',
            'breathing difficulty': 'Asthma',
            'pneumonia': 'Bronchitis',  # Similar breathing exercises
            'gastritis': 'Gastritis',
            'stomach inflammation': 'Gastritis',
            'migraine': 'Anxiety',  # Similar relaxation exercises
            'dengue': 'Common Cold',  # Very light exercises during recovery
            'typhoid': 'Common Cold',  # Very light exercises during recovery
            'malaria': 'Common Cold',  # Very light exercises during recovery
            'tuberculosis': 'Bronchitis',  # Similar breathing exercises
            'back pain': 'Back Pain',
            'lower back pain': 'Back Pain',
            'depression': 'Depression',
            'major depression': 'Depression',
            'clinical depression': 'Depression',
            'obesity': 'Obesity',
            'overweight': 'Obesity',
            'osteoporosis': 'Osteoporosis',
            'bone loss': 'Osteoporosis',
            'copd': 'COPD',
            'chronic obstructive pulmonary disease': 'COPD',
            'emphysema': 'COPD',
            'fibromyalgia': 'Fibromyalgia',
            'chronic pain syndrome': 'Fibromyalgia',
            'multiple sclerosis': 'Multiple Sclerosis',
            'ms': 'Multiple Sclerosis',
            'parkinsons': 'Parkinsons Disease',
            'parkinsons disease': 'Parkinsons Disease',
            'stroke': 'Stroke Recovery',
            'stroke recovery': 'Stroke Recovery',
            'post stroke': 'Stroke Recovery',
            'heart disease': 'Heart Disease',
            'coronary artery disease': 'Heart Disease',
            'heart failure': 'Heart Disease',
            'cardiac disease': 'Heart Disease'
        }

        # Intensity levels and guidelines
        self.intensity_levels = {
            'very_light': {
                'heart_rate': '< 50% max heart rate',
                'breathing': 'Normal breathing, can easily hold conversation',
                'duration': '5-15 minutes',
                'frequency': 'As tolerated',
                'signs_too_much': [
                    'Feeling exhausted',
                    'Difficulty breathing',
                    'Dizziness',
                    'Increased pain'
                ]
            },
            'light': {
                'heart_rate': '50-60% max heart rate',
                'breathing': 'Slightly elevated but can hold conversation',
                'duration': '15-30 minutes',
                'frequency': 'Daily if possible',
                'signs_too_much': [
                    'Cannot hold conversation',
                    'Excessive sweating',
                    'Feeling strain'
                ]
            },
            'light_to_moderate': {
                'heart_rate': '60-70% max heart rate',
                'breathing': 'Moderately elevated, conversation possible with effort',
                'duration': '20-40 minutes',
                'frequency': '3-5 times per week',
                'signs_too_much': [
                    'Cannot speak comfortably',
                    'Feeling significant strain',
                    'Excessive fatigue after exercise'
                ]
            },
            'moderate': {
                'heart_rate': '70-80% max heart rate',
                'breathing': 'Definitely elevated, conversation difficult',
                'duration': '30-60 minutes',
                'frequency': '3-5 times per week',
                'signs_too_much': [
                    'Cannot maintain form',
                    'Feeling very out of breath',
                    'Significant muscle fatigue'
                ]
            }
        }

        self.exercise_plans = {
            'Common Cold': {
                'acute_phase': {
                    'intensity': 'very_light',
                    'exercises': [
                        {
                            'name': 'Deep Breathing',
                            'duration': '5-10 minutes',
                            'frequency': '3-4 times daily',
                            'instructions': 'Sit upright, breathe deeply through nose, exhale slowly through mouth',
                            'benefits': 'Helps clear airways, reduces congestion',
                            'precautions': 'Stop if feeling dizzy'
                        },
                        {
                            'name': 'Gentle Walking',
                            'duration': '5-10 minutes',
                            'frequency': 'Once or twice daily if feeling up to it',
                            'instructions': 'Walk slowly around your home or garden',
                            'benefits': 'Maintains circulation, prevents stiffness',
                            'precautions': 'Only if fever-free and feeling capable'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'light',
                    'exercises': [
                        {
                            'name': 'Walking',
                            'duration': '15-20 minutes',
                            'frequency': 'Once or twice daily',
                            'instructions': 'Walk at a comfortable pace outdoors',
                            'benefits': 'Improves circulation, boosts immune function',
                            'precautions': 'Wear appropriate clothing, avoid cold air'
                        },
                        {
                            'name': 'Light Stretching',
                            'duration': '10-15 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Gentle full-body stretches',
                            'benefits': 'Reduces muscle tension, improves flexibility',
                            'precautions': 'Don\'t overstretch'
                        }
                    ]
                }
            },
            'Bronchitis': {
                'acute_phase': {
                    'intensity': 'very_light',
                    'exercises': [
                        {
                            'name': 'Pursed Lip Breathing',
                            'duration': '5-10 minutes',
                            'frequency': '4-5 times daily',
                            'instructions': 'Inhale through nose, exhale slowly through pursed lips',
                            'benefits': 'Improves breathing control, reduces shortness of breath',
                            'precautions': 'Stop if feeling lightheaded'
                        },
                        {
                            'name': 'Diaphragmatic Breathing',
                            'duration': '5-10 minutes',
                            'frequency': '3-4 times daily',
                            'instructions': 'Place hand on belly, breathe to expand belly not chest',
                            'benefits': 'Strengthens breathing muscles',
                            'precautions': 'Practice when relaxed'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'light_to_moderate',
                    'exercises': [
                        {
                            'name': 'Brisk Walking',
                            'duration': '20-30 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Walk at a pace that allows conversation',
                            'benefits': 'Improves lung capacity, overall fitness',
                            'precautions': 'Use inhaler if prescribed before exercise'
                        }
                    ]
                }
            },
            'Hypertension': {
                'acute_phase': {
                    'intensity': 'very_light',
                    'exercises': [
                        {
                            'name': 'Walking',
                            'duration': '10-15 minutes',
                            'frequency': '2-3 times daily',
                            'instructions': 'Walk at a comfortable pace, avoid hills initially',
                            'benefits': 'Helps lower blood pressure, improves circulation',
                            'precautions': 'Monitor blood pressure, stop if dizzy'
                        },
                        {
                            'name': 'Light Stretching',
                            'duration': '5-10 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Gentle full-body stretches, focus on breathing',
                            'benefits': 'Reduces stress, improves flexibility',
                            'precautions': 'No sudden movements'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'light_to_moderate',
                    'exercises': [
                        {
                            'name': 'Brisk Walking',
                            'duration': '30 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Walk at a faster pace, can include gentle hills',
                            'benefits': 'Cardiovascular health, blood pressure control',
                            'precautions': 'Stay hydrated, monitor breathing'
                        },
                        {
                            'name': 'Swimming',
                            'duration': '20-30 minutes',
                            'frequency': '3-4 times weekly',
                            'instructions': 'Gentle swimming or water walking',
                            'benefits': 'Low-impact cardio, full body workout',
                            'precautions': 'Avoid cold water, monitor heart rate'
                        }
                    ]
                }
            },
            'Diabetes': {
                'acute_phase': {
                    'intensity': 'light',
                    'exercises': [
                        {
                            'name': 'Walking',
                            'duration': '15-20 minutes',
                            'frequency': 'Twice daily',
                            'instructions': 'Walk after meals, maintain steady pace',
                            'benefits': 'Helps control blood sugar, improves insulin sensitivity',
                            'precautions': 'Check blood sugar before and after, carry quick sugar source'
                        },
                        {
                            'name': 'Resistance Band Exercises',
                            'duration': '10-15 minutes',
                            'frequency': '3 times weekly',
                            'instructions': 'Light resistance exercises for major muscle groups',
                            'benefits': 'Improves insulin sensitivity, builds muscle',
                            'precautions': 'Start with light resistance, proper form essential'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'moderate',
                    'exercises': [
                        {
                            'name': 'Circuit Training',
                            'duration': '20-30 minutes',
                            'frequency': '3 times weekly',
                            'instructions': 'Alternate between cardio and strength exercises',
                            'benefits': 'Improves overall fitness, blood sugar control',
                            'precautions': 'Monitor blood sugar, stay hydrated'
                        }
                    ]
                }
            },
            'Arthritis': {
                'acute_phase': {
                    'intensity': 'very_light',
                    'exercises': [
                        {
                            'name': 'Water Exercises',
                            'duration': '15-20 minutes',
                            'frequency': '3 times weekly',
                            'instructions': 'Gentle movements in warm water',
                            'benefits': 'Reduces joint stress, improves mobility',
                            'precautions': 'Use warm water, avoid cold pools'
                        },
                        {
                            'name': 'Range of Motion Exercises',
                            'duration': '10-15 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Gentle joint movements through full range',
                            'benefits': 'Maintains flexibility, reduces stiffness',
                            'precautions': 'Stop if pain increases'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'light',
                    'exercises': [
                        {
                            'name': 'Stationary Cycling',
                            'duration': '15-20 minutes',
                            'frequency': '3-4 times weekly',
                            'instructions': 'Low resistance, comfortable pace',
                            'benefits': 'Improves joint mobility, builds strength',
                            'precautions': 'Proper seat height, avoid high resistance'
                        }
                    ]
                }
            },
            'Anxiety': {
                'acute_phase': {
                    'intensity': 'light',
                    'exercises': [
                        {
                            'name': 'Deep Breathing Yoga',
                            'duration': '10-15 minutes',
                            'frequency': '2-3 times daily',
                            'instructions': 'Focus on breath, gentle yoga poses',
                            'benefits': 'Reduces anxiety, promotes relaxation',
                            'precautions': 'No forcing poses, stay within comfort zone'
                        },
                        {
                            'name': 'Walking Meditation',
                            'duration': '15-20 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Walk slowly, focus on steps and breath',
                            'benefits': 'Mindfulness, stress reduction',
                            'precautions': 'Choose quiet, safe locations'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'light_to_moderate',
                    'exercises': [
                        {
                            'name': 'Group Exercise Class',
                            'duration': '30-45 minutes',
                            'frequency': '2-3 times weekly',
                            'instructions': 'Join low-impact group classes',
                            'benefits': 'Social interaction, structured exercise',
                            'precautions': 'Choose beginner-friendly classes'
                        }
                    ]
                }
            },
            'Depression': {
                'acute_phase': {
                    'intensity': 'light',
                    'exercises': [
                        {
                            'name': 'Morning Walk',
                            'duration': '10-15 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Walk outdoors in morning sunlight',
                            'benefits': 'Mood improvement, vitamin D exposure',
                            'precautions': 'Start small, build gradually'
                        },
                        {
                            'name': 'Gentle Stretching',
                            'duration': '10 minutes',
                            'frequency': 'Twice daily',
                            'instructions': 'Basic stretches, focus on breathing',
                            'benefits': 'Reduces tension, improves body awareness',
                            'precautions': 'No pressure to perform perfectly'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'moderate',
                    'exercises': [
                        {
                            'name': 'Mixed Activity Program',
                            'duration': '30 minutes',
                            'frequency': '5 times weekly',
                            'instructions': 'Combine walking, strength, and flexibility',
                            'benefits': 'Overall mood improvement, energy boost',
                            'precautions': 'Listen to body, adjust as needed'
                        }
                    ]
                }
            },
            'Osteoporosis': {
                'acute_phase': {
                    'intensity': 'light',
                    'exercises': [
                        {
                            'name': 'Balance Training',
                            'duration': '10-15 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Practice standing on one leg, heel-to-toe walk',
                            'benefits': 'Improves balance, reduces fall risk',
                            'precautions': 'Have support nearby, avoid risky movements'
                        },
                        {
                            'name': 'Seated Resistance Exercises',
                            'duration': '15-20 minutes',
                            'frequency': '3 times weekly',
                            'instructions': 'Light weights, focus on proper form',
                            'benefits': 'Builds bone density, strengthens muscles',
                            'precautions': 'Avoid high-impact movements, maintain good posture'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'light_to_moderate',
                    'exercises': [
                        {
                            'name': 'Walking Program',
                            'duration': '30 minutes',
                            'frequency': '5 times weekly',
                            'instructions': 'Brisk walking on even surfaces',
                            'benefits': 'Weight-bearing exercise, improves bone density',
                            'precautions': 'Wear supportive shoes, avoid uneven terrain'
                        },
                        {
                            'name': 'Tai Chi',
                            'duration': '20-30 minutes',
                            'frequency': '3 times weekly',
                            'instructions': 'Follow instructor or video guidance',
                            'benefits': 'Improves balance, strength, and coordination',
                            'precautions': 'Learn proper form, progress gradually'
                        }
                    ]
                }
            },
            'Hypothyroidism': {
                'acute_phase': {
                    'intensity': 'very_light',
                    'exercises': [
                        {
                            'name': 'Gentle Walking',
                            'duration': '10-15 minutes',
                            'frequency': 'Twice daily',
                            'instructions': 'Walk at comfortable pace, preferably outdoors',
                            'benefits': 'Boosts metabolism, increases energy',
                            'precautions': 'Start slowly, monitor fatigue levels'
                        },
                        {
                            'name': 'Light Yoga',
                            'duration': '15-20 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Focus on gentle poses and breathing',
                            'benefits': 'Improves flexibility, reduces stiffness',
                            'precautions': 'Avoid overexertion, listen to body'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'light',
                    'exercises': [
                        {
                            'name': 'Strength Training',
                            'duration': '20-30 minutes',
                            'frequency': '3 times weekly',
                            'instructions': 'Light weights, focus on form',
                            'benefits': 'Increases metabolism, builds muscle',
                            'precautions': 'Progress gradually, maintain proper form'
                        }
                    ]
                }
            },
            'Psoriasis': {
                'acute_phase': {
                    'intensity': 'light',
                    'exercises': [
                        {
                            'name': 'Swimming',
                            'duration': '20 minutes',
                            'frequency': '3 times weekly',
                            'instructions': 'Gentle swimming in chlorinated pool',
                            'benefits': 'Helps clear skin, reduces inflammation',
                            'precautions': 'Moisturize after swimming, avoid hot water'
                        },
                        {
                            'name': 'Stress-Relief Walking',
                            'duration': '15-20 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Walk in nature, focus on relaxation',
                            'benefits': 'Reduces stress, improves overall health',
                            'precautions': 'Protect skin from sun exposure'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'moderate',
                    'exercises': [
                        {
                            'name': 'Mixed Cardio',
                            'duration': '30 minutes',
                            'frequency': '4-5 times weekly',
                            'instructions': 'Combine different low-impact activities',
                            'benefits': 'Improves overall health, reduces inflammation',
                            'precautions': 'Wear appropriate clothing, avoid skin irritation'
                        }
                    ]
                }
            },
            'Fibromyalgia': {
                'acute_phase': {
                    'intensity': 'very_light',
                    'exercises': [
                        {
                            'name': 'Water Walking',
                            'duration': '10-15 minutes',
                            'frequency': '3 times weekly',
                            'instructions': 'Walk in waist-deep warm water',
                            'benefits': 'Low-impact movement, pain relief',
                            'precautions': 'Use warm water, avoid cold pools'
                        },
                        {
                            'name': 'Gentle Stretching',
                            'duration': '10 minutes',
                            'frequency': 'Daily',
                            'instructions': 'Very gentle stretches, focus on breathing',
                            'benefits': 'Reduces stiffness, improves flexibility',
                            'precautions': 'Stop if pain increases, avoid overstretching'
                        }
                    ]
                },
                'recovery_phase': {
                    'intensity': 'light',
                    'exercises': [
                        {
                            'name': 'Tai Chi',
                            'duration': '20 minutes',
                            'frequency': '2-3 times weekly',
                            'instructions': 'Follow gentle, flowing movements',
                            'benefits': 'Improves balance, reduces pain',
                            'precautions': 'Move within comfort zone, rest as needed'
                        },
                        {
                            'name': 'Recumbent Cycling',
                            'duration': '15-20 minutes',
                            'frequency': '3 times weekly',
                            'instructions': 'Use recumbent bike with low resistance',
                            'benefits': 'Builds endurance, low-impact cardio',
                            'precautions': 'Start with short sessions, increase gradually'
                        }
                    ]
                }
            },
            'Asthma': {
                'acute_phase': [
                    'Pursed Lip Breathing - 5-10 minutes (4-6 times daily)\nInstructions: Inhale through nose, exhale slowly through pursed lips\nBenefits: Improves breathing control\nPrecautions: Stop if wheezing increases',
                    'Diaphragmatic Breathing - 5-10 minutes (3-4 times daily)\nInstructions: Focus on belly breathing\nBenefits: Strengthens breathing muscles\nPrecautions: Use inhaler if needed'
                ],
                'recovery_phase': [
                    'Swimming - 20-30 minutes\nInstructions: Start with gentle strokes in warm water\nBenefits: Improves lung capacity in humid environment\nPrecautions: Indoor pool preferred',
                    'Walking - 15-20 minutes\nInstructions: Gradual pace on flat terrain\nBenefits: Builds cardio endurance\nPrecautions: Avoid cold or polluted air'
                ],
                'intensity': 'light'
            },
            'Hypertension': {
                'acute_phase': [
                    'Gentle Walking - 10-15 minutes (2-3 times daily)\nInstructions: Walk at comfortable pace on level ground\nBenefits: Helps regulate blood pressure\nPrecautions: Monitor BP before and after',
                    'Deep Breathing - 10 minutes (3-4 times daily)\nInstructions: Slow, controlled breathing\nBenefits: Reduces stress and BP\nPrecautions: Sit while exercising'
                ],
                'recovery_phase': [
                    'Brisk Walking - 30 minutes\nInstructions: Moderate pace walking\nBenefits: Improves cardiovascular health\nPrecautions: Check BP regularly',
                    'Swimming - 20-30 minutes\nInstructions: Gentle swimming or water aerobics\nBenefits: Low-impact cardio workout\nPrecautions: Avoid holding breath'
                ],
                'intensity': 'light_to_moderate'
            },
            'Diabetes': {
                'acute_phase': [
                    'Walking - 10-15 minutes (after meals)\nInstructions: Gentle walk post-meals\nBenefits: Helps control blood sugar\nPrecautions: Check glucose levels',
                    'Chair Exercises - 10 minutes\nInstructions: Simple seated movements\nBenefits: Maintains activity while monitoring\nPrecautions: Have sugar source nearby'
                ],
                'recovery_phase': [
                    'Mixed Cardio - 30 minutes\nInstructions: Combine walking, cycling, swimming\nBenefits: Improves insulin sensitivity\nPrecautions: Check glucose before/after',
                    'Resistance Training - 20-30 minutes\nInstructions: Light weights or resistance bands\nBenefits: Helps regulate blood sugar\nPrecautions: Start with supervision'
                ],
                'intensity': 'light_to_moderate'
            },
            'Arthritis': {
                'acute_phase': [
                    'Water Exercises - 15-20 minutes\nInstructions: Gentle movements in warm pool\nBenefits: Reduces joint stress\nPrecautions: Use warm water only',
                    'Isometric Exercises - 10 minutes\nInstructions: Static muscle contractions\nBenefits: Maintains strength without joint movement\nPrecautions: Avoid painful positions'
                ],
                'recovery_phase': [
                    'Low-Impact Cardio - 20-30 minutes\nInstructions: Stationary bike or elliptical\nBenefits: Improves joint mobility\nPrecautions: Adjust resistance carefully',
                    'Strength Training - 15-20 minutes\nInstructions: Light weights with proper form\nBenefits: Builds supporting muscles\nPrecautions: Focus on control'
                ],
                'intensity': 'light'
            },
            'Back Pain': {
                'acute_phase': [
                    'Walking - 5-10 minutes\nInstructions: Short, gentle walks on level ground\nBenefits: Maintains mobility\nPrecautions: Maintain good posture',
                    'Core Breathing - 5-10 minutes\nInstructions: Gentle core engagement with breath\nBenefits: Stabilizes spine\nPrecautions: Avoid straining'
                ],
                'recovery_phase': [
                    'Swimming - 20-30 minutes\nInstructions: Gentle swimming or water walking\nBenefits: Non-weight bearing exercise\nPrecautions: Avoid butterfly stroke',
                    'Core Strengthening - 15-20 minutes\nInstructions: Gentle planks and bridges\nBenefits: Improves spine stability\nPrecautions: Maintain neutral spine'
                ],
                'intensity': 'light'
            },
            'Depression': {
                'acute_phase': [
                    'Morning Walk - 10-15 minutes\nInstructions: Walk in natural light\nBenefits: Exposure to sunlight, mood improvement\nPrecautions: Start with short duration',
                    'Gentle Yoga - 15 minutes\nInstructions: Basic poses with breathing\nBenefits: Reduces stress, improves mood\nPrecautions: No pressure to perform'
                ],
                'recovery_phase': [
                    'Group Exercise - 30-45 minutes\nInstructions: Join group fitness classes\nBenefits: Social interaction, structured activity\nPrecautions: Choose supportive environment',
                    'Mixed Activities - 30 minutes\nInstructions: Combine walking, swimming, cycling\nBenefits: Variety maintains interest\nPrecautions: Progress gradually'
                ],
                'intensity': 'light_to_moderate'
            },
            'Anxiety': {
                'acute_phase': [
                    'Deep Breathing - 10-15 minutes\nInstructions: Focus on slow, controlled breaths\nBenefits: Reduces anxiety, centers mind\nPrecautions: Practice in quiet space',
                    'Walking Meditation - 15 minutes\nInstructions: Mindful walking in nature\nBenefits: Combines exercise and mindfulness\nPrecautions: Choose quiet routes'
                ],
                'recovery_phase': [
                    'Yoga - 30 minutes\nInstructions: Gentle flow with breathing focus\nBenefits: Improves mind-body connection\nPrecautions: Avoid overwhelming classes',
                    'Swimming - 20-30 minutes\nInstructions: Rhythmic swimming\nBenefits: Meditative movement in water\nPrecautions: Start with basic strokes'
                ],
                'intensity': 'light'
            },
            'Obesity': {
                'acute_phase': [
                    'Walking - 15-20 minutes\nInstructions: Start with short walks on flat ground\nBenefits: Builds basic endurance\nPrecautions: Wear supportive shoes',
                    'Water Walking - 15-20 minutes\nInstructions: Walk in chest-deep water\nBenefits: Reduced joint stress\nPrecautions: Use pool rails for support'
                ],
                'recovery_phase': [
                    'Mixed Cardio - 30-45 minutes\nInstructions: Combine walking, swimming, cycling\nBenefits: Burns calories, improves fitness\nPrecautions: Monitor heart rate',
                    'Strength Training - 20-30 minutes\nInstructions: Full body workout with light weights\nBenefits: Builds muscle, increases metabolism\nPrecautions: Focus on form'
                ],
                'intensity': 'light_to_moderate'
            },
            'Osteoporosis': {
                'acute_phase': [
                    'Balance Training - 10-15 minutes\nInstructions: Practice standing on one leg, heel-toe walks\nBenefits: Improves stability\nPrecautions: Have support nearby',
                    'Gentle Resistance - 15 minutes\nInstructions: Light weights, resistance bands\nBenefits: Maintains bone density\nPrecautions: Avoid high-impact movements'
                ],
                'recovery_phase': [
                    'Weight-Bearing Exercise - 20-30 minutes\nInstructions: Walking, stair climbing with support\nBenefits: Strengthens bones\nPrecautions: Avoid twisting movements',
                    'Strength Training - 20-30 minutes\nInstructions: Progressive resistance training\nBenefits: Builds bone and muscle\nPrecautions: Use proper form'
                ],
                'intensity': 'light'
            },
            'COPD': {
                'acute_phase': [
                    'Pursed Lip Breathing - 5-10 minutes\nInstructions: Inhale through nose, exhale slowly through pursed lips\nBenefits: Improves oxygen exchange\nPrecautions: Rest between sets',
                    'Seated Exercises - 10-15 minutes\nInstructions: Arm and leg movements while seated\nBenefits: Maintains strength\nPrecautions: Monitor breathing'
                ],
                'recovery_phase': [
                    'Walking Program - 20-30 minutes\nInstructions: Progressive walking with breaks\nBenefits: Improves endurance\nPrecautions: Use rescue inhaler if needed',
                    'Stationary Cycling - 15-20 minutes\nInstructions: Low resistance pedaling\nBenefits: Cardio without weight bearing\nPrecautions: Keep intensity moderate'
                ],
                'intensity': 'very_light'
            },
            'Fibromyalgia': {
                'acute_phase': [
                    'Gentle Stretching - 10-15 minutes\nInstructions: Very gentle full body stretches\nBenefits: Reduces stiffness\nPrecautions: Stop if pain increases',
                    'Water Therapy - 20 minutes\nInstructions: Gentle movements in warm water\nBenefits: Pain relief, improved mobility\nPrecautions: Use warm water only'
                ],
                'recovery_phase': [
                    'Tai Chi - 20-30 minutes\nInstructions: Slow, flowing movements\nBenefits: Improves balance, reduces pain\nPrecautions: Modify as needed',
                    'Low-Impact Cardio - 20 minutes\nInstructions: Elliptical or recumbent bike\nBenefits: Builds endurance\nPrecautions: Start slowly'
                ],
                'intensity': 'light'
            },
            'Multiple Sclerosis': {
                'acute_phase': [
                    'Cooling Exercises - 15-20 minutes\nInstructions: Exercise in cool environment\nBenefits: Prevents overheating\nPrecautions: Monitor temperature',
                    'Seated Exercises - 10-15 minutes\nInstructions: Range of motion exercises\nBenefits: Maintains mobility\nPrecautions: Rest when tired'
                ],
                'recovery_phase': [
                    'Pool Exercises - 20-30 minutes\nInstructions: Water-based movements\nBenefits: Supports body weight\nPrecautions: Use cool water',
                    'Balance Training - 15-20 minutes\nInstructions: Supported standing exercises\nBenefits: Improves stability\nPrecautions: Have support ready'
                ],
                'intensity': 'very_light'
            },
            'Parkinsons Disease': {
                'acute_phase': [
                    'Balance Exercises - 10-15 minutes\nInstructions: Supported standing practice\nBenefits: Improves stability\nPrecautions: Use sturdy support',
                    'Stretching - 15-20 minutes\nInstructions: Focus on tight muscle groups\nBenefits: Maintains flexibility\nPrecautions: Gentle movements'
                ],
                'recovery_phase': [
                    'Walking Program - 20-30 minutes\nInstructions: Focus on big steps\nBenefits: Improves gait\nPrecautions: Use walking aids if needed',
                    'Resistance Training - 20 minutes\nInstructions: Light weights, focus on control\nBenefits: Maintains strength\nPrecautions: Avoid heavy weights'
                ],
                'intensity': 'light'
            },
            'Stroke Recovery': {
                'acute_phase': [
                    'Passive Range of Motion - 15 minutes\nInstructions: Gentle assisted movements\nBenefits: Prevents stiffness\nPrecautions: Follow therapist guidance',
                    'Seated Balance - 10 minutes\nInstructions: Supported sitting exercises\nBenefits: Improves core strength\nPrecautions: Start with support'
                ],
                'recovery_phase': [
                    'Walking Practice - 20 minutes\nInstructions: With appropriate assistance\nBenefits: Regains mobility\nPrecautions: Use prescribed aids',
                    'Functional Training - 20-30 minutes\nInstructions: Practice daily activities\nBenefits: Improves independence\nPrecautions: Progress gradually'
                ],
                'intensity': 'very_light'
            },
            'Heart Disease': {
                'acute_phase': [
                    'Walking - 10-15 minutes\nInstructions: Short walks on level ground\nBenefits: Maintains circulation\nPrecautions: Monitor heart rate',
                    'Breathing Exercises - 10 minutes\nInstructions: Deep, controlled breathing\nBenefits: Reduces stress\nPrecautions: Stop if chest pain'
                ],
                'recovery_phase': [
                    'Cardiac Rehab Exercises - 30 minutes\nInstructions: Supervised program\nBenefits: Strengthens heart\nPrecautions: Follow program guidelines',
                    'Stationary Cycling - 20 minutes\nInstructions: Low resistance\nBenefits: Improves endurance\nPrecautions: Check pulse regularly'
                ],
                'intensity': 'very_light'
            }
        }

        # Add more disease-specific exercise plans here...

        self.condition_modifications = {
            'elderly': [
                'Reduce duration by 50%',
                'Reduce intensity by one level',
                'Include more rest periods',
                'Focus on balance and stability'
            ],
            'heart_condition': [
                'Reduce intensity to very_light',
                'Monitor heart rate closely',
                'Include longer warm-up',
                'More frequent rest periods'
            ],
            'respiratory_condition': [
                'Focus on breathing exercises',
                'Reduce cardio intensity',
                'Monitor breathing rate',
                'Stop if breathing becomes difficult'
            ]
        }

        self.exercise_recommendations = {
            'Common Cold': {
                'acute_phase': [
                    'Deep Breathing - 5-10 minutes (3-4 times daily)\nInstructions: Sit upright, breathe deeply through nose, exhale slowly through mouth\nBenefits: Helps clear airways, reduces congestion\nPrecautions: Stop if feeling dizzy',
                    'Gentle Walking - 5-10 minutes (Once or twice daily if feeling up to it)\nInstructions: Walk slowly around your home or garden\nBenefits: Maintains circulation, prevents stiffness\nPrecautions: Only if fever-free and feeling capable'
                ],
                'recovery_phase': [
                    'Walking - 15-20 minutes daily\nInstructions: Walk at a comfortable pace\nBenefits: Improves circulation and energy levels\nPrecautions: Stop if feeling exhausted',
                    'Light Stretching - 10 minutes daily\nInstructions: Gentle full-body stretches\nBenefits: Reduces muscle tension\nPrecautions: Avoid overexertion'
                ],
                'intensity': 'very_light'
            },
            'Flu': {
                'acute_phase': [
                    'Complete Rest - No exercise during fever\nInstructions: Focus on rest and recovery\nBenefits: Allows body to fight infection\nPrecautions: Essential during acute phase',
                    'Deep Breathing - 5 minutes (2-3 times daily)\nInstructions: Gentle breathing exercises in bed\nBenefits: Prevents lung congestion\nPrecautions: Stop if causing fatigue'
                ],
                'recovery_phase': [
                    'Short Walks - 5-10 minutes\nInstructions: Start with walking around home\nBenefits: Gradually rebuild strength\nPrecautions: Only after fever subsides',
                    'Light Stretching - 5-10 minutes\nInstructions: Basic stretches to prevent stiffness\nBenefits: Maintains mobility\nPrecautions: Stop if tired'
                ],
                'intensity': 'very_light'
            },
            'Pneumonia': {
                'acute_phase': [
                    'Pursed Lip Breathing - 5-10 minutes (4-5 times daily)\nInstructions: Inhale through nose, exhale slowly through pursed lips\nBenefits: Improves breathing control, reduces shortness of breath\nPrecautions: Stop if feeling lightheaded',
                    'Diaphragmatic Breathing - 5-10 minutes (3-4 times daily)\nInstructions: Place hand on belly, breathe to expand belly not chest\nBenefits: Strengthens breathing muscles\nPrecautions: Practice when relaxed'
                ],
                'recovery_phase': [
                    'Walking - 10-15 minutes\nInstructions: Gradual increase in duration\nBenefits: Improves lung capacity\nPrecautions: Monitor breathing rate',
                    'Respiratory Muscle Training - As prescribed\nInstructions: Use incentive spirometer\nBenefits: Strengthens lungs\nPrecautions: Follow medical guidance'
                ],
                'intensity': 'very_light'
            },
            'Migraine': {
                'acute_phase': [
                    'Rest in Dark Room - As needed\nInstructions: Complete rest in quiet, dark environment\nBenefits: Reduces sensory stimulation\nPrecautions: Essential during acute phase',
                    'Gentle Neck Stretches - 5 minutes\nInstructions: Very gentle neck and shoulder movements\nBenefits: Relieves tension\nPrecautions: Stop if pain increases'
                ],
                'recovery_phase': [
                    'Walking - 15-20 minutes\nInstructions: Walk in calm environment\nBenefits: Improves circulation\nPrecautions: Avoid bright sunlight',
                    'Light Yoga - 10-15 minutes\nInstructions: Gentle poses, no inversions\nBenefits: Reduces stress and tension\nPrecautions: Avoid head-down positions'
                ],
                'intensity': 'light'
            },
            'Dengue': {
                'acute_phase': [
                    'Complete Bed Rest - During fever\nInstructions: Focus on rest and recovery\nBenefits: Conserves energy for healing\nPrecautions: Essential during fever phase',
                    'Gentle Joint Movement - 5 minutes (2-3 times daily)\nInstructions: Move joints gently while in bed\nBenefits: Prevents stiffness\nPrecautions: Stop if painful'
                ],
                'recovery_phase': [
                    'Short Walks - 5-10 minutes\nInstructions: Start with walking inside home\nBenefits: Rebuilds strength gradually\nPrecautions: Monitor fatigue levels',
                    'Light Stretching - 5-10 minutes\nInstructions: Gentle full-body stretches\nBenefits: Improves flexibility\nPrecautions: Avoid overexertion'
                ],
                'intensity': 'very_light'
            },
            'Malaria': {
                'acute_phase': [
                    'Complete Rest - During fever cycles\nInstructions: Rest during fever episodes\nBenefits: Allows body to fight infection\nPrecautions: Essential during acute phase',
                    'Gentle Movement - 5 minutes\nInstructions: Basic movements in bed\nBenefits: Prevents muscle weakness\nPrecautions: Only when fever is down'
                ],
                'recovery_phase': [
                    'Walking - 10-15 minutes\nInstructions: Start with short distances\nBenefits: Rebuilds strength\nPrecautions: Monitor energy levels',
                    'Light Activities - 10-15 minutes\nInstructions: Simple daily activities\nBenefits: Improves stamina\nPrecautions: Rest when tired'
                ],
                'intensity': 'very_light'
            },
            'Tuberculosis': {
                'acute_phase': [
                    'Breathing Exercises - 10 minutes (3-4 times daily)\nInstructions: Deep breathing in isolated environment\nBenefits: Maintains lung function\nPrecautions: Use mask, isolated area',
                    'Postural Drainage - As prescribed\nInstructions: Follow medical guidance\nBenefits: Helps clear lungs\nPrecautions: Do under supervision'
                ],
                'recovery_phase': [
                    'Walking - 15-20 minutes\nInstructions: Gradual increase in duration\nBenefits: Improves stamina\nPrecautions: Wear mask outdoors',
                    'Light Resistance Exercises - 10-15 minutes\nInstructions: Simple strength exercises\nBenefits: Rebuilds muscle\nPrecautions: Monitor breathing'
                ],
                'intensity': 'light'
            },
            'Typhoid': {
                'acute_phase': [
                    'Complete Rest - During fever\nInstructions: Bed rest essential\nBenefits: Conserves energy\nPrecautions: Avoid any exertion',
                    'Passive Range of Motion - 5 minutes\nInstructions: Gentle joint movements\nBenefits: Prevents stiffness\nPrecautions: Only if feeling stable'
                ],
                'recovery_phase': [
                    'Short Walks - 10 minutes\nInstructions: Start with indoor walking\nBenefits: Rebuilds strength\nPrecautions: Monitor fatigue',
                    'Light Activities - 15 minutes\nInstructions: Simple household tasks\nBenefits: Improves endurance\nPrecautions: Rest frequently'
                ],
                'intensity': 'very_light'
            },
            'Gastritis': {
                'acute_phase': [
                    'Gentle Walking - 5-10 minutes\nInstructions: Walk after meals\nBenefits: Aids digestion\nPrecautions: Wait 30 minutes after eating',
                    'Deep Breathing - 5 minutes\nInstructions: Focus on relaxed breathing\nBenefits: Reduces stress\nPrecautions: Practice when comfortable'
                ],
                'recovery_phase': [
                    'Regular Walking - 15-20 minutes\nInstructions: Moderate pace walking\nBenefits: Improves digestion\nPrecautions: Not immediately after meals',
                    'Yoga - 15 minutes\nInstructions: Gentle digestive poses\nBenefits: Reduces stress, aids digestion\nPrecautions: Avoid pressure on stomach'
                ],
                'intensity': 'light'
            },
            'Asthma': {
                'acute_phase': [
                    'Pursed Lip Breathing - 5-10 minutes (4-6 times daily)\nInstructions: Inhale through nose, exhale slowly through pursed lips\nBenefits: Improves breathing control\nPrecautions: Stop if wheezing increases',
                    'Diaphragmatic Breathing - 5-10 minutes (3-4 times daily)\nInstructions: Focus on belly breathing\nBenefits: Strengthens breathing muscles\nPrecautions: Use inhaler if needed'
                ],
                'recovery_phase': [
                    'Swimming - 20-30 minutes\nInstructions: Start with gentle strokes in warm water\nBenefits: Improves lung capacity in humid environment\nPrecautions: Indoor pool preferred',
                    'Walking - 15-20 minutes\nInstructions: Gradual pace on flat terrain\nBenefits: Builds cardio endurance\nPrecautions: Avoid cold or polluted air'
                ],
                'intensity': 'light'
            },
            'Hypertension': {
                'acute_phase': [
                    'Gentle Walking - 10-15 minutes (2-3 times daily)\nInstructions: Walk at comfortable pace on level ground\nBenefits: Helps regulate blood pressure\nPrecautions: Monitor BP before and after',
                    'Deep Breathing - 10 minutes (3-4 times daily)\nInstructions: Slow, controlled breathing\nBenefits: Reduces stress and BP\nPrecautions: Sit while exercising'
                ],
                'recovery_phase': [
                    'Brisk Walking - 30 minutes\nInstructions: Moderate pace walking\nBenefits: Improves cardiovascular health\nPrecautions: Check BP regularly',
                    'Swimming - 20-30 minutes\nInstructions: Gentle swimming or water aerobics\nBenefits: Low-impact cardio workout\nPrecautions: Avoid holding breath'
                ],
                'intensity': 'light_to_moderate'
            },
            'Diabetes': {
                'acute_phase': [
                    'Walking - 10-15 minutes (after meals)\nInstructions: Gentle walk post-meals\nBenefits: Helps control blood sugar\nPrecautions: Check glucose levels',
                    'Chair Exercises - 10 minutes\nInstructions: Simple seated movements\nBenefits: Maintains activity while monitoring\nPrecautions: Have sugar source nearby'
                ],
                'recovery_phase': [
                    'Mixed Cardio - 30 minutes\nInstructions: Combine walking, cycling, swimming\nBenefits: Improves insulin sensitivity\nPrecautions: Check glucose before/after',
                    'Resistance Training - 20-30 minutes\nInstructions: Light weights or resistance bands\nBenefits: Helps regulate blood sugar\nPrecautions: Start with supervision'
                ],
                'intensity': 'light_to_moderate'
            },
            'Arthritis': {
                'acute_phase': [
                    'Water Exercises - 15-20 minutes\nInstructions: Gentle movements in warm pool\nBenefits: Reduces joint stress\nPrecautions: Use warm water only',
                    'Isometric Exercises - 10 minutes\nInstructions: Static muscle contractions\nBenefits: Maintains strength without joint movement\nPrecautions: Avoid painful positions'
                ],
                'recovery_phase': [
                    'Low-Impact Cardio - 20-30 minutes\nInstructions: Stationary bike or elliptical\nBenefits: Improves joint mobility\nPrecautions: Adjust resistance carefully',
                    'Strength Training - 15-20 minutes\nInstructions: Light weights with proper form\nBenefits: Builds supporting muscles\nPrecautions: Focus on control'
                ],
                'intensity': 'light'
            },
            'Back Pain': {
                'acute_phase': [
                    'Walking - 5-10 minutes\nInstructions: Short, gentle walks on level ground\nBenefits: Maintains mobility\nPrecautions: Maintain good posture',
                    'Core Breathing - 5-10 minutes\nInstructions: Gentle core engagement with breath\nBenefits: Stabilizes spine\nPrecautions: Avoid straining'
                ],
                'recovery_phase': [
                    'Swimming - 20-30 minutes\nInstructions: Gentle swimming or water walking\nBenefits: Non-weight bearing exercise\nPrecautions: Avoid butterfly stroke',
                    'Core Strengthening - 15-20 minutes\nInstructions: Gentle planks and bridges\nBenefits: Improves spine stability\nPrecautions: Maintain neutral spine'
                ],
                'intensity': 'light'
            },
            'Depression': {
                'acute_phase': [
                    'Morning Walk - 10-15 minutes\nInstructions: Walk in natural light\nBenefits: Exposure to sunlight, mood improvement\nPrecautions: Start with short duration',
                    'Gentle Yoga - 15 minutes\nInstructions: Basic poses with breathing\nBenefits: Reduces stress, improves mood\nPrecautions: No pressure to perform'
                ],
                'recovery_phase': [
                    'Group Exercise - 30-45 minutes\nInstructions: Join group fitness classes\nBenefits: Social interaction, structured activity\nPrecautions: Choose supportive environment',
                    'Mixed Activities - 30 minutes\nInstructions: Combine walking, swimming, cycling\nBenefits: Variety maintains interest\nPrecautions: Progress gradually'
                ],
                'intensity': 'light_to_moderate'
            },
            'Anxiety': {
                'acute_phase': [
                    'Deep Breathing - 10-15 minutes\nInstructions: Focus on slow, controlled breaths\nBenefits: Reduces anxiety, centers mind\nPrecautions: Practice in quiet space',
                    'Walking Meditation - 15 minutes\nInstructions: Mindful walking in nature\nBenefits: Combines exercise and mindfulness\nPrecautions: Choose quiet routes'
                ],
                'recovery_phase': [
                    'Yoga - 30 minutes\nInstructions: Gentle flow with breathing focus\nBenefits: Improves mind-body connection\nPrecautions: Avoid overwhelming classes',
                    'Swimming - 20-30 minutes\nInstructions: Rhythmic swimming\nBenefits: Meditative movement in water\nPrecautions: Start with basic strokes'
                ],
                'intensity': 'light'
            }
        }
        
        # Default recommendations for diseases without specific exercises
        self.default_recommendations = {
            'acute_phase': [
                'Deep Breathing - 5-10 minutes (3-4 times daily)\nInstructions: Gentle breathing exercises\nBenefits: Maintains lung function\nPrecautions: Stop if uncomfortable',
                'Very Light Movement - As tolerated\nInstructions: Basic movements within comfort\nBenefits: Prevents stiffness\nPrecautions: Stop if pain increases'
            ],
            'recovery_phase': [
                'Walking - Start with 5-10 minutes\nInstructions: Begin with short distances\nBenefits: Improves circulation\nPrecautions: Increase gradually',
                'Light Stretching - 5-10 minutes\nInstructions: Basic stretches\nBenefits: Maintains flexibility\nPrecautions: Stay within comfort zone'
            ],
            'intensity': 'very_light'
        }

    def get_recommendations(self, disease, phase='acute_phase', age=None, conditions=None):
        """Get exercise recommendations for a specific disease and phase"""
        
        # Initialize response
        response = {
            'exercises': [],
            'intensity': 'very_light',
            'warnings': [],
            'intensity_guidelines': {}
        }
        
        # Get disease-specific recommendations or default
        disease_recs = self.exercise_recommendations.get(disease, self.default_recommendations)
        
        # Get phase-specific exercises
        if phase in disease_recs:
            exercises = disease_recs[phase]
            response['exercises'] = exercises
            response['intensity'] = disease_recs.get('intensity', 'very_light')
        else:
            exercises = self.default_recommendations[phase]
            response['exercises'] = exercises
            response['intensity'] = 'very_light'
        
        response['intensity_guidelines'] = self.intensity_levels[response['intensity']]
        
        # Add age-specific warnings
        if age:
            if age < 12:
                response['warnings'].append("Children should exercise under adult supervision")
            elif age > 65:
                response['warnings'].append("Elderly individuals should start very gradually and monitor response")
        
        # Add condition-specific warnings
        if conditions:
            for condition in conditions:
                condition_lower = condition.lower()
                if 'heart' in condition_lower:
                    response['warnings'].append("Monitor heart rate closely and stop if any chest pain")
                elif any(x in condition_lower for x in ['lung', 'breath', 'respiratory']):
                    response['warnings'].append("Monitor breathing and use inhaler if prescribed")
        
        return response

    def get_progression_plan(self, disease, weeks=4):
        """Get a progression plan for gradually increasing activity"""
        
        disease_specific_plans = {
            "Pneumonia": [
                "Week 1: Focus on breathing exercises and very short walks",
                "Week 2: Increase walking duration if breathing is comfortable",
                "Week 3: Add light resistance exercises if cleared by doctor",
                "Week 4: Gradually increase intensity based on breathing comfort"
            ],
            "Bronchitis": [
                "Week 1: Focus on breathing exercises and rest",
                "Week 2: Add short walks if breathing is stable",
                "Week 3: Increase walking duration and add gentle stretches",
                "Week 4: Consider adding light cardio if cleared by doctor"
            ],
            "Tuberculosis": [
                "Week 1: Focus on breathing exercises in isolation",
                "Week 2: Add short walks in well-ventilated areas",
                "Week 3: Increase activity duration if feeling stronger",
                "Week 4: Add light resistance exercises if doctor approves"
            ],
            "Dengue": [
                "Week 1: Complete rest and gentle joint movements",
                "Week 2: Start with short walks when fever subsides",
                "Week 3: Gradually increase walking duration",
                "Week 4: Return to normal activities if strength returns"
            ],
            "Typhoid": [
                "Week 1: Strict bed rest and passive movements",
                "Week 2: Begin with sitting activities and short walks",
                "Week 3: Increase walking duration gradually",
                "Week 4: Add light activities as energy improves"
            ],
            "Malaria": [
                "Week 1: Rest during fever cycles, basic movements between episodes",
                "Week 2: Short walks when fever-free",
                "Week 3: Gradually increase activity duration",
                "Week 4: Return to normal activities as strength returns"
            ],
            "Gastritis": [
                "Week 1: Short walks after meals",
                "Week 2: Increase walking duration",
                "Week 3: Add gentle yoga or stretching",
                "Week 4: Return to normal exercise if symptoms improve"
            ],
            "Migraine": [
                "Week 1: Rest during attacks, gentle neck stretches between episodes",
                "Week 2: Add short walks in calm environments",
                "Week 3: Gradually increase activity avoiding triggers",
                "Week 4: Introduce regular light exercise routine"
            ]
        }
        
        if disease in disease_specific_plans:
            return disease_specific_plans[disease]
        
        # Default progression plan
        return [
            "Week 1: Focus on rest and very gentle movement",
            "Week 2: Gradually increase activity duration",
            "Week 3: Add more activities if feeling stronger",
            "Week 4: Return to normal activity if cleared by doctor"
        ] 