text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29


"""
The first print() we call rfind() on the retrun value of the splice, which is 
'for the fjords' and the rfind() goes from right to left. The 1st 'f' is the 
index number 8.

In the second print(), rfind() is called on the whole text, where index 0 starts
with 'I', not just the spliced section. 
"""


