import tensorflow as tf
import numpy as np
import score
import pickle


N = 134

loaded_model = tf.keras.models.load_model("ali_model.keras")
# Define the neural network architecture
loaded_model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(2*N,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
# Compile the model
loaded_model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['accuracy'])

x_train = []
y_train = []
x_test = []
y_test = []
#train score=1
for i in range(100000):

    cv = np.random.randint(0, 2, size=N)
    cv1 = cv.tolist()
    jd = np.random.randint(0, 2, size=N)
    jd1 = cv.tolist()
    x_train.append(cv1+jd1)
    sc = score.cosine_similarity(cv1, jd1)
    y_train.append(sc)
# TEST THE MODEL
for i in range(1000):
    jd = np.random.randint(0, 2, size=N)
    cv = np.random.randint(0, 2, size=N)
    jd1 = jd.tolist()
    cv1 = cv.tolist()
    x_test.append(cv1 + jd1)
    sc = score.cosine_similarity(cv1, jd1)
    y_test.append(sc)
    
loaded_model.fit(x_train, y_train, epochs=200, validation_data=(x_test, y_test))



# Evaluate the model
loaded_model.evaluate(x_test, y_test)

# Optionnel : Sauvegarde du modèle mis à jour
loaded_model.save("f_model.keras")

"""
# Save the trained model
with open('trained.model', 'wb') as f:
    pickle.dump(model, f)

# Load the saved model
with open('trained.model', 'rb') as f:
    loaded_model = pickle.load(f)
"""




