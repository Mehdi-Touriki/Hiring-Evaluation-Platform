import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate
from tensorflow.keras.models import Model
from math import sqrt
import CV_analyser.static_version.score as score

model = tf.keras.models.load_model('cosine_similarity_model_me.keras')


# Example input data parameters
N = 134  # Length of input vectors
num_samples = 1000  # Number of samples per iteration
epochs = 1  # Number of epochs per iteration
batch_size = 32  # Batch size


# Training loop for case =1
for i in range(1000):
    data1 = np.random.randint(0, 2, size=(num_samples, N))
    labels = np.array([score.cosine_similarity(x, y) for x, y in zip(data1, data1)])

    # Train the model
    model.fit([data1, data1], labels, epochs=epochs, batch_size=batch_size, verbose=0)

    if i % 100 == 0:
        print("Iteration:", i)

model.save("trained_model_2.keras")
model = tf.keras.models.load_model("trained_model_2.keras")
# Training loop for case =0
for i in range(1000):
    data1 = np.random.randint(0, 2, size=(num_samples, N))
    data3 = []
    for j in range(num_samples):
        data2 = [0 if data1[j][k] else 1 for k in range(134)]
        data3.append(data2)
    data2 = np.array(data3).reshape((num_samples, N))
    labels = np.array([score.cosine_similarity(x, y) for x, y in zip(data1, data2)])

    # Train the model
    model.fit([data1, data2], labels, epochs=epochs, batch_size=batch_size, verbose=0)

    if i % 100 == 0:
        print("Iteration:", i)
# Save the model to a file
model.save("trained_model_3.keras")
