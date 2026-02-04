

d = {}  # this is an empty dictionary
marks = {
    "Alice": 85,
    "mingo": 98,
    "Bob": 76,
    "Diana": 89
}

print(marks.items())
# print(marks.keys())
# print(marks.values())
print(marks.get("jon")) # returns none if key not found 
# printI(marks["mingo"]) # raises error if key not found


marks.update({"mingo": 100})
print(marks["mingo"])