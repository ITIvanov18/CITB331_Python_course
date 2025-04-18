from SchoolMember import SchoolMember

class Teacher(SchoolMember):
    def __init__(self, name, age, salary, courses):
        super().__init__(name, age)
        self.salary = salary
        self.courses = {}

    def get_salary(self):
        return self.salary

    def add_course(self, signature, course_name):
        self.courses[signature] = course_name

    def get_courses(self):
        for signature, course_name in self.courses.items():
            print(f"{signature}: {course_name}")


