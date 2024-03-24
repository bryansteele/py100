def sum_of_squares(num1, num2):
    def square(num):
        return num * num
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))
print(sum_of_squares(5, 12))
