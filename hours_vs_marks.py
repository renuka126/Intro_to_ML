from sklearn.linear_model import LinearRegression

# Simple data: hours studied vs marks scored
X = [[1], [2], [3], [4], [5]]   # hours studied
y = [35, 45, 50, 65, 75]        # marks scored

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict marks for 6 hours of study
prediction = model.predict([[6]])
print("Predicted marks:", prediction[0])

# A few more predictions at once
for h in [8, 9, 10]:
    print(f"{h} hours -> predicted marks: {model.predict([[h]])[0]:.2f}")