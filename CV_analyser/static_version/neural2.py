import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate
from tensorflow.keras.models import Model
from math import sqrt
import score

N = 134


def create_model(input_shape):
    input1 = Input(shape=(input_shape,))
    input2 = Input(shape=(input_shape,))

    concatenated = Concatenate()([input1, input2])

    dense1 = Dense(64, activation='relu')(concatenated)
    dense2 = Dense(32, activation='relu')(dense1)
    output = Dense(1, activation='sigmoid')(dense2)

    model = Model(inputs=[input1, input2], outputs=output)
    return model


# Create and compile model
model = create_model(N)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# Example input data parameters
N = 134  # Length of input vectors
num_samples = 3  # Number of samples per iteration
epochs = 10  # Number of epochs per iteration
batch_size = 32  # Batch size

## Training loop
for i in range(20000):
    data1 = np.random.randint(0, 2, size=(num_samples, N))
    data2 = np.random.randint(0, 2, size=(num_samples, N))
    labels = np.array([score.cosine_similarity(x, y) for x, y in zip(data1, data2)])

    # Train the model
    model.fit([data1, data2], labels, epochs=epochs, batch_size=batch_size, verbose=0)

    # Case where both input vectors are identical
    data1 = np.random.randint(0, 2, size=(num_samples, N))
    labels = np.array([score.cosine_similarity(x, y) for x, y in zip(data1, data1)])

    # Train the model
    model.fit([data1, data1], labels, epochs=epochs, batch_size=batch_size, verbose=0)

    # Case where input vectors are complements
    data1 = np.random.randint(0, 2, size=(num_samples, N))
    data2 = np.array([[0 if data1[j][k] else 1 for k in range(N)] for j in range(num_samples)])
    labels = np.array([score.cosine_similarity(x, y) for x, y in zip(data1, data2)])
    # Train the model
    model.fit([data1, data1], labels, epochs=epochs, batch_size=batch_size, verbose=0)
    for j in range(10):
        data1 = np.random.randint(0, 2, size=(num_samples, N))
        # Define the desired output
        desired_output = j/10
        # Define the length of the vectors
        N = 134
        # Generate random binary vector for data2 by flipping some bits in data1
        # Flip approximately 10% of the bits to achieve the desired cosine similarity
        num_flips = int(N * (1 - desired_output))
        flipped_indices = np.random.choice(N, size=num_flips, replace=False)
        data2 = np.copy(data1)
        data2[:, flipped_indices] = 1 - data2[:, flipped_indices]
        # Calculate the cosine similarity between data1 and data2
        labels = np.array([score.cosine_similarity(x, y) for x, y in zip(data1, data2)])
        # Train the model
        model.fit([data1, data2], labels, epochs=epochs, batch_size=batch_size, verbose=0)
    if i % 100 == 0:
        print("Iteration:", i)

# Save the model to a file
model.save("trained_model_wadi3_last_hope.keras")
