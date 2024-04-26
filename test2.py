import os
import pickle
from CV_analyser.static_version.score import cosine_similarity
import numpy as np
from tensorflow.keras.models import load_model

loaded_model = load_model("CV_analyser/static_version/trained_model_wadi3_bzf_tl3ilm.keras")
for i in range(100):
    data1 = np.random.randint(0, 2, size=(134,))
    data2 = np.random.randint(0, 2, size=(134,))
    data3 = [data1[i] if i > 66 else 0 if data1[i] else 1 for i in range(134)]
    print("score static: ", cosine_similarity(data1.tolist(), data1))
    data3 = np.array(data3).reshape((1, 134))
    data1 = data1.reshape((1, 134))
    data2 = data2.reshape((1, 134))
    print("score ai:", loaded_model.predict([data1, data2]))
