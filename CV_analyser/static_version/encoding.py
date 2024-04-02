from extraction import Resume

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
concatenated_list = SKILLS + EDUCATION

def encoding(cv: Resume)-> list[int]:
    encoded_vector = []
    for j in range(len(concatenated_list)):
        encoded_vector.append(0)
    
    for i, item in enumerate(concatenated_list):
        if item.lower() in cv.skills or item.lower() in cv.education:
            encoded_vector[i] = 1
    return encoded_vector




job_description = " graduate  studied flutter experience (july to sept)"
gd=Resume()
gd.get_data(job_description)
job_encoded_vector = encoding(gd)
print("Encoded job description vector:", job_encoded_vector)


