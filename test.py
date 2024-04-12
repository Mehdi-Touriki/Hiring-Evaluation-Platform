import CV_analyser.static_version.extraction as extraction
import CV_analyser.static_version.encoding as encoding
import CV_analyser.static_version.score as score

import os

import tensorflow as tf

# Chargement du modèle existant
model = tf.keras.models.load_model("f_model.keras")
cv1 = extraction.Resume()
jd1_vector = encoding.encoding_jd(
    ['project management', 'communication skills', "python", "java", "django", "mathematica", "html", "opengl",
     "tensorflow"],
    ["undergraduate", "graduate", "ma", "ba"])
directory = 'Sample_cvs/INFORMATION-TECHNOLOGY' 
for i, filename in enumerate(os.listdir(directory)):
    if filename.lower().endswith('.pdf'):
        print("_" * 10)
        print("Candidate Number ", i + 1)
        content = extraction.parse_pdf(directory + '/' + filename)
        cv1.get_data(content)

        print("Name:", cv1.fullname, ", Email:", cv1.email, ", Experience:", cv1.experience)
        print("Score: ", score.cosine_similarity(encoding.encoding_resume(cv1), jd1_vector))
        print("ai score: ",model.predict((encoding.encoding_resume(cv1)+jd1_vector,)))
    
