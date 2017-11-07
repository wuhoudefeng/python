#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student:
    stu_count = 0
    def __init__(self, stu_no, name, stu_class, male):
        self.stu_no = stu_no
        self.name = name
        self.stu_class = stu_class
        self.male = male
        Student.stu_count += 1
    if self.stu_class=='wl163'
        Student.su_count163+=1
    elif self.stu_class=='wl161'
        Student.su_count161+=1

    def displayStudent(self):
        print "student number:",self.stu_no,"name:",self.name,"class:",self.stu_class,"male:",self.male
    def displayCount(self):
        print "count:%d" % Student.stu_count
 
