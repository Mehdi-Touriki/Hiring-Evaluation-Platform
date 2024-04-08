import tensorflow as tf
import numpy as np
import score
import pickle


N = 134
# Define the neural network architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(28, activation='relu', input_shape=(2*N,)),
    tf.keras.layers.Dense(28, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
# Compile the model
model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['accuracy'])

x_train = []
y_train = []
x_test = []
y_test = []
#train score=1
for i in range(10000):

    cv = np.random.randint(0, 2, size=N)
    cv1 = cv.tolist()
    x_train.append(cv1+cv1)
    sc = score.cosine_similarity(cv1, cv1)
    y_train.append(sc)
#train score=0
for i in range(10000):
    
    cv = np.random.randint(0, 2, size=N)
    jd= [1 if x == 0 else 0 for x in cv]
    cv1 = cv.tolist()
    x_train.append(cv1+jd)
    sc = score.cosine_similarity(cv1, jd)
    y_train.append(sc)

# train score=0.5
for i in range(10000):
    
    cv = np.random.randint(0, 2, size=N)
    jd= [cv[i] if i < len(cv)/2  else 1 if cv[i] == 0 else 0 for i in range(len(cv))]

    
    cv1 = cv.tolist()
    x_train.append(cv1+jd)
    sc = 0.5
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
    
model.fit(x_train, y_train, epochs=200, validation_data=(x_test, y_test))



# Evaluate the model
model.evaluate(x_test, y_test)


# Save the trained model
with open('trained.model', 'wb') as f:
    pickle.dump(model, f)

# Load the saved model
with open('trained.model', 'rb') as f:
    loaded_model = pickle.load(f)
