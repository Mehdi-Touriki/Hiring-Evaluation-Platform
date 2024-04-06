from datetime import datetime
import spacy
import re
from pypdf import PdfReader

SKILLS = [
    "web scraper", "software testing", "project management", "communication skills", "research assistant",
    "data analysis", "technical design", "problem solving", "scraper api", "assembly", "bash", "c", "c++", "c#",
    "coffeescript", "emacs lisp", "go!", "groovy", "haskell", "java", "javascript", "matlab", "max msp",
    "objective c", "perl", "php", "html", "xml", "css", "bootstrap", "python", "ruby", "sml", "swift", "latex",
    "unity", "unix", "visual basic", "wolfram language", "xquery", "sql", "node.js", "scala", "kdb", "jquery",
    "mongodb", "express.js", "angular.js", "vue.js", "asp.net", "react.js", "hyperledger fabric", "aws cloud",
    "android", "mysql", "couchdb", "microsoft sql server", "oracle", "redis", "postgresql", "orientdb", "mariadb",
    "sqlite", "couchbase", "cassandra", "hadoop", "tensorflow", "firebase", "google api", "developer", "programmer",
    "automation", "planning", "organization", "data scientist", "engineer", "framework", "automation", "crm", "crud",
    "orm", "rest", "laravel", "api", "nodejs", "backend api", "full-stack", "front-end", "graphql", "blazor",
    "xamarin", "collaborate", "spring", "hibernate", "jdbc", "postgis", "machine learning", "deep learning",
    "maven", "apache spark", "gradle", "scrum", "agile", "dom manipulation", "flux", "redux", "restful api",
    "next.js", "blockchain", "typescript", "kanban", "code-splitting", "chunking", "lazy loading", "regression testing",
    "django", "kivy", "flask", "cherrypy", "pyqt", "flutter", "opengl", "mathematica", "asp",
]

EDUCATION = [
    "phd", "ma", "mcom", "msc", "ba", "bachelor", "bcs", "bcom", "undergraduate", "graduate"
]


def find_experience_paragraph(resume_text: str):
    exp_pattern = r"(?s)(?:experience|work history)(?!d)(.*?)(?:Skills|Education|Achievements)"
    matches = re.findall(exp_pattern, resume_text, re.I)
    if len(matches) == 0:
        exp_pattern = r"(?s)(?:experience|work history)(?!d).*"
        matches = re.findall(exp_pattern, resume_text, re.I)
    if len(matches) == 0:
        return [""]
    result = ""
    for match in matches:
        result += match
    result = result.replace("\n", " ")
    print(result)
    matches[0] = result
    return matches


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


def calc_total_months(date: dict) -> int:
    """
    Une fonction qui calcule la durée en mois entre les dates entrées comme dictionnaire :param date: elle peut avoir
    3 formes. Exemples:{"fmonth":"May","fyear":"2001","lmonth":"sept","lyear":"2004"},{"fmonth":"sept",
    "lmonth":"oct"};{"fyear":"2004","lyear":"2005"}

    :return: la durée en mois entre ces deux dates
    """
    current_year = datetime.now().year
    current_month = datetime.now().month
    months_numbers = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dec': '12'
    }
    total = 0
    print(date)
    try:
        if len(date) == 4:

            if date['fmonth'].isnumeric():
                if date['lmonth'] in ["present", "current", "now", "date"]:
                    total += 12 - int(date['fmonth']) + 12 * (
                            current_year - int(date['fyear']) - 1) + current_month
                else:
                    total += 12 - int(date['fmonth']) + 12 * (
                            int(date['lyear']) - int(date['fyear']) - 1) + int(
                        date['lmonth'])
            else:
                if date['lmonth'] in ["present", "current", "now", "date"]:
                    total += 12 - int(months_numbers[date['fmonth'][:3]]) + 12 * (
                            current_year - int(date['fyear']) - 1) + current_month
                else:
                    total += 12 - int(months_numbers[date['fmonth'][:3]]) + 12 * (
                            int(date['lyear']) - int(date['fyear']) - 1) + int(
                        months_numbers[date['lmonth'][:3]])
        elif len(date) == 2:
            if 'fyear' in date and 'lyear' in date:
                if date['lyear'] in ["present", "current", "now", "date"]:
                    date['lyear'] = "2024"
                total += 12 * (int(date['lyear']) - int(date['fyear']))
            elif 'fmonth' in date and 'lmonth' in date:
                if date['lmonth'] == "present":
                    total += 12 - int(months_numbers[date['fmonth'][:3]])
                else:
                    total += int(months_numbers[date['lmonth'][:3]]) - int(months_numbers[date['fmonth'][:3]])
    except KeyError:
        print("There has been an exception while calculating dates in experience paragraph.")
        return 0
    return total


