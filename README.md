# Hiring Evaluation Platform Driven by AI

### Introduction:
#### Context and Problem Definition:
In an ever-evolving job market where companies are inundated with applications for every vacant position, the use of technological tools to facilitate the recruitment process has become indispensable. In this context, a web application dedicated to assisting in CV filtering emerges as a promising solution. Thanks to advances in artificial intelligence and natural language processing, this application offers recruiters the ability to automate part of the CV sorting process by analyzing their content semantically, comparing them to the job requirements, and ranking candidates based on their relevance. This approach not only saves valuable time but also improves the quality of selected candidates while ensuring the security and confidentiality of personal data.

### The Solution:
This web application is divided into two distinct interfaces to meet the needs of the two main actors in the recruitment process: recruiters and candidates. On the recruiters' side, the application allows them to post job offers by describing available positions and their requirements. At the end of the process, they receive a list of candidates automatically sorted based on the match between their CV and the job description. On the other hand, candidates use the application to apply by uploading their CVs and responding to available job offers. By simplifying communication between the two parties and automating the application filtering process, the application makes the recruitment process more efficient and transparent for everyone involved.

### Objective:
The main objective of this web application is to simplify and optimize the recruitment process for both recruiters and candidates. For recruiters, it aims to reduce the time spent manually sorting CVs by providing them with a pre-sorted list of candidates that best match the job requirements. This allows them to identify relevant profiles more quickly and spend more time evaluating the most promising candidates. For candidates, the application offers a user-friendly platform to apply for job offers by uploading their CVs, thus facilitating access to professional opportunities that match their skills and aspirations.

### Technical Requirements:
#### Web Application (Platform):
- UML Diagram

#### Platform Functionality Description:
- **The Visitor:** A site visitor has the option to register as either a candidate or a recruiter. Additionally, they can view the latest job offers published, providing an overview of available opportunities. However, it should be noted that comprehensive details are only accessible after registration. Furthermore, the visitor has the option to explore companies that have already used our platform to advertise job offers, allowing them to understand potential employers.
- **The Candidate:** The candidate's page offers an intuitive and comprehensive experience for job searching and application. The candidate has access to a search engine that allows them to filter job offers. Each job offer is presented clearly and concisely, providing essential offer information. Once a suitable job offer is found, the candidate can apply directly by submitting their CV.
- **The Recruiter:** The recruiter has the ability to publish new job offers by filling out an intuitive form defining specific criteria for the position, such as required skills and desired experience levels. Once published, job offers are automatically analyzed and classified by our AI system. Recruiters can use this feature to filter and sort applications based on predefined criteria, allowing them to quickly find the most relevant candidates for the position. Additionally, the recruiter can track the current status of these offers.

#### Technical Requirements:
- **Front-end:** HTML5, CSS, and JS
- **Back-end:** DJANGO-PYTHON

#### CV Analysis:
For this section, two approaches are proposed:
1. **Static Approach:**
   - **CV Conversion:** Using the PdfReader module of the PyPDF library to convert the CV into a Python string.
   - **Data Extraction:** Using SpaCy, a natural language processing library, relevant data from the CV is extracted: name, email address, phone number, experiences, skills, and education. It is then checked whether the candidate has sufficient experience to be considered. Otherwise, their CV is rejected.
   - **Encoding:** A predefined set of skills (and education) is defined to convert CV data into a fixed-size vector. Each value in the vector is associated with a specific skill (or education). This value is set to 1 if the CV contains that skill and 0 otherwise. The same operation is performed for the job description published by the recruiter.
   - **Classification:** The correlation coefficient between the job description and each CV is calculated. This score is used to classify candidates, selecting those whose score is above average.
2. **Dynamic Approach:**
   - An ANN(artificial neural network) was trained.
   - **Comparison of Results and Conclusion:** The results are then compared, and a conclusion is drawn.
