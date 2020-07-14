names = ["mark" , "bob" , "mosh", "sarah", "marrry"]
print(names)

names = ["mark" , "bob" , "mosh", "sarah", "marrry"]
print(names[2])

names = ["mark" , "bob" , "mosh", "sarah", "marry"]
print(names[2:])

names = ["mark" , "bob" , "mosh", "sarah", "marry"]
print(names[2:4])

numbers =[3,5,7,9,0,4,2]
max = numbers [0]
for number in numbers :
    if number>max:
        max=number
print(max)

numbers =[3,5,7,9,4,2]
min = numbers [0]
for number in numbers :
    if number<min:
        min=number
print(min)