def find_total_months(exp_list: list[str]) -> int:
    """
    Une fonction qui trouve la duree totale dans une liste d'experiences
    :param exp_list:
    :return:
    """
    dates = []
    print(exp_list)
    lines = exp_list[0].split(".")
    print(lines)
    for line in lines:
        line = line.lower()
        # dates in the form 2015 - 2020
        experience = re.search(
            r"(?P<fyear>\d{4})\s*(\s|-|to)\s*(?P<lyear>\d{4}|present|date|now|current)",
            line,
        )
        if experience:
            d = experience.groupdict()
            # exemple d = {"fyear":"2004","lyear":"2005"}
            dates.append(d)
            continue
        # dates in the form (sept - oct [2012])
        experience = re.search(
            r"(?s)\((?P<fmonth>\w+)\s*(-|to)\s*(?P<lmonth>\w+|present|date|now|current).*\)",
            line,
        )
        if experience:
            d = experience.groupdict()
            # exemple d = {"fmonth":"sept","lmonth":"oct"}
            dates.append(d)
            continue
        # dates in the form May 2001 to sept 2004
        experience = re.search(
            r"(?P<fmonth>\w+)\s*/*(?P<fyear>\d+)\s*(-|to)\s*((?P<lmonth>\w+)\s*/*("
            r"?P<lyear>\d+)|present|date|now|current)",
            line,
        )
        if experience:
            d = experience.groupdict()
            # exemple d = {"fmonth":"May","fyear":"2001","lmonth":"sept","lyear":"2004"}
            dates.append(d)
            continue
            # dates in the form 07/2019 to current
        experience = re.search(
            r"(?P<fmonth>\w+)\s*/(?P<fyear>\d+)\s*(-|to)\s*((?P<lmonth>\w+)\s*/("
            r"?P<lyear>\d+)|present|date|now|current)",
            line,
        )
        if experience:
            d = experience.groupdict()
            # exemple d = {"fmonth":"May","fyear":"2001","lmonth":"sept","lyear":"2004"}
            dates.append(d)
            continue
    results = []
    for date in dates:
        total = calc_total_months(date)
        if total > 1200 or total < 0:
            continue
        results.append(calc_total_months(date))

    return sum(results)


class Resume:
    def __init__(self):
        self._nlp = spacy.load("en_core_web_sm")
        self.fullname = ""
        self.email = ""
        self.phone_number = ""
        self.experience = 0
        self.skills = []
        self.education = []

    def get_data(self, resume_text: str):
        """
        Extraction de touts les données souhaitées
        :param resume_text:
        """
        self.fullname = self.find_name(resume_text)
        self.email = self.find_email(resume_text)
        self.experience = self.find_experience(resume_text)
        self.skills = self.find_skills(resume_text)
        self.education = self.find_education(resume_text)
        self.phone_number = self.find_phone_number(resume_text)

    def find_name(self, resume_text: str) -> str:
        """
        :param resume_text: un CV en format string
        :return: un string contenant le nom complet du candidat dans le CV
        """
        doc = self._nlp(resume_text)
        name = ""
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                name = str(ent.text)
                break
        return name

    def find_email(self, resume_text: str) -> str:
        """

        :param resume_text:
        :return:
        """
        doc = self._nlp(resume_text)
        email = ""
        for token in doc:
            if token.like_email:
                email = token
                break
        return email

    def find_experience(self, resume_text: str) -> int:
        # get experience paragraph
        matches = find_experience_paragraph(resume_text)
        return find_total_months(matches)

    def find_skills(self, resume_text: str) -> list[str]:
        """

        :param resume_text: une chaine de caractères contenant le CV
        :return:
        """
        skills = []
        for skill in SKILLS:
            if skill in resume_text.lower():
                skills.append(skill)
        return skills

    def find_education(self, resume_text: str) -> list[str]:
        """
        :param resume_text:
        :return:
        """
        education = []
        for edu in EDUCATION:
            if edu in resume_text.lower():
                education.append(edu)
        return education

    def find_phone_number(self, resume_text: str) -> str:
        doc = self._nlp(resume_text)
        phone = ""
        for token in doc:
            if token.like_num:
                phone = token
        return phone
