import numpy as np
from CV_analyser.static_version import score
num_samples = 1000
# Define the desired output
desired_output = 1/10
# Define the length of the vectors
N = 134
data1 = np.random.randint(0, 2, size=(num_samples, N))
# Generate random binary vector for data2 by flipping some bits in data1
# Flip approximately 10% of the bits to achieve the desired cosine similarity
num_flips = int(N * (1 - desired_output))
flipped_indices = np.random.choice(N, size=num_flips, replace=False)
data2 = np.copy(data1)
data2[:, flipped_indices] = 1 - data2[:, flipped_indices]
# Calculate the cosine similarity between data1 and data2
labels = np.array([score.cosine_similarity(x, y) for x, y in zip(data1, data2)])
print(labels)