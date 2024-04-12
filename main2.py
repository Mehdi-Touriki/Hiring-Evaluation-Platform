import CV_analyser.static_version.extraction as extraction
import CV_analyser.static_version.encoding as encoding
import CV_analyser.static_version.score as score
import CV_analyser.static_version.encoding as neural
import os
import pickle
import numpy as np

from tensorflow.keras.models import load_model

# Load the model from the file
loaded_model = load_model("cosine_similarity_model.keras")

data1 = np.random.randint(0, 2, size=(2, 134))
data2 = np.random.randint(0, 2, size=(2, 134))

print("score ai:",loaded_model.predict([data1,data2]))
    