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
        for i, emp in enumerate (self.employees):
            first_name = emp["first_name"]
            last_name = emp["last_name"]
            age = emp["age"]
            
            summary += f"The employee number {i} is {first_name} {last_name} who is {age} years old.\n"
        
        return summary
    

drug = Drug(name='drug1', amount=5, price=10)
drug2 = Drug(name='drug2', amount=10, price=20)
drug3 = Drug(name='drug3', amount=15, price=30) 

pharmacy = Pharmacy(name='pharmacy1')
pharmacy.add_drug(drug)
pharmacy.add_drug(drug2)

pharmacy.add_employee(first_name='John', last_name='Doe', age=30)
pharmacy.add_employee(first_name='Jane', last_name='Doe', age=25)

print(pharmacy.total_value())

#test