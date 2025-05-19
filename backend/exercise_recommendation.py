class ExerciseRecommender:
    def __init__(self):
        self.exercise_recommendations = {
            'Common Cold': [
                'Light walking - 15-20 minutes daily',
                'Gentle stretching',
                'Deep breathing exercises'
            ],
            'Flu': [
                'Rest until fever subsides',
                'Gentle stretching when recovering',
                'Short walks during recovery'
            ],
            'Migraine': [
                'Neck stretches',
                'Shoulder rolls',
                'Light yoga (avoid inversions)',
                'Walking in fresh air when pain-free'
            ],
            'Asthma': [
                'Swimming (in controlled environment)',
                'Walking',
                'Stationary cycling',
                'Breathing exercises',
                'Yoga with focus on breathing'
            ],
            'Hypertension': [
                'Brisk walking - 30 minutes daily',
                'Light jogging',
                'Swimming',
                'Stationary cycling',
                'Low-impact aerobics'
            ],
            'Diabetes Type 2': [
                'Walking - 30 minutes daily',
                'Swimming',
                'Resistance band exercises',
                'Stationary cycling',
                'Light weight training'
            ],
            'Arthritis': [
                'Water aerobics',
                'Gentle swimming',
                'Tai Chi',
                'Range-of-motion exercises',
                'Stationary cycling'
            ],
            'Depression': [
                'Brisk walking',
                'Jogging',
                'Group exercise classes',
                'Yoga',
                'Dancing'
            ],
            'Anxiety': [
                'Walking in nature',
                'Yoga',
                'Tai Chi',
                'Deep breathing exercises',
                'Swimming'
            ],
            'Osteoporosis': [
                'Weight-bearing exercises',
                'Walking',
                'Low-impact aerobics',
                'Resistance training',
                'Balance exercises'
            ],
            'Fibromyalgia': [
                'Water exercises',
                'Gentle stretching',
                'Walking',
                'Tai Chi',
                'Light yoga'
            ],
            'Back Pain': [
                'Core strengthening exercises',
                'Swimming',
                'Walking',
                'Gentle stretching',
                'Yoga (with professional guidance)'
            ],
            'Obesity': [
                'Walking - start with 10 minutes',
                'Swimming',
                'Water aerobics',
                'Stationary cycling',
                'Resistance training'
            ]
        }
        
        # Default exercises for conditions without specific recommendations
        self.default_exercises = [
            'Gentle walking as tolerated',
            'Light stretching if appropriate',
            'Deep breathing exercises',
            'Consult with healthcare provider for specific recommendations'
        ]
        
    def get_recommendations(self, disease, age=None, physical_limitations=None):
        """Get exercise recommendations for a specific disease"""
        
        if disease in self.exercise_recommendations:
            exercises = self.exercise_recommendations[disease]
        else:
            exercises = self.default_exercises
            
        # Add safety warning
        exercises.append('Note: Always start slowly and stop if you experience pain or discomfort')
        exercises.append('Consult your healthcare provider before starting any exercise program')
        
        return exercises 