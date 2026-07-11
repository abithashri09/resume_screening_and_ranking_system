import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# -----------------------------
# Load cleaned dataset
# -----------------------------
df = pd.read_csv("data/cleaned_resume_data.csv")

# Fill missing values
df = df.fillna("")

# -----------------------------
# Resume Text
# -----------------------------
resume_columns = [
    "career_objective",
    "skills",
    "degree_names",
    "major_field_of_studies",
    "professional_company_names",
    "responsibilities"
]

df["resume_text"] = df[resume_columns].astype(str).agg(" ".join, axis=1)

# -----------------------------
# Job Description Text
# -----------------------------
job_columns = [
    "job_position_name",
    "educationaL_requirements",
    "experiencere_requirement",
    "responsibilities.1",
    "skills_required"
]

df["job_text"] = df[job_columns].astype(str).agg(" ".join, axis=1)

# -----------------------------
# Combined Text
# -----------------------------
df["combined_text"] = df["resume_text"] + " " + df["job_text"]

# -----------------------------
# TF-IDF
# -----------------------------
tfidf = TfidfVectorizer(max_features=5000)

X = tfidf.fit_transform(df["combined_text"])

y = df["matched_score"]

print("Feature Matrix Shape:", X.shape)

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Model
# -----------------------------
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
predictions = model.predict(X_test)

print("\nR2 Score:", r2_score(y_test, predictions))
print("Mean Squared Error:", mean_squared_error(y_test, predictions))

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "models/resume_model.pkl")
joblib.dump(tfidf, "models/tfidf_vectorizer.pkl")

print("\nModel saved successfully!")