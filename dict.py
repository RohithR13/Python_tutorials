dictionary = {'apple': 5, 'chikku': 6}
print(dictionary["apple"])
print(dictionary.get("apple"))
print(dictionary.get("mango"))
contact = {
    "ram": ["904850612", "ram@gmail.com"],
    "raju": ["99567123", "raju@gmail.com"]
}
print(contact.get("ram"))

strings = int(input("enter the length:"))

# words= str.split(" ")
# # print(l)
# word_counts = dict()

   
dictionaries =dict()

# for word in words:
#     if word in word_counts:
#         word_counts[word] = word_counts[word] + 1
#     else:
#        word_counts[word]= 1

# # print(counts)

# for key in list(word_counts.keys()):
#     print(key, ":", word_counts[key])

for lengths in range(strings):
    key = str(input("enter the key:" ))
    value = input("enter the value:")
    dictionaries[key]= value 

print(dictionaries)

