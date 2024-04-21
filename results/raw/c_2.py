import numpy as np

class LogisticRegressionManual:
    def __init__(self, lr=0.01, n_iter=1000):
        self.lr = lr
        self.n_iter = n_iter
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Gradient descent
        for _ in range(self.n_iter):
            model = np.dot(X, self.weights) + self.bias
            predicted = self._sigmoid(model)
            
            dw = (1 / n_samples) * np.dot(X.T, (predicted - y))
            db = (1 / n_samples) * np.sum(predicted - y)
            
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        model = np.dot(X, self.weights) + self.bias
        predicted = self._sigmoid(model)
        return [1 if i > 0.5 else 0 for i in predicted]
    
    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

# Example data
X = np.array([[0.50, 0.20], 
              [0.75, 0.34], 
              [1.00, 0.45], 
              [1.25, 0.50], 
              [1.50, 0.55],
              [1.75, 0.70], 
              [2.00, 0.85], 
              [2.25, 0.90], 
              [2.50, 0.95]])
y = np.array([0, 0, 0, 0, 1, 0, 1, 1, 1])

# Logistic Regression Model
model = LogisticRegressionManual(lr=0.1, n_iter=1000)
model.fit(X, y)
predictions = model.predict(X)

print("Predictions:", predictions)

# ************* Module c_2
# results/raw/c_2.py:5:8: C0103: Attribute name "lr" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_2.py:4:23: C0103: Argument name "lr" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_2.py:10:18: C0103: Argument name "X" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_2.py:10:21: C0103: Argument name "y" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_2.py:10:18: W0621: Redefining name 'X' from outer scope (line 35) (redefined-outer-name)
# results/raw/c_2.py:10:21: W0621: Redefining name 'y' from outer scope (line 44) (redefined-outer-name)
# results/raw/c_2.py:17:12: W0621: Redefining name 'model' from outer scope (line 47) (redefined-outer-name)
# results/raw/c_2.py:20:12: C0103: Variable name "dw" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_2.py:21:12: C0103: Variable name "db" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_2.py:26:22: C0103: Argument name "X" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_2.py:26:22: W0621: Redefining name 'X' from outer scope (line 35) (redefined-outer-name)
# results/raw/c_2.py:27:8: W0621: Redefining name 'model' from outer scope (line 47) (redefined-outer-name)
# results/raw/c_2.py:31:23: C0103: Argument name "z" doesn't conform to snake_case naming style (invalid-name)
# ------------------------------------------------------------------
# Your code has been rated at 5.67/10 (previous run: 8.18/10, -2.52)