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

cv1 = extraction.Resume()
jd1_vector = encoding.encoding_jd(
    ['project management', 'communication skills', "python", "java", "django", "mathematica", "html", "opengl",
     "tensorflow"],
    ["undergraduate", "graduate", "ma", "ba"])
jd= np.array(jd1_vector)
jd1 = jd.reshape((1, 134))




directory = 'C:\dataextraction\Hiring-Evaluation-Platform\Hiring-Evaluation-Platform\Sample_cvs\INFORMATION-TECHNOLOGY' 
for i, filename in enumerate(os.listdir(directory)):
    if filename.lower().endswith('.pdf'):
        print("_" * 10)
        print("Candidate Number ", i + 1)
        content = extraction.parse_pdf(directory + '/' + filename)
        cv1.get_data(content)
        cv=encoding.encoding_resume(cv1)
        cv2=np.array(cv)
        cv3= cv2.reshape((1, 134))

        
        

        print("Name:", cv1.fullname, ", Email:", cv1.email, ", Experience:", cv1.experience)
        print("Score: ", score.cosine_similarity(encoding.encoding_resume(cv1), jd1_vector))
        print("score ai:",loaded_model.predict([cv3,jd1]))
    break