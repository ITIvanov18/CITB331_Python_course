from Teacher import Teacher
from Student import Student

A=Teacher('Andonov',30,3000, {})
print(A.get_salary())

A.add_course('CSCB101','Python')
A.add_course('CITB201','Databases')
A.get_courses()

B=Student('Petrov',21)
B.enroll_course('CSCB101',2013)
B.add_grade('CITB203',6)
B.get_courses()

B.add_grade('CSCB101',3)
B.add_grade('CSCB101',4)
B.get_courses()
print(B.get_avg_grade('CSCB101'))
