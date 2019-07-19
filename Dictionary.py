'''Similar to a map in java
'''
import FlexArgs

age = {"Dhruv":12, "Sam":13, "Bob": 15}

print(age)

for name in age:
    print(name, "is",age[name], "years old")

#OR
print("\n")

for n, a in age.items():
    print(n,"is", a,"years old")

print(FlexArgs.calc(*range(10)))