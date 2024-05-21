from math import sqrt, pow, acos
from CV_analyser.static_version import extraction, encoding
import PyPDF2
from tensorflow.keras.models import load_model


def cosine_similarity(vector1: list[float], vector2: list[float]) -> float:
    """Returns the cosine of the angle between two vectors."""
    # the cosine similarity between two vectors is the dot product of the two vectors divided by the magnitude of
    # each vector

    dot_product = 0
    magnitude_vector1 = 0
    magnitude_vector2 = 0

    vector1_length = len(vector1)
    vector2_length = len(vector2)

    if vector1_length > vector2_length:
        # fill vector2 with 0s until it is the same length as vector1 (required for dot product)
        vector2 = vector2 + [0] * (vector1_length - vector2_length)
    elif vector2_length > vector1_length:
        # fill vector1 with 0s until it is the same length as vector2 (required for dot product)
        vector1 = vector1 + [0] * (vector2_length - vector1_length)

    # dot product calculation
    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]

    # vector1 magnitude calculation
    for i in range(len(vector1)):
        magnitude_vector1 += pow(vector1[i], 2)

    # vector2 magnitude calculation
    for i in range(len(vector2)):
        magnitude_vector2 += pow(vector2[i], 2)

    # final magnitude calculation
    magnitude = sqrt(magnitude_vector1) * sqrt(magnitude_vector2)

    # return cosine similarity
    try:
        return dot_product / magnitude
    except ZeroDivisionError:
        return 0


def ai_score(model: str, resume_file, job_description: str, category: str) -> float:
    """
    Calculates the score of a resume file given as input with it's corresponding job description and
    category.
    """
    extracted_skills = extraction.extract_skills(job_description, category)
    extracted_education = extraction.extract_education(job_description)
    jd = encoding.encoding_jd(extracted_skills, extracted_education, category)
    resume = extraction.Resume()
    resume.get_data(extraction.parse_pdf(resume_file), category)
    cv = encoding.encoding_resume(resume, category)
    loaded_model = load_model(model)
    return loaded_model.predict([acos(cosine_similarity(cv, jd))])


def static_score(resume_file: str, job_description: str, category: str) -> float:
    resume = extraction.Resume()
    resume.get_data(extraction.parse_pdf(resume_file).lower(), category)
    cv = encoding.encoding_resume(resume, category)
    job_description = job_description.lower()
    extracted_skills = extraction.find_skills(job_description, category)
    extracted_education = extraction.find_education(job_description)
    jd = encoding.encoding_jd(extracted_skills, extracted_education, category)
    return cosine_similarity(cv, jd)
