from OOP.employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee
import OOP.employee as employee

class company: 
    def __init__(self):
        self.employees = []

    def add_employee(self,new_employee):
        self.employees.append(new_employee)

    def display_emp(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('------')

    def calc(self):
        print('Payment for Employees:')
        for i in self.employees:
            print('Paycheck for', i.fname, i.lname)
            print('Amount paid:', '$'+str(round(i.cal_paycheck(),2)))
            print('------')


def main():
    my_company = company()

    employee1 = SalaryEmployee('Manthan', 'Mehta', 5000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Dhara', 'Desai', 25,50)
    my_company.add_employee(employee2)
    employee3 = HourlyEmployee('Aadit', 'Kachalia', 40, 15)
    my_company.add_employee(employee3)
    employee4 = CommissionEmployee('Aayushi', 'Gandhi', 4000, 5, 200)
    my_company.add_employee(employee4)

    my_company.display_emp()
    my_company.calc()

main()


