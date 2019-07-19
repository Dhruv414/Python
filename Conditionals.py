'''This program highlights the conditionals/syntax in Python
    Notes:
    - "is" is equivalent to == in java
    - "in range" creates a for loop structure
    -To indicate a range for an array/string, use [] next to it, for ex: f[1:] (from 1 onwards), f[1:2] (1 inclusive to 2 exclusive), negative indices mean from the end (-1 = the last index)
    -breaks and continue work as they do in java
'''

integer = 0
list = [1,2,3,4,5,6,7,8,9,10]

if integer is 0:
    print("The number is 0")
elif integer is 10:
    print("The number is not 0, but 10")
else:
    print("The number is none of the above")
    #In python, you need the : at the end of your conditionals to tell everything that is intended will follow/run

print("\n")

print("The first loop:")
    #These following programs will print out the elements from the list with some variation'''

for num in list:
    print(num)

print("\nThe second loop:")

for num in range(0,len(list), 1):  #Quit habit of inserting parenthesis
    print(list[num])

print("\nEvery other number")

for num in range(0, len(list), 2):
    print(list[num])

print("\n Using a while loop")

integer = 1
while integer <= 10:
    print(integer)
    integer += 1







