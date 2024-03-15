# Super Keywords

class ParentClass:
    def parent_method(self):
        print("Parent Method")
    
class childClass(ParentClass):

    def parent_method(self):
        print("Licaa2")
        super().parent_method()
    def child_method(self):
        print("Child_Method")
        super().parent_method()

child_obeject = childClass()
child_obeject.child_method()
child_obeject.parent_method()


# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

# class Programmer(Employee):
#     def __init__(self, name, id, lang):
#         self.name = name
#         self.id = id
#         self.lang = lang
#         super().__init__(name,id)
#         self.lang = lang

# Lica = Employee("Lica", "459")
# shiro = Programmer("Shiro", "2897", "Python")

# print(Lica.name)
# print(shiro.lang)
# print(shiro.id)
# print(shiro.name)


