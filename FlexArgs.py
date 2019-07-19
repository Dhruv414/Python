def calc(*args):
    total = 0
    for num in args:
        total += num
    return total
'''
print(calc(1,2,3))
print(calc(1,2,3,4,5))
print(calc(1,2,3,4,5,6,7,8,9,10)) # * means to unpack, so * before a list will use all values into parameter

list = [1,2,3,4,5,6,7,8,9,10]
print(calc(*list))
print(calc(*range(100))) #range is a list array w/ numbers from 1-a number
print(calc(*range(1000)))
'''