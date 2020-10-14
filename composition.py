#composition

class Salary:
    def __init__(self,pay,reward):
        self.pay=pay
        self.reward=reward
        
    def annual_salary(self):
        return(self.pay*12) + self.reward
    
class Employee:
    def __init__(self,name,position,pay,reward):
        self.name=name
        self.position=position
        self.final_salary=Salary(pay,reward)
        
    def final_salary_m(self):
        return self.final_salary.annual_salary()
    
emp=Employee("Spandana","py dev",100,100)
print(emp.final_salary_m())

# return(self.pay*12) + self.reward
#100*12+100
#1200+100
#1300
    