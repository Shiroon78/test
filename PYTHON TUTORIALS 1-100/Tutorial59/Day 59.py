
def greet(fx):
    def mfx():
        print("Good Morning")
        mfx()
        print("Thank you for using this Function")
        return mfx
@greet
def hello():
    print("Hello, World!")

@greet
def add(a, b):
    print(a+b)

hello()