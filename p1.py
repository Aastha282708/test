Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="I dont like smoke"
>>> a[0]
'I'
>>> a.upper
<built-in method upper of str object at 0x03B1A710>
>>> a.upper()
'I DONT LIKE SMOKE'
>>> 'i'.islower()
True
>>> 'i'.isdigit()
False
>>> '2'.isdigit()
True
>>> 'abc2'.isalnum()
True
>>> '2222'.isdecimal()
True
>>> a="i dont like smoke"
>>> a.split()
['i', 'dont', 'like', 'smoke']
>>> a.split('o')
['i d', 'nt like sm', 'ke']
>>> a.split('like')
['i dont ', ' smoke']
>>> 12 is not 12
False
>>> 12 is 13
False
>>> 12 is '12'
False
>>> 'smoke' in a
True
>>> 'abc' in a
False
>>> 2**2
4
>>> 
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 10%3
1
>>> list1=[12,12,12,"Nepal",True]
>>> type(list1)
<class 'list'>
>>> list1=[12,12.12,'Nepal',True]
>>> type(list1)
<class 'list'>
>>> type(12)
<class 'int'>
>>> type(True)
<class 'bool'>
>>> type('Nepal')
<class 'str'>
>>> index(12)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    index(12)
NameError: name 'index' is not defined
>>> list1[2]
'Nepal'
>>> list[0]=43
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list[0]=43
TypeError: 'type' object does not support item assignment
>>> list1[0]=13
>>> list1[0]
13
>>> list[-2]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list[-2]
TypeError: 'type' object is not subscriptable
>>> list1[-2]
'Nepal'
>>> list1[-2][2]
'p'
>>> list1[-2][2:]
'pal'
>>> list2=[13,45,23,["Nepal","Canada"],1,22]
>>> print(list2)
[13, 45, 23, ['Nepal', 'Canada'], 1, 22]
>>> print type(list2)
SyntaxError: invalid syntax
>>> type(list2)
<class 'list'>
>>> list2[3][0][2]
'p'
>>> a="nepal"
>>> a[::-1]
'lapen'
>>> list2[::-1]
[22, 1, ['Nepal', 'Canada'], 23, 45, 13]
>>> list2.append(47)
>>> list2.insert(1,2,22,23)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    list2.insert(1,2,22,23)
TypeError: insert() takes exactly 2 arguments (4 given)
>>> list2.insert(1,44)
>>> print(list2)
[13, 44, 45, 23, ['Nepal', 'Canada'], 1, 22, 47]
>>> list1.insert(2,6)
>>> print(list1)
[13, 12.12, 6, 'Nepal', True]
>>> list2.append([6,7])
>>> print(list2)
[13, 44, 45, 23, ['Nepal', 'Canada'], 1, 22, 47, [6, 7]]
>>> list2.extend([9, 11, 13])
>>> print(list2)
[13, 44, 45, 23, ['Nepal', 'Canada'], 1, 22, 47, [6, 7], 9, 11, 13]
>>> list2=list2+[2,3,4]
>>> print(list2)
[13, 44, 45, 23, ['Nepal', 'Canada'], 1, 22, 47, [6, 7], 9, 11, 13, 2, 3, 4]
>>> print(list2)







