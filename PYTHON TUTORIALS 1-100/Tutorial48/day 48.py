# Local and Global Variable



x = 4          # This is a global variable

def hello():
    global x
    x = 10     # This will change the value of x within the function
    y = 5      # This is a local variable
    print(y)
    print(f"The local x is {y}")

print(x)
# print(y)       # This will throw error because y is not a global variable and it cannot be used outside a function
hello()
print(f"The global x is {x}")













