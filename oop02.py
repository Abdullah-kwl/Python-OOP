class Employe:
    inc=1.5

    def __init__(self,fname,lname,salary) :
        self.fname=fname
        self.lname=lname
        self.salary=salary

    def increment(self):
        self.salary=self.salary*Employe.inc


ali=Employe("Ali","Khan",40000) 

print(ali.fname,ali.lname,ali.salary)


ali.increment()

print(ali.fname,ali.lname,ali.salary)


