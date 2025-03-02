class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname,lname)
        self.salary = salary

    def cal_paycheck(self):
        return self.salary/52
    
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname,lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def cal_paycheck(self):
        return self.weekly_hours * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate

    def cal_paycheck(self):
        return super().cal_paycheck() + self.sales_num * self.com_rate