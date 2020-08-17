class SalaryCalculator:
    def __init__(self, base_pay, hours_worked):
        self.base_pay = base_pay
        self.hours_worked = hours_worked

    def calculate(self):
        if self.base_pay < 8:
            print(f'${self.base_pay} did not meet minimum salary wage')
            return
        if self.hours_worked > 60:
            print(f'{self.hours_worked} is over the maximum amount for overtime')
            return

        overtime_hr = hours_worked - 40
        if overtime_hr > 0:
            self.base_pay = (self.hours_worked * self.base_pay) + (overtime_hr * self.base_pay * 1.5)
        else:
            self.base_pay = self.hours_worked * self.base_pay

        return self.__str__()

    def __str__(self):
        print(f'Here is your wage: ${self.base_pay}')


employees = {
    'employee1': (7.50, 35),
    'employee2': (8.20, 47),
    'employee3': (10.00, 73)
}

for k,v in employees.items():
    base_pay, hours_worked = v
    sc = SalaryCalculator(base_pay, hours_worked)
    sc.calculate()
