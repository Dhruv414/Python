'''currency conversion, from USD to Euros, 1$ = 0.89 Euros
    -flexible argument parameter keyword is : *args
'''

def convert(integer):
    return integer*0.89

def convertFullStatement(integer): #This is the equivalent of a void method in java
    print(integer,"dollars is ", integer*0.89, " euros")

print("From 1-10 dollars, the value of the Euro goes like:")
for num in range(1,11):
    print(num,"dollars is: ", convert(num)," euros")

print("\n")

for num in range(1,11):
    convertFullStatement(num)