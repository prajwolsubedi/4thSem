import numpy as np

class NaiveBayesClassifier:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.num_classes = len(self.classes)
        self.num_features = X.shape[1]

        self.priors = np.zeros(self.num_classes)
        self.means = np.zeros((self.num_classes, self.num_features))
        self.variances = np.zeros((self.num_classes, self.num_features))

        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            self.priors[i] = X_c.shape[0] / float(X.shape[0])
            self.means[i] = X_c.mean(axis=0)
            self.variances[i] = X_c.var(axis=0)

    def predict(self, X):
        predictions = []
        for x in X:
            posteriors = []
            for i, c in enumerate(self.classes):
                prior = np.log(self.priors[i])
                likelihood = np.sum(np.log(self.calculate_likelihood(x, i)))
                posterior = prior + likelihood
                posteriors.append(posterior)
            predictions.append(self.classes[np.argmax(posteriors)])
        return predictions

    def calculate_likelihood(self, x, i):
        mean = self.means[i]
        variance = self.variances[i]
        epsilon = 1e-9  # Small epsilon value to avoid numerical instability

        if np.all(variance == 0):
            likelihood = np.where(x == mean, 1.0, epsilon)
        else:
            numerator = np.exp(-(x - mean) ** 2 / (2 * variance + epsilon))
            denominator = np.sqrt(2 * np.pi * variance + epsilon)
            likelihood = numerator / denominator

        return likelihood


# Example usage:

# Create some dummy training data
X_train = np.array([
    [1, 0],
    [1, 0],
    [0, 1],
    [0, 1]
])
y_train = np.array(['B', 'A', 'B', 'A'])

# Create an instance of the Naive Bayes classifier
nb_classifier = NaiveBayesClassifier()

# Train the classifier
nb_classifier.fit(X_train, y_train)

# Create some dummy test data
X_test = np.array([
    [1, 1],
    [0, 0]
])

# Use the classifier to make predictions
predictions = nb_classifier.predict(X_test)

# Print the predictions
for i, prediction in enumerate(predictions):
    print(f"Sample {i+1} predicted class: {prediction}")
