var_list = []

print(type(var_list))

objects = [10,20,30,40]

print(objects )

objects.append(1000)

print(objects)
for obj in objects: # iterate a list
    print(int(obj) + 5)
    
print(objects)

print(objects[1]) # counting starts at 0

print(len(objects)) # how many elements are in a list

numbers = [0,1,2,3,4,5,6,7,8,9]

print(numbers)

numbers = (list(range(0,60))) # numbers

print(numbers)

print(dir(numbers))

things = [["grapes", "pineapples"], [3,4,5]]

print(things)

