import CV_analyser.static_version.extraction as extraction
import CV_analyser.static_version.encoding as encoding
import CV_analyser.static_version.score as score
import CV_analyser.static_version.encoding as neural
import os
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# Load the model from the file
loaded_model = load_model("CV_analyser/static_version/trained_model_wadi3_bzf_tl3ilm.keras")
cv1 = extraction.Resume()
jd1_vector = encoding.encoding_jd(
    ['project management', 'communication skills', "python", "java", "django", "mathematica", "html", "opengl",
     "tensorflow"],
    ["undergraduate", "graduate", "ma", "ba"])

directory = 'Sample_cvs/INFORMATION-TECHNOLOGY'
loss = 0
for i, filename in enumerate(os.listdir(directory)):
    if filename.lower().endswith('.pdf'):
        content = extraction.parse_pdf(directory + '/' + filename)
        cv1.get_data(content)
        cv = encoding.encoding_resume(cv1)
        print("Score: ", score.cosine_similarity(cv, jd1_vector))
        data1 = np.array(cv).reshape((1, 134))
        data2 = np.array(jd1_vector).reshape((1, 134))
        ai_score = loaded_model.predict([data1, data2])
        print("score ai:", ai_score)
        loss += pow(score.cosine_similarity(cv, jd1_vector) - ai_score, 2)
        print("loss:", loss)
