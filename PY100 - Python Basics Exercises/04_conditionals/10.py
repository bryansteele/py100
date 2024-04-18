speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)

# True

print()

# Bonus Question
# Yes, we need the parentheses. Since and has a higher operator precedence than or

