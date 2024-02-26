def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)


# SyntaxError is raised because a parameter without a default follows parameter with a default