class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = {}

    def getSalary(self):
        return self.salary

    def addCourse(self, signature, course_name):
        self.courses[signature] = course_name

    def getCourses(self):
        for signature, course in self.courses.items():
            print(signature, course)


class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}

    def attendCourse(self, signature, year):
        self.courses[signature] = {"grades": [], "year": year}

    def addGrade(self, signature, grade):
        if signature in self.courses:
            self.courses[signature]["grades"].append(grade)

    def getCourses(self):
        for signature, info in self.courses.items():
            print(signature, info)

    def getAvgGrade(self, signature):
        if signature in self.courses and self.courses[signature]["grades"]:
            grades = self.courses[signature]["grades"]
            avg = sum(grades) / len(grades)
            return avg
        else:
            return 0

