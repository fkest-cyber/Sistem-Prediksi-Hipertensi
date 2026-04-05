# Script untuk retrain model hipertensi dengan sklearn 1.3.2
# Mengatasi error AttributeError: Can't get attribute '_RemainderColsList'

import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

# Import preprocessing
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Import model
from sklearn.ensemble import GradientBoostingClassifier

# Import metrics
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score

# Set random seed
np.random.seed(42)

print("="*60)
print("RETRAIN MODEL HIPERTENSI DENGAN SKLEARN 1.3.2")
print("="*60)

# 1. Load data
print("\n1. Loading data...")
df = pd.read_csv('hypertension_dataset.csv')
print(f"✓ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# 2. Define features
numeric_features = ['Age', 'Salt_Intake', 'Stress_Score', 'Sleep_Duration', 'BMI']
categorical_features = ['BP_History', 'Medication', 'Family_History', 'Exercise_Level', 'Smoking_Status']
target = 'Has_Hypertension'

print(f"✓ Numeric features: {numeric_features}")
print(f"✓ Categorical features: {categorical_features}")

# 3. Encode target
print("\n2. Encoding target...")
y = df[target].map({'No': 0, 'Yes': 1})
print(f"✓ Target encoded: {y.value_counts().to_dict()}")

# 4. Split data
X = df.drop(target, axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"✓ Train set: {X_train.shape}, Test set: {X_test.shape}")

# 4. Create preprocessor
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# 5. Create pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', GradientBoostingClassifier(n_estimators=100, random_state=42))
])

# 6. Train model
print("\n2. Training model...")
pipeline.fit(X_train, y_train)
print("✓ Model trained successfully")

# 7. Evaluate
print("\n3. Evaluating model...")
y_pred = pipeline.predict(X_test)
y_pred_proba = pipeline.predict_proba(X_test)[:, 1]

f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)
accuracy = accuracy_score(y_test, y_pred)

print(".4f")
print(".4f")
print(".4f")

# 8. Save model
print("\n4. Saving model...")
with open('model_hipertensi.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("✓ Model saved to model_hipertensi.pkl")

# 9. Save model info
model_info = {
    'model_name': 'GradientBoostingClassifier',
    'f1_score_test': f1,
    'roc_auc_test': roc_auc,
    'accuracy_test': accuracy,
    'numeric_features': numeric_features,
    'categorical_features': categorical_features,
    'sklearn_version': '1.3.2'
}

with open('model_info.pkl', 'wb') as file:
    pickle.dump(model_info, file)

print("✓ Model info saved to model_info.pkl")

print("\n" + "="*60)
print("RETRAINING COMPLETED SUCCESSFULLY!")
print("Model is now compatible with sklearn 1.3.2")
print("="*60)