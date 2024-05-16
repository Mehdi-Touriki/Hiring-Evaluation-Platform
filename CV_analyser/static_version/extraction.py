from pypdf import PdfReader
from CV_analyser.static_version.skills import SKILLS
from CV_analyser.static_version.experience import *
EDUCATION = [
    "phd", "ma", "mcom", "msc", "ba", "bachelor", "bcs", "bcom", "undergraduate", "graduate"
]
def parse_pdf(path: str) -> str:
    """
    Une fonction pour convertir un CV au format pdf en string
    :param path: le chemin du fichier pdf
    :return: le contenu du fichier pdf
    """
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    text_utf8 = text.encode('utf-8')
    text_utf8_string = text_utf8.decode('utf-8')
    return text_utf8_string


def find_experience(resume_text: str) -> int:
    # get experience paragraph
    matches = find_experience_paragraph(resume_text)
    return find_total_months(matches)


def find_skills(resume_text: str, category: str) -> list[str]:
    """
    Finds all the skills in a string of text associated with a certain category and returns the list of skills as a list of strings.
    :param resume_text: une chaine de caractères contenant le CV.
    :param category: une chaine de caractères contenant la categorie du CV.
    :return: skills: une liste de chaine de caractères contenant les compétences du CV.
    """
    skills = []
    for skill in SKILLS[category]:
        if skill in resume_text.lower():
            skills.append(skill)
    return skills


def find_education(resume_text: str) -> list[str]:
    """
    :param resume_text:
    :return:
    """
    education = []
    for edu in EDUCATION:
        if edu in resume_text.lower():
            education.append(edu)
    return education


class Resume:
    def __init__(self):
        self.experience = 0
        self.skills = []
        self.education = []

    def get_data(self, resume_text: str, category: str):
        """
        Extraction de toutes les données souhaitées
        :param resume_text:
        :param category:
        """
        self.experience = find_experience(resume_text)
        self.skills = find_skills(resume_text, category)
        self.education = find_education(resume_text)

