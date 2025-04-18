from SchoolMember import SchoolMember

class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = {}

    def enroll_course(self, signature, year):
        if signature not in self.enrolled_courses:
            self.enrolled_courses[signature] = {"year": year, "grades": []}

    def add_grade(self, signature, grade):
        if signature in self.enrolled_courses:
            self.enrolled_courses[signature]["grades"].append(grade)
        else:
            print("This course is not enrolled.")

    def get_courses(self):
        for signature, course_name in self.enrolled_courses.items():
            print(f"{signature}: {course_name}")

    def get_avg_grade(self, signature):
        if signature in self.enrolled_courses:
            return sum(self.enrolled_courses[signature]["grades"]) / len(self.enrolled_courses[signature]["grades"])



