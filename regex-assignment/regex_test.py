import requests
import re
import random

# Get the text for the constitution
page = requests.get('https://www.usconstitution.net/const.txt')
constitution_text = page.text

# A useful construct I'm leaving in, commented out
# constitution_lines = constitution_text.split('\n')
# for line in constitution_lines:
#       print "-->",line

# Define the regular expression and use it to find matches
regex = r"(Amendment) (\d+)"
matches = re.findall(regex, constitution_text)

# Do something with the matches
phrases = ["Ye olde", "Hairy", "Dubious", "Purloined",
           "Prurient", "Right honorable"]
for match in matches:
    print random.choice(phrases), match[0], match[1], \
        "+ 100 =", match[0], int(match[1])+100

# Do a replace.  Uncomment to see it working
backwards = re.sub(
    regex, r"--==>>\2 is the \1 in question<<==--", constitution_text
)
print backwards
