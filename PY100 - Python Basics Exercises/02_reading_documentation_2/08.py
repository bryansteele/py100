"""
https://docs.python.org/3/library/exceptions.html#SyntaxError
A SyntaxError occurs when a Python program can't be understood by the Python
interpreter.

File "/Users/bryan/py100/PY100 - Python Basics
Exercises/02_reading_documentation_2/08.py", line 9
    if current_speed > speed_limit
                                  ^
SyntaxError: expected ':'

The ^ indicates where the error was first detected. With that and SyntaxError:
expected ':', we can see that a : was left off the end of the if statement.
"""


speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')