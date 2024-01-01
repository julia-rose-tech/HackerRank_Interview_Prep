# You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Observe that Student inherits all the properties of Person.

# A Student class constructor, has  parameters:
# A string, .
# A string, .
# An integer, .
# An integer array (or vector) of test scores, .
# A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

# Sample Input:
# Heraldo Memelli 8135627
# 2
# 100 80

# Sample Output: 

#  Name: Memelli, Heraldo
#  ID: 8135627
#  Grade: O

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber,)
        self.scores = scores

    def calculate(self):
        score_total = sum(scores)
        score_average = score_total / len(scores)

         
        if 90 <= score_average <= 100:
            grade_char = 'O'
        elif 80 <= score_average < 90:
            grade_char = 'E'
        elif 70 <= score_average < 80:
            grade_char = 'A'
        elif 55 <= score_average < 70:
            grade_char = 'P'
        elif 40 <= score_average < 55:
            grade_char = 'D'
        elif score_average < 40:
            grade_char = 'T'
        else:
            grade_char = "Error"
       
        return (grade_char)


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())