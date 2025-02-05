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
            total_value += (i.amount * i.price)
            
        return total_value

    def employees_summary(self) -> str:
        summary = "Employees:\n"
        for i, employee in enumerate (self.employees):
            first_name = employee["first_name"]
            last_name = employee["last_name"]
            age = employee["age"]
            
            summary += f"The employee number {i} is {first_name} {last_name} who is {age} years old.\n"
        
        return summary
