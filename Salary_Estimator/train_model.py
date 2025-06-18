import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Set seed for reproducibility
np.random.seed(42)

# Create synthetic dataset
n = 300
experience = np.random.randint(0, 21, size=n)

# Clean linear relationship + small noise
salary = 3 + experience * 1.2 + np.random.normal(0, 0.5, size=n)  # Salary in LPA

# Create DataFrame
df = pd.DataFrame({
    'experience': experience,
    'salary': salary.round(2)
})

# Train model
X = df[['experience']]
y = df['salary']

model = LinearRegression()
model.fit(X, y)

# Save model
with open('salary_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as salary_model.pkl")

