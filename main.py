import CV_analyser.static_version.extraction as extraction
import CV_analyser.static_version.encoding as encoding
import CV_analyser.static_version.score as score
import os

cv1 = extraction.Resume()
jd1_vector = encoding.encoding_jd(
    ['project management', 'communication skills', "python", "java", "django", "mathematica", "html", "opengl",
     "tensorflow"],
    ["undergraduate", "graduate", "ma", "ba"])
directory = 'Sample_cvs/INFORMATION-TECHNOLOGY'
for i, filename in enumerate(os.listdir(directory)):
    if filename.lower().endswith('.pdf'):
        content = extraction.parse_pdf(directory + '/' + filename)
        cv1.get_data(content)
        if cv1.experience == 0:
            continue
        print("_" * 10)
        print("Candidate Number ", i + 1)
        print("Name:", cv1.fullname, ", Email:", cv1.email, ", Experience:", cv1.experience)
        print("Score: ", score.cosine_similarity(encoding.encoding_resume(cv1), jd1_vector))
