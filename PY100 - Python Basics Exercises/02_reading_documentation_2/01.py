"""
https://docs.python.org/3/library/string.html#format-string-syntax

The str.format method uses placeholders, represented by {}, which sequentially
take in the arguments specified in the format function.


https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals

f-strings allow direct embedding of expressions within the string literals.
The embedded expressions are identified by using {}. These expressions are
assessed during execution and are subsequently transformed according to the
provided format string. 
"""

name = "Victor"
profession = "programmer"

# str.format:
msg = "Hello, {}. You are a {}."
formatted_msg = msg.format(name, profession)
print(formatted_msg)

# f-strings:
print(f"Hello, {name}. You are a {profession}.")