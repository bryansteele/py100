def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1

    return result


# OR


def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number

    return result


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(25))
