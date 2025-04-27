from F115436_L7_T1 import Teacher, Student


teacher = Teacher('Andonov', 30, 3000)
print("Teacher's salary:", teacher.getSalary())
teacher.addCourse('CS101', 'Introduction to Python')
teacher.addCourse('CS102', 'Algorithms')
print("Courses for the teacher:")
teacher.getCourses()



student = Student('Petrov', 21)
student.attendCourse('CS101', 2023)
student.addGrade('CS101', 5)
student.addGrade('CS101', 4)
print("Courses attended by the student:")
student.getCourses()
print("Average grade on CS101:", student.getAvgGrade('CS101'))