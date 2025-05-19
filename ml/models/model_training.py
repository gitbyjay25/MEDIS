import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
import joblib
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Define critical conditions that need higher precision
CRITICAL_CONDITIONS = {
    'Heart Attack': ['chest_pain', 'breathlessness', 'sweating', 'vomiting'],
    'Stroke': ['sudden_weakness', 'difficulty_speaking', 'severe_headache'],
    'Pneumonia': ['high_fever', 'cough', 'breathlessness', 'chest_pain']
}

class ModelTraining:
    def __init__(self, cleaned_data_file):
        """Initialize model training with data validation"""
        try:
            self.df = pd.read_csv(cleaned_data_file)
            print(f"Loaded dataset with {len(self.df)} rows and {len(self.df.columns)} columns")
            self.validate_input_data()
        except Exception as e:
            print(f"Error loading dataset: {e}")
            raise
        
    def validate_input_data(self):
        """Validate input data before training"""
        try:
            assert not self.df.isnull().any().any(), "Dataset contains null values"
            assert len(self.df) > 0, "Dataset is empty"
            assert "Disease" in self.df.columns, "Disease column is missing"
            assert "Disease_Encoded" in self.df.columns, "Disease_Encoded column is missing"
            
            print("\nColumns in dataset:")
            print(self.df.columns.tolist())
            
            # Check for class imbalance
            class_counts = self.df["Disease"].value_counts()
            min_samples = class_counts.min()
            if min_samples < 5:
                print(f"\n⚠️ Warning: Some diseases have very few samples (minimum: {min_samples})")
                print("Classes with few samples:")
                print(class_counts[class_counts < 5])
            
            print("\nDisease distribution:")
            print(class_counts)
            
            # Check critical conditions
            for condition in CRITICAL_CONDITIONS:
                if condition not in self.df["Disease"].unique():
                    print(f"\n⚠️ Warning: Critical condition '{condition}' not found in dataset")
                else:
                    condition_samples = len(self.df[self.df["Disease"] == condition])
                    if condition_samples < 10:
                        print(f"⚠️ Warning: Critical condition '{condition}' has only {condition_samples} samples")
                    else:
                        print(f"✅ {condition}: {condition_samples} samples")
        except Exception as e:
            print(f"Error in data validation: {e}")
            raise

    def prepare_data(self):
        """Prepare data for training with feature selection"""
        try:
            # Get all numeric columns except Disease_Encoded
            self.feature_cols = [col for col in self.df.columns 
                               if col not in ["Disease", "Disease_Encoded"] 
                               and not col.startswith("Precaution")]
            
            print(f"\nSelected {len(self.feature_cols)} features for training")
            
            self.X = self.df[self.feature_cols]
            self.y = self.df["Disease_Encoded"]
            
            # Split data with stratification
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                self.X, self.y, test_size=0.2, random_state=42, stratify=self.y
            )
            
            print(f"Training set size: {len(self.X_train)}")
            print(f"Test set size: {len(self.X_test)}")
        except Exception as e:
            print(f"Error in data preparation: {e}")
            raise

    def tune_hyperparameters(self):
        """Perform grid search for hyperparameter tuning"""
        try:
            # Simplified parameter grid for faster training
            param_grid = {
                'n_estimators': [200],  # Reduced options
                'max_depth': [30],      # Fixed value
                'min_samples_split': [5],
                'min_samples_leaf': [2],
                'class_weight': ['balanced'],
                'max_features': ['sqrt']
            }
            
            base_model = RandomForestClassifier(random_state=42)
            grid_search = GridSearchCV(
                estimator=base_model,
                param_grid=param_grid,
                cv=3,  # Reduced cross-validation folds
                n_jobs=-1,
                scoring='accuracy',
                verbose=2
            )
            
            print("\nStarting hyperparameter tuning...")
            grid_search.fit(self.X_train, self.y_train)
            print("\nBest parameters:", grid_search.best_params_)
            print("Best cross-validation score:", grid_search.best_score_)
            
            return grid_search.best_estimator_
        except Exception as e:
            print(f"Error in hyperparameter tuning: {e}")
            raise

    def evaluate_model(self, model):
        """Evaluate model performance with multiple metrics"""
        try:
            # Make predictions
            y_pred = model.predict(self.X_test)
            y_pred_proba = model.predict_proba(self.X_test)
            
            # Calculate metrics
            accuracy = accuracy_score(self.y_test, y_pred)
            
            # Get classification report
            class_report = classification_report(self.y_test, y_pred)
            
            # Calculate ROC AUC score for multiclass
            y_test_bin = label_binarize(self.y_test, classes=np.unique(self.y))
            roc_auc = roc_auc_score(y_test_bin, y_pred_proba, multi_class='ovr')
            
            # Print results
            print(f"\n{'='*50}")
            print(f"Model Evaluation Results:")
            print(f"{'='*50}")
            print(f"Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
            print(f"ROC AUC Score: {roc_auc:.4f}")
            print("\nClassification Report:")
            print(class_report)
            
            # Evaluate critical conditions specifically
            print("\nCritical Conditions Performance:")
            print("="*50)
            label_encoder = joblib.load("models/label_encoder.pkl")
            for condition in CRITICAL_CONDITIONS:
                if condition in label_encoder.classes_:
                    condition_idx = label_encoder.transform([condition])[0]
                    condition_mask = self.y_test == condition_idx
                    if any(condition_mask):
                        condition_acc = accuracy_score(
                            y_true=self.y_test[condition_mask],
                            y_pred=y_pred[condition_mask]
                        )
                        print(f"{condition}:")
                        print(f"  Accuracy: {condition_acc:.4f} ({condition_acc*100:.2f}%)")
                        
                        # Calculate precision and recall for critical symptoms
                        true_positives = sum((self.y_test == condition_idx) & (y_pred == condition_idx))
                        false_positives = sum((self.y_test != condition_idx) & (y_pred == condition_idx))
                        false_negatives = sum((self.y_test == condition_idx) & (y_pred != condition_idx))
                        
                        precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
                        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
                        
                        print(f"  Precision: {precision:.4f}")
                        print(f"  Recall: {recall:.4f}")
            
            # Plot confusion matrix
            plt.figure(figsize=(12, 8))
            cm = confusion_matrix(self.y_test, y_pred)
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
            plt.title('Confusion Matrix')
            plt.ylabel('True Label')
            plt.xlabel('Predicted Label')
            
            # Save plot
            os.makedirs("models/evaluation", exist_ok=True)
            plt.savefig("models/evaluation/confusion_matrix.png")
            plt.close()
            
            # Save feature importances
            feature_imp = pd.DataFrame({
                'feature': self.feature_cols,
                'importance': model.feature_importances_
            }).sort_values('importance', ascending=False)
            
            feature_imp.to_csv("models/evaluation/feature_importances.csv", index=False)
            
            return accuracy, roc_auc
        except Exception as e:
            print(f"Error in model evaluation: {e}")
            raise

    def train_model(self):
        """Train the model with improved process"""
        try:
            print("🔄 Preparing data...")
            self.prepare_data()
            
            print("\n🔍 Tuning hyperparameters...")
            model = self.tune_hyperparameters()
            
            print("\n📊 Training final model...")
            model.fit(self.X_train, self.y_train)
            
            print("\n📈 Evaluating model...")
            accuracy, roc_auc = self.evaluate_model(model)
            
            # Save the model and metadata
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            model_dir = "models"
            os.makedirs(model_dir, exist_ok=True)
            
            # Save model
            model_path = os.path.join(model_dir, "disease_prediction_model.pkl")
            joblib.dump(model, model_path)
            
            # Save model metadata
            metadata = {
                'timestamp': timestamp,
                'accuracy': accuracy,
                'roc_auc': roc_auc,
                'n_features': len(self.feature_cols),
                'n_classes': len(np.unique(self.y)),
                'feature_columns': self.feature_cols,
                'hyperparameters': model.get_params(),
                'critical_conditions': list(CRITICAL_CONDITIONS.keys())
            }
            
            joblib.dump(metadata, os.path.join(model_dir, "model_metadata.pkl"))
            
            print(f"\n✅ Model training completed!")
            print(f"Model and metadata saved in: {model_dir}")
            print(f"Final Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
            print(f"ROC AUC Score: {roc_auc:.4f}")
        except Exception as e:
            print(f"Error in model training: {e}")
            raise

if __name__ == "__main__":
    try:
        data_file = "data/cleaned_diseases.csv"
        if not os.path.exists(data_file):
            print(f"Error: Dataset file {data_file} not found!")
            print("Available files in data directory:")
            for file in os.listdir("data"):
                print(f"- {file}")
            exit(1)
            
        print(f"Starting model training with dataset: {data_file}")
        trainer = ModelTraining(data_file)
        trainer.train_model()
    except Exception as e:
        print(f"Error during model training: {str(e)}")
        raise