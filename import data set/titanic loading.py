import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------
# 1. Load Dataset
# -------------------------------

df = pd.read_csv("titanic.csv")
print("Dataset Loaded Successfully\n")
print(df.head())

# -------------------------------
# 2. Basic Cleaning
# -------------------------------

# Fill numeric missing values with mean
df = df.fillna(df.mean(numeric_only=True))

# Fill categorical missing values with mode
df = df.fillna(df.mode().iloc[0])

# -------------------------------
# 3. Encode Categorical Columns
# -------------------------------

encoder = LabelEncoder()

# Identify object (categorical) columns
cat_cols = df.select_dtypes(include=["object"]).columns

for col in cat_cols:
    df[col] = encoder.fit_transform(df[col])

print("\nData After Encoding:")
print(df.head())

# -------------------------------
# 4. Define Features and Target
# -------------------------------

target = "Survived"   # you can change this if needed

X = df.drop(target, axis=1)
y = df[target]

# -------------------------------
# 5. Train-Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,
    random_state=42
)

print("\nData Split Completed")
print("Training Shape:", X_train.shape)
print("Testing Shape :", X_test.shape)

# -------------------------------
# 6. Model Training
# -------------------------------

model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

print("\nModel Training Completed")

# -------------------------------
# 7. Model Evaluation
# -------------------------------

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
