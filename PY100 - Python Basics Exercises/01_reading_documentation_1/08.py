"""
https://docs.python.org/3/reference/lexical_analysis.html#numeric-literals

You can write large numbers by using underscores to separate groups of digits.
"""

1_987_654_321



# Further Exploration: Is it okay to write 

1_987_654_321 
# as
19_87_65_4321

print(1_987_654_321 == 19_87_65_4321)
print(1_987_654_321 is 19_87_65_4321)

"""
Yes

Underscores are ignored for determining the numeric value of the literal.
They can be used to group digits for enhanced readability. One underscore can
occur between digits, and after base specifiers like 0x.
"""