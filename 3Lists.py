# Working with Lists p.s. they are similar to array

friends = ["Mihir", "Abdul", "Ghanshyam"]

print(friends[0])
print(friends[-1])  # Reverse index starts searching from backwards... IT'll print Ghanshyam as output
print(friends[1:])  # will grab all the elements from index 1 including 1

planets = ["Mercury", "Venus", " Earth", "Mars", "Jupiter", "Saturn ", "Uranus", "Neptune"]
planets[6] = "Your Anus"  # Will replace uranus with your anus
print(planets[1:7])  # will grab all the elements from index 1 including 1 but excluding 7

# Playing around with List Functions
list1 = [1, 2, 3, 4, 5, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

print(str(list1)+" \n"+str(list2))
list2.extend(list1)  # Will extend list1 @ the end of list2. when list2 print ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]
print(list2)

list2.append('f')  # Will append at the end of list o.p ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 'f']
print(list2)

list2.insert(1, "tdk")  # Will insert tdk @ index 1 in list2. Op is ['a', 'tdk', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 'f']
print(list2)

list2.remove("tdk")
print(list2)  # Will remove tdk from list. o.p is ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 'f']

# list2.clear()
# print(list2)  # Will truncate all data from list i.e empty it. o.p is []

list2.pop()
print(list2)  # Will pop the last element from list. o.p. is ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]. see f is missing

print(list2.index("e"))  # Prints the index of e o.p is 4

print(list2.count(5))  # Will print the count of 5.

list2 = ["e", "d", "c", "b", "a"]

list2.sort()  # Will sort it alphabetically
print(list2)

list1 = [5, 4, 3, 2, 1]

list1.sort()  # Will sort it numerically in ascending order [1, 2, 3, 4, 5]
print(list1)

list1.reverse()  # Will list it in a reverse order  o.p [5, 4, 3, 2, 1]
print(list1)

list3 = list1.copy()  # Will copy the exact contents of list1 to list 3 o.p [5, 4, 3, 2, 1]
print(list3)




