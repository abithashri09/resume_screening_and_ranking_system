import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("candidates.csv")

# Features and target
X = data[['Skills', 'Experience', 'Education']]
y = data['Score']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# New candidate data
new_candidate = pd.DataFrame({
    'Skills': [8],
    'Experience': [4],
    'Education': [2]
})

# Predict score
predicted_score = model.predict(new_candidate)

print("Predicted Resume Score:", round(predicted_score[0], 2))