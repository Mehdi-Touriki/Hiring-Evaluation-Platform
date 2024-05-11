import numpy as np
import tensorflow as tf
import math
# Generate training data
angles = np.random.uniform(low=0, high=2*np.pi, size=1000)  # Random angles between 0 and 2*pi
cosine_values = np.cos(angles)  # Cosine values of the angles

# Define the model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(angles, cosine_values, epochs=500, batch_size=32)


# Test angles
test_angles = [np.pi / 4, np.pi / 3, np.pi / 6, np.pi / 2, np.pi, 3*np.pi / 2]

for angle in test_angles:
    predicted_cosine = model.predict([angle])
    print("Predicted cosine of", angle, "is:", predicted_cosine[0][0])
    print("Real cosine of", angle, "is:", math.cos(angle))

model.save('neural_network_1layer_2.keras')