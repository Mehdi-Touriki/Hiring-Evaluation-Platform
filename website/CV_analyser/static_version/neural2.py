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
num_samples = 1000  # Number of samples per iteration
epochs = 1  # Number of epochs per iteration
batch_size = 32  # Batch size

## Training loop
for i in range(33333):
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

    if i % 100 == 0:
        print("Iteration:", i)
    # Train the model
    model.fit([data1, data2], labels, epochs=epochs, batch_size=batch_size, verbose=0)

# Save the model to a file
model.save("trained_model_wadi3_bzf_tl3ilm.keras")
