Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> line = "Cats are smarter than dogs"
>>> line
'Cats are smarter than dogs'
>>> import re
>>> re.match(r'dogs',line,re.M|re.I)
>>> re.match(r'Cats',line,re.M|re.I)
<_sre.SRE_Match object at 0x015FA988>
>>> matchObje = re.match(r'Cats',line,re.M|re.I)
>>> matchObje.group()
'Cats'
>>> matchObj = re.match(r'dogs',line,re.M|re.I)
>>> print matchObj.group()

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print matchObj.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>>  matchObje = re.match(r'dogs',line,re.M|re.I)
 
  File "<pyshell#9>", line 2
    matchObje = re.match(r'dogs',line,re.M|re.I)
    ^
IndentationError: unexpected indent
>>> matchObj = re.search(r'dogs',line,re.M|re.I)
>>> print matchObj.group()
dogs
>>> matchObj = re.search(r'Dogs',line,re.M|re.I)
>>> print matchObj.group()
dogs
>>> matchObj
<_sre.SRE_Match object at 0x01FA6218>
>>> line = "Cats are smarter than dogs"
>>> matchObj = re.search(r'dogs',line)
>>> matchObj
<_sre.SRE_Match object at 0x01FA61A8>
>>> matchObj = re.search(r'dogs$',line)
>>> matchObj
<_sre.SRE_Match object at 0x01FA6218>
>>> matchObj.group()
'dogs'
>>> 

>>> searchObj.group()

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    searchObj.group()
NameError: name 'searchObj' is not defined
>>> line = "Cats are smarter than dogs"
>>> import re
>>> re.match(r'dogs',line,re.M|re.I)
>>> matchObj.group()
'dogs'
>>> re.match(r'dogs',line,re.M|re.I)
>>> print matchObj.group()
dogs
>>> matchObj = re.match(r'dogs',line,re.M|re.I)
>>> print matchObj.group()

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print matchObj.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
