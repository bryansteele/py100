a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

"""
Prints 7

In Python, integers are immutable. When the function is called with `a` as an
argument, the local variable `b` inside the function is set to reference the
same value as `a`, which is 7.
+= inside the function creates a new object of 17 and updates the variable `b`, 
but the original variable `a` remains unaffected .
"""