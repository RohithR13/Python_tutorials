import re

#findall
text ="a hello human in the world"

pattern =re.compile("a hello")

result = pattern.search(text)
print(result)
email =input("give ur email:")
pat =re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
test = pat.search(email)
print(test)