# MAP

# def cube(x):
#     return x*x*x

# print(cube(3))

l = [1,2,3,4,5,6]
# newl = []
# for line in l:
#     newl.append(cube(item))

newl = list(map(lambda x: x*x*x, l)) # Map is a higher order function
print(newl)

# FILTER

def filter_function(a):
    return a>=4
newnewl = list(filter(filter_function, l)) # Filer is also a higher order function
print(newnewl)

# reduce

from functools import reduce

num = [1,2,3,4,5]
nums = [6,4,5]

# sum = reduce(lambda x,y: x + y, num)

def mysum(x, y):
    return x + y

sum = reduce(mysum, num)

print(sum)

# import functools
# print(dir(functools))