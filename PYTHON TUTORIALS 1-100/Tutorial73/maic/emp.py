# Magic/Dunder method


class Employee:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def work(self):
        print(f"Hello, my name is {self.name}. I work as a software {self.job}.")

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"The name of the employee is {self.name} str"

    def __repr__(self):
        return f"mployee('{self.name}') repr"

    def __call__(self):
        print("Hey I am good")
