from CV_analyser.static_version.extraction import Resume
from CV_analyser.static_version.extraction import SKILLS, EDUCATION


def encoding_jd(job_skills: list[str], job_education: list[str], category: str) -> list[int]:
    encoded_vector = []
    concatenated_list = SKILLS[category] + EDUCATION
    job_skills = [job.lower() for job in job_skills]
    job_education = [job.lower() for job in job_education]
    for j in range(len(concatenated_list)):
        encoded_vector.append(0)

    for i, item in enumerate(concatenated_list):
        if item.lower() in job_skills or item.lower() in job_education:
            encoded_vector[i] = 1
    return encoded_vector


def encoding_resume(cv: Resume, category) -> list[int]:
    encoded_vector = []
    concatenated_list = SKILLS[category] + EDUCATION
    for j in range(len(concatenated_list)):
        encoded_vector.append(0)

    for i, item in enumerate(concatenated_list):
        if item.lower() in cv.skills or item.lower() in cv.education:
            encoded_vector[i] = 1
    return encoded_vector


if __name__ == '__main__':
    job_description = " graduate  studied flutter experience (july to sept)"
    gd = Resume()
    gd.get_data(job_description, 'Information and Technology')
    job_encoded_vector = encoding_resume(gd, 'Information and Technology')
    print("Encoded job description vector:", job_encoded_vector)
