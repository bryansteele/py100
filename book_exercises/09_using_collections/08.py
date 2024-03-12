text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# On line 3, the .rfind is only looking at the slice that was extracted out.
# On line 4, .rfind is looking at the whole text 