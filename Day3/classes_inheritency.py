# -*- coding: utf-8 -*-


class Person:
    # gets fist name and last name of individuals and merge them together
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __str__ (self):
        return (self.firstName +' '+ self.lastName)



class Student(Person):
    # gets the students names and print it together with their subject of study
    def __init__(self,firstName, lastName, subject):
        super().__init__(firstName, lastName)
        self.subject = subject
        
    def printStudentSunject(self):
       print (self.firstName +' '+ self.lastName +','+ self.subject)


        
student = Student ('Fatima','Johari','UBEM')
student.printStudentSunject()



class Teacher(Person):
    # gets teachers names and print it together with their course
    def __init__(self,firstName, lastName, subject):
        super().__init__(firstName, lastName)
        self.subject = subject
        
    def printTeacherCourse(self):
       return print(self.firstName +' '+ self.lastName +','+ self.subject)
   


teacher = Teacher ('Filipe', 'Maia', 'Python')
teacher.printTeacherCourse()       
