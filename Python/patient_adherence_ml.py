import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("adherence_flat.csv")

# Dataset Shape
print("="*60)
print("DATASET SHAPE")
print("="*60)
print(df.shape)

# First 5 Rows
print("\n"+"="*60)
print("FIRST 5 ROWS")
print("="*60)
print(df.head())

# Column Names
print("\n"+"="*60)
print("COLUMN NAMES")
print("="*60)
print(df.columns.tolist())

# Data Types
print("\n"+"="*60)
print("DATA TYPES")
print("="*60)
df.info()

# Missing Values
print("\n"+"="*60)
print("MISSING VALUES")
print("="*60)
print(df.isnull().sum())

# Target Variable
print("\n"+"="*60)
print("TARGET VARIABLE")
print("="*60)
print(df["dropped_off"].value_counts())

from sklearn.preprocessing import LabelEncoder

# Create a copy of the dataset
ml_df = df.copy()

# Remove ID columns (they don't help prediction)
ml_df = ml_df.drop(columns=[
    'prescription_id',
    'patient_id',
    'doctor_id',
    'prescription_start_date',
    'last_fill_date'
])

# Convert text columns into numbers
encoder = LabelEncoder()

for column in ml_df.select_dtypes(include='object').columns:
    ml_df[column] = encoder.fit_transform(ml_df[column])

print("="*60)
print("ENCODED DATASET")
print("="*60)
print(ml_df.head())


from sklearn.preprocessing import LabelEncoder

# Make a copy of dataset
ml_df = df.copy()

# Remove columns that should not be used for prediction
ml_df.drop(columns=[
    "prescription_id",
    "patient_id",
    "doctor_id",
    "prescription_start_date",
    "last_fill_date"
], inplace=True)

# Convert all text columns into numbers
encoder = LabelEncoder()

for col in ml_df.select_dtypes(include="object").columns:
    ml_df[col] = encoder.fit_transform(ml_df[col])

print("\n================ ML DATASET =================")
print(ml_df.head())

print("\nShape after preprocessing:")
print(ml_df.shape)



from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ----------------------------
# Split Features and Target
# ----------------------------

X = ml_df.drop("dropped_off", axis=1)
y = ml_df["dropped_off"]

# ----------------------------
# Split Training & Testing Data
# ----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# ----------------------------
# Train Random Forest Model
# ----------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ----------------------------
# Make Predictions
# ----------------------------

y_pred = model.predict(X_test)

# ----------------------------
# Evaluate Model
# ----------------------------

print("\n==============================")
print("MODEL ACCURACY")
print("==============================")

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy : {accuracy:.2%}")

print("\n==============================")
print("CONFUSION MATRIX")
print("==============================")

print(confusion_matrix(y_test, y_pred))

print("\n==============================")
print("CLASSIFICATION REPORT")
print("==============================")

print(classification_report(y_test, y_pred))


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ----------------------------------------
# Features (X) and Target (y)
# ----------------------------------------

X = ml_df.drop("dropped_off", axis=1)
y = ml_df["dropped_off"]

# ----------------------------------------
# Split Data
# ----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape :", X_test.shape)

# ----------------------------------------
# Create Model
# ----------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train Model
model.fit(X_train, y_train)

# ----------------------------------------
# Prediction
# ----------------------------------------

y_pred = model.predict(X_test)

# ----------------------------------------
# Accuracy
# ----------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n===================================")
print("MODEL ACCURACY")
print("===================================")

print("Accuracy :", accuracy)

print("\n===================================")
print("CONFUSION MATRIX")
print("===================================")

print(confusion_matrix(y_test, y_pred))

print("\n===================================")
print("CLASSIFICATION REPORT")
print("===================================")

print(classification_report(y_test, y_pred))


# ===========================================
# Feature Importance
# ===========================================

importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
})

importance = importance.sort_values(
    by='Importance',
    ascending=False
)

print("\n=======================================")
print("TOP 10 IMPORTANT FEATURES")
print("=======================================\n")

print(importance.head(10))

# ===========================================
# Export Predictions for Power BI
# ===========================================

predictions = X_test.copy()

predictions["Actual_Dropoff"] = y_test.values
predictions["Predicted_Dropoff"] = y_pred

predictions.to_csv("patient_predictions.csv", index=False)

print("\n==========================================")
print("Prediction file exported successfully!")
print("File Name : patient_predictions.csv")
print("==========================================")

# ===========================================
# Export Predictions
# ===========================================

predictions = X_test.copy()

predictions["Actual_Dropoff"] = y_test.values
predictions["Predicted_Dropoff"] = y_pred

predictions.to_csv("patient_predictions.csv", index=False)

print("\n==========================================")
print("Predictions exported successfully!")
print("File created: patient_predictions.csv")
print("==========================================")