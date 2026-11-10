>>> int('12a)
  File "<python-input-0>", line 1
    int('12a)
        ^
SyntaxError: unterminated string literal (detected at line 1)
>>> int('12a')
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    int('12a')
    ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '12a'
>>> 4+'3'
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    4+'3'
    ~^~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> num={'name' :'rithi','age':19,'country':'india'}
>>> print(ag)
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    print(ag)
          ^^
NameError: name 'ag' is not defined
>>> print(age)
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    print(age)
          ^^^
NameError: name 'age' is not defined
>>> print('age')
age
>>> num={'name':'rithi','age':19}
>>> print(age)
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    print(age)
          ^^^
NameError: name 'age' is not defined
>>>
KeyboardInterrupt
>>> num={'name':'rithi','age':19} print(age)
  File "<python-input-9>", line 1
    num={'name':'rithi','age':19} print(age)
                                  ^^^^^
SyntaxError: invalid syntax. Did you mean 'in'?
>>> num={'name':'rithi','age':19}
>>> num['name']
'rithi'
>>> num[ag]
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    num[ag]
        ^^
NameError: name 'ag' is not defined
>>> num['ag']
Traceback (most recent call last):
  File "<python-input-13>", line 1, in <module>
    num['ag']
    ~~~^^^^^^
KeyError: 'ag'