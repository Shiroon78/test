class Person:
    name = "Shiro"
    occupation = "Software Developer"
    networth = "10mil"

    def info(self):
        print(f"{self.name} is a {self.occupation} and his networth is {self.networth}")

a = Person()
b = Person()
c = Person()


# a.name = "Sen"
# a.occupation = "CA"

# b.name = "Dellin"
# b.occupation = "HR"

a.info()
b.info()