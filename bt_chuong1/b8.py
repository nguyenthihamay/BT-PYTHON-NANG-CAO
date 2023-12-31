class Date:
    def __init__(self,day,month,years) :
        self.day = day 
        self.month = month
        self.years = years
    def display(self):
        print(f"{self.day}/{self.month}/{self.years}")
class Employee(Date):
    def __init__(self,name):
        self.name = name
        print('tên nhân viên',self.name)
    def date_birth(self,day,month,years):
        super().__init__(day,month,years)
        print('ngày sinh: ',self.day,self.month,self.years)
    def date_in(self,day,month,years):
        super().__init__(day,month,years)
        print('ngày vào: ',self.day,self.month,self.years)
obj = Employee('m')
obj.date_birth(6,3,2004)
obj.date_in(5,4,2021)