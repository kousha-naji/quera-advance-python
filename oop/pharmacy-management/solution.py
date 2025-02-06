class Drug:
    def __init__(self, name: str, amount: int, price: int):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug: Drug):
        self.drugs.append(drug)

    def add_employee(self, first_name: str, last_name: str, age: int):
        employee = {
            "first_name" : first_name,
            "last_name" : last_name,
            "age" : age
        }
        self.employees.append(employee)

    def total_value(self) -> int:
        total_value = 0
        for i in self.drugs:
            total_value +- (i.amount * i.price)

    def employees_summary(self) -> str:
        summary = "Employees:\n"
        for i in self.Employees:
            name = i["first_name"]
            last_name = i["last_name"]
            age = i[age]
            
            summary += "The employee number {i} is {first_name} {last_name} who is {age} years old.\n"
        
        return summary