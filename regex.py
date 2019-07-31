import re



inputString = 'Binet–Simon'


regPat = r'[A-Za-z][\w–\-]+[\w.]'
pattern = re.compile(regPat, re.M)

match = re.search(pattern, inputString)
print(match) 
