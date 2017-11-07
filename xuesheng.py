class Student:
    stuCount = 0
    def __init__(self,name,stu_no,class_no,gender):
        self.name = name
        self.stu_no = stu_no
        self.class_no = class_no
        self.gender = gender
        Student.stuCount += 1
        
    def study(self):
        print"Student can study"
        
    def getStuCount(self):
        return Student.stuCount
    
class primaryStudent(Student):
    primaryStudent=0
    
    def canRecite(self):
        print "Primary Student can recite"
        
    def canOral(self):
        print "Primary Student can oral"
        
class MiddleStudent(Student):
    middleStudent=0
    
    def __init__(self,name,stu_no,class_no,gender):
        self.name = name
        self.stu_no = stu_no
        self.class_no = class_no
        self.gender = gender
        MiddleStudent.middleStudent += 1
        
    def canChenistry(self):
        print "middle Student can Chenistry"
        
    def canPyhics(self):
        print "middle Student can Pyhics"
