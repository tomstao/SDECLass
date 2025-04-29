class Student:
    grade = {
        "Math" : 0.0,
        "Science" : 0.0,
        "English" : 0.0
    }

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def add_grade(self, subject, grade):
        self.grade[subject] = grade

    def get_average_grade(self):
        sum_grade = 0.0
        for subject in self.grade:
            sum_grade += self.grade[subject]
        return sum_grade/len(self.grade)

student1 = Student("John", 18)

student1.add_grade("Chemistry", 90)
student1.add_grade("Math", 95)
student1.add_grade("English", 87)
student1.add_grade("Science", 93)

print(f"The student {student1.name}'s average grade is {student1.get_average_grade()}.")