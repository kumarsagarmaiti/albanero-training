from dataclasses import dataclass, field


@dataclass(order=True)
class Employee:
    sort_index: int = field(init=False, repr=False)
    f_name: str
    l_name: str
    age: int
    company: str
    full_name: str = field(init=False, repr=True)
    role: str = field(repr=True)

    def check_age(self):
        if self.age < 18:
            return "Underage"

    def __repr__(self):
        return f'{self.f_name} is a {self.role} at {self.company}. He is {self.age} years old'

    def __post_init__(self):
        self.sort_index = self.age
        self.full_name = f'{self.f_name} {self.l_name}'


employee1 = Employee("Kumar Sagar", "Maiti", 24, "Albanero", "Software Engineer")
print(employee1.age)
employee2 = Employee("Mahesh", "Kumar", 26, "Albanero", "Software Engineer")

print(employee1 < employee2)
print(employee1.full_name)
print(employee2.full_name)

print(employee1)
print(employee2)
