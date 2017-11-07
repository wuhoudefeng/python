Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: C:/Python27/xuesheng.py ======================
>>> s = Student('st','11','154','male')
>>> s.study()
Student can study
>>> s.getStuCount

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s.getStuCount
AttributeError: Student instance has no attribute 'getStuCount'
>>> 
====================== RESTART: C:/Python27/xuesheng.py ======================
>>> 
====================== RESTART: C:/Python27/xuesheng.py ======================
>>> s = Student('st','11','154','male')
>>> s.getStuCount()
1
>>> s = Student('st1','121','1543','female')
>>> s.getStuCount()
2
>>> p=PrimaryStudent('p1','22','123','male')

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    p=PrimaryStudent('p1','22','123','male')
NameError: name 'PrimaryStudent' is not defined
>>> p=primaryStudent('p1','22','123','male')
>>> p.canRecite()
Primary Student can recite
>>> p.study()
Student can study
>>> p.name
'p1'
>>> m=MiddleStudent('m1','32','153','female')
>>> m.getStuCount()
3
>>> p.getStuCount()
3
>>> 
