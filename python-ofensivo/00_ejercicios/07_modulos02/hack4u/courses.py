class Course:

    def __init__(self, id, name, duration, link):
        self.id = id
        self.name = name
        self.duration = duration
        self.link = link

    def __repr__(self):
        return f"""[i] {self.id} {self.name} 
- Duration: {self.duration} horas
- Link: {self.link}
"""


courses = [
    Course(1, "Introducción a Linux", 15, "https://www.python.org/"),
    Course(2, "Introducción a Python", 25, "https://www.python.org/"),
    Course(3, "Django en profundidad", 55, "https://www.python.org/"),
    Course(4, "Personalización de Linux", 45, "https://www.python.org/"),
]


def list_courses():

    for course in courses:
        print(course)

def search_course_by_name(name):

    for course in courses:
        if course.name == name:
            return course
            break
    else:
        print("No se encontró ningún curso")

