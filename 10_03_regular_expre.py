import re

text = "Namsjar! Dhanu I am dhanu. "
# https://regexr.com/



# match = re.search("Dhanu",text)
# print(match)

# if match:
#      print("Match found")
#      print("start index", match.start())
#      print("end index", match.end())

matches = re.findall("Dhanu", text, re.IGNORECASE)
print(matches)

new = re.sub("Namsjar","Namskar",text)
print(new)