import spacy
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
    "django", "kivy", "flask", "cherrypy", "pyqt", "flutter"
]

EDUCATION = [
    "phd", "ma", "mcom", "msc", "ba", "bachelor", "bcs", "bcom", "undergraduate", "graduate"
]


class Resume:
    def __init__(self):
        self._nlp = spacy.load("en_core_web_lg")
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
        # regular expression
        pass

    def find_skills(self, resume_text: str) -> list[str]:
        """

        :param resume_text: une chaine de caractères contenant le CV
        :return:
        """
        skills = []
        for skill in SKILLS:
            if skill in resume_text:
                skills.append(skill)
        return skills

    def find_education(self, resume_text: str) -> list[str]:
        """

        :param resume_text:
        :return:
        """
        education = []
        for edu in EDUCATION:
            if edu in resume_text:
                education.append(edu)
        return education

    def find_phone_number(self, resume_text: str):
        doc = self._nlp(resume_text)
        phone = ""
        for token in doc:
            if token.like_num:
                phone = token
        return phone
