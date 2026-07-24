text = "aSdgytGTYBKO:        34562"

# Find and extract the number
position = text.find("3")
number = text[position:].strip()

# Convert to float
result = float(number)

print("Extracted value:", result)

# Other string methods
test = "blood culture"
print(test.upper())
print(test.lower())
print(test.capitalize())
print(test.title())

result2 = "Blood Group: A positive"
print(result2.replace("positive", "POS"))
