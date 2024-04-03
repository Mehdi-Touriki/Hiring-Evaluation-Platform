import CV_analyser.static_version.extraction as extraction
import CV_analyser.static_version.encoding as encoding
import CV_analyser.static_version.score as score

with open("resume_test_1.txt", "r", encoding='utf-8') as text:
    content = text.read()
cv1 = extraction.Resume()
jd1_vector = encoding.encoding_jd(["python", "java", "django", "mathematica", "html", "opengl", "tensorflow"],
                                  ["undergraduate"])
cv1.get_data(content)
cv1_vector = encoding.encoding_resume(cv1)
print(cv1.fullname, cv1.email, cv1_vector)
print("score = ", score.cosine_similarity(cv1_vector, jd1_vector))
