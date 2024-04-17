"""
https://docs.python.org/3/library/exceptions.html#TypeError
Raised when an operation or function is applied to an object of inappropriate
type.
It "may be raised by user code to indicate that an attempted operation on an
object is not supported, and is not meant to be."

File "/Users/bryan/py100/PY100 - Python Basics
Exercises/02_reading_documentation_2/09.py", line 10, in <module>
    length_of_tweet = len(tweet + 5)
                          ~~~~~~^~~
TypeError: can only concatenate str (not "int") to str

This is telling us that we can not concatenate a string and an integer
"""

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)
