import re
name = input("What is your name? ")
name1 = str(name)
print(name1)
name_pattern = r"^[a-zA-Z]+$"

if re.match(name_pattern,name1):
  print("Yes ")
else:
  print("No match")
Aadress  = input("What is your address ?")

print(Aadress)
aadress_pattern = r"^[a-zA-Z0-9\s,]+$"

if re.match(aadress_pattern,Aadress):
  print("Yes Address")
else:
  print("Please enter valid aadress")

percentage = input("What is your percentage ? ")
percentage1 = float(percentage)
print(percentage1)
percentage_pattern = r"^[0-9][0-9,.]+$"

if re.match(percentage_pattern, percentage):
  print("Yes Percentage")
else:
  print("Please enter valid percentage")

highest =  input("What is your highest qualification ? ")
highest1 = str(highest)
print(highest)
highest_pattern = r"^[a-zA-Z,.]+$"

if re.match(highest_pattern,highest1):
  print("Yes Heighest Qualification")
else:
  print("Please enter Heighest Qualification")
