import json
employee_data = [{"Name":"Lipsa Behera","DOB":"01-08-1998","Height":"5","City":"Bhubaneswar","State":"Odisha"}, 
                 {"Name":"Shamsuddin Mohammad","DOB":"24-09-1996","Height":"5.5","City":"kakinada","State":"Andhrapradesh"},
                 {"Name":"Jyotirmayee","DOB":"31-12-1997","Height":"5.6","City":"Bargarh","State":"Odisha"},
                 {"Name":"Harsita Grover","DOB":"26-04-1996","Height":"5","City":"Ludhiana","State":"Punjab"},
                 {"Name":"Amrita Sinha","DOB":"02-01-1995","Height":"5","City":"Gaya","State":"Bihar"}]

with open("employee.json", "w") as f:
    json.dump(employee_data, f)

with open("employee.json", "r") as f:
    employee_data = json.load(f)

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __repr__(self):
        return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"

employee_list = []
for employee in employee_data:
    emp = Employee(employee["Name"], employee["DOB"], employee["Height"], employee["City"], employee["State"])
    employee_list.append(emp)

print(employee_list)