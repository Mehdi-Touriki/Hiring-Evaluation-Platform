import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate
from tensorflow.keras.models import Model
from math import sqrt
import CV_analyser.static_version.score as score



   
# Create model
def create_model(input_shape):
    input1 = Input(shape=(input_shape,))
    input2 = Input(shape=(input_shape,))

    concatenated = Concatenate()([input1, input2])

    dense1 = Dense(64, activation='relu')(concatenated)
    dense2 = Dense(32, activation='relu')(dense1)
    output = Dense(1, activation='sigmoid')(dense2)

    model = Model(inputs=[input1, input2], outputs=output)
    return model

# Example input data parameters
N = 134  # Length of input vectors
num_samples = 1000  # Number of samples per iteration
epochs = 1  # Number of epochs per iteration
batch_size = 32  # Batch size

# Create and compile model
model = create_model(N)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Training loop
for i in range(1000):
    # Generate random training data
    data1 = np.random.randint(0, 2, size=(num_samples, N))
    data2 = np.random.randint(0, 2, size=(num_samples, N))
    labels = np.array([score.cosine_similarity(x, y) for x, y in zip(data1, data2)])
    

    # Train the model
    model.fit([data1, data2], labels, epochs=epochs, batch_size=batch_size, verbose=0)

    if i % 100 == 0:
        print("Iteration:", i)

# Save the model to a file
model.save("cosine_similarity_model.keras")