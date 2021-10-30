subject = ['physics', "chemistry", "math"]
games = ['football', "cricket", "tennis"]

# append
# subject.append("bangla")
# print(subject)

# Index = subject.index("math")
# print(Index)

# insert
# subject.insert(0,"bangla")
# print(subject)

# extend
# subject.extend(games)
# print(subject)

# remove
# subject.remove("math")
# print(subject)

# reverse
# subject.reverse()
# print(subject)

# conactenation
# print(subject + games)

# repetition
# print(subject * 2)

# List Comprehension

# list1 = [0, 1, 2, 3, 4, 5, 6]
# list2 = []
# for i in list1:
#    list2.append(i+1)
# print(list2)


# List Comprehension

# list1 = []
# for i in range(20):
#    list1.append(i + 1)

# print(list1)


# List Comprehension
list1 = []
for i in range(20):
    if i % 2 == 0:
        list1.append(i)
print(list1)
