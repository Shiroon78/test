# a = True
# print(a:=False)  # Using the walrus Operator, It is represented as ():=)... Any expression that is part of a larger expression performs assignment with the help of the operator and helps to get the value of the edpression


# numbers = [1,2,3,4,5]

# while (n := len(numbers)) > 0:
#     print(numbers.pop())

# foods = list()
# while True:
#     food = input("What kind of food do you like?")

#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while (food := input("What kind of food do you like?")) != "quit":
    foods.append(food)