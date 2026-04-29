import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load CSV dataset
data = pd.read_csv("student_performance.csv")

# Independent and dependent variables
X = data[['Marks']].values
y = data['GradePoint'].values

# Polynomial features (degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_poly, y)

# Smooth curve for plotting
x_range = np.linspace(X.min(), X.max(), 500).reshape(-1,1)
x_poly_range = poly.transform(x_range)
y_pred = model.predict(x_poly_range)

# Plot original data
plt.scatter(X, y, color='blue', label='Actual Data')

# Plot polynomial regression curve
plt.plot(x_range, y_pred, color='red',
         label='Polynomial Regression Curve')

plt.title('Polynomial Regression on Student Performance')
plt.xlabel('Marks')
plt.ylabel('Grade Point')
plt.legend()
plt.grid(True)
plt.show()

# Print equation coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)