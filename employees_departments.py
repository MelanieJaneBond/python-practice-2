class Employee:
    def __init__(self, name):
        self.name = name
        self.job_title = ""
        self.start_date = 0

sarah_smith = Employee("Sarah")
sarah_smith.job_title = "laundry"
sarah_smith.start_date = 2017

bob_smith = Employee("Bobby")
bob_smith.job_title = "laundry"
bob_smith.start_date = 2016

adam_knowles = Employee("Queen of Sass")
adam_knowles.job_title = "maid"
adam_knowles.start_date = 2018

joe_kennerly = Employee("Smarty Pants Man")
joe_kennerly.job_title = "friend"
joe_kennerly.start_date = 1990

mel_bond = Employee("Mel B")
mel_bond.job_title = "maid"
mel_bond.start_date = 2005

class Company:
    def __init__(self, name):
        self.name = name
        self.address = ""
        self.industry = "Hospitality"
        self.employees = list()

hyatt = Company("The Hyatt")
hyatt.address = "Cranberry St"
hyatt.employees.append(mel_bond)
hyatt.employees.append(adam_knowles)
hyatt.employees.append(joe_kennerly)



westin = Company("The Westin")
westin.address = "Blueberry St"
westin.employees.append(sarah_smith)
westin.employees.append(bob_smith)

print(f"{westin.name} is in the {westin.industry} industry. Their employees are...")
for i in westin.employees:
        print(f"* {i.name}")
print(f"{hyatt.name} is in the {hyatt.industry} industry. Their employees are...")
for i in hyatt.employees:
    print(f"* {i.name}")

#struggled with this; I didn't realize I needed to call out the "i.name" to access
#the "name" property of those listed objects in the "employees" list.