import numpy as np

class LogisticRegressionManual:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def fit(self, features, labels):
        num_samples, num_features = features.shape
        self.weights = np.zeros(num_features)
        self.bias = 0

        # Gradient descent
        for _ in range(self.num_iterations):
            linear_model = np.dot(features, self.weights) + self.bias
            predicted_labels = self._sigmoid(linear_model)
            
            gradient_w = (1 / num_samples) * np.dot(features.T, (predicted_labels - labels))
            gradient_b = (1 / num_samples) * np.sum(predicted_labels - labels)
            
            self.weights -= self.learning_rate * gradient_w
            self.bias -= self.learning_rate * gradient_b

    def predict(self, features):
        linear_model = np.dot(features, self.weights) + self.bias
        predicted_labels = self._sigmoid(linear_model)
        return [1 if i > 0.5 else 0 for i in predicted_labels]
    
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

# Example usage
features = np.array([
    [0.50, 0.20], [0.75, 0.34], [1.00, 0.45],
    [1.25, 0.50], [1.50, 0.55], [1.75, 0.70],
    [2.00, 0.85], [2.25, 0.90], [2.50, 0.95]
])
labels = np.array([0, 0, 0, 0, 1, 0, 1, 1, 1])

# Create a Logistic Regression Model
model = LogisticRegressionManual(learning_rate=0.1, num_iterations=1000)
model.fit(features, labels)
predictions = model.predict(features)

print("Predictions:", predictions)

# ************* Module c_2
# results/optimized/c_2.py:10:18: W0621: Redefining name 'features' from outer scope (line 35) (redefined-outer-name)
# results/optimized/c_2.py:10:28: W0621: Redefining name 'labels' from outer scope (line 40) (redefined-outer-name)
# results/optimized/c_2.py:26:22: W0621: Redefining name 'features' from outer scope (line 35) (redefined-outer-name)
# results/optimized/c_2.py:31:23: C0103: Argument name "x" doesn't conform to snake_case naming style (invalid-name)
# ------------------------------------------------------------------
# Your code has been rated at 8.67/10 (previous run: 5.67/10, +3.00)