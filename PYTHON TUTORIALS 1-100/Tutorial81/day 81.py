# Example of Hybrid inheritance

class Employee:
    pass

class Dancer:
    pass

class Employee_Dancer(Employee, Dancer):
    pass

# Hierarchical Inheritance

class RestClass:
    pass

class A(RestClass):
    pass
class B(RestClass):
    pass
class C(A):
    pass