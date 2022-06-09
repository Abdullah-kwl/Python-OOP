
class Employe:
    inc=2

    def __init__(self,fname,lname,salary) :
        self.fname=fname
        self.lname=lname
        self.salary=salary
        # self.inc=1.5

    def increment(self):
        # Replacing Employ.inc to self.inc
        # first it will go for object_instance and if not found then go for Class_instance  
        self.salary=self.salary*self.inc


ali=Employe("Ali","Khan",40000) 

print(ali.fname,ali.lname,ali.salary)

ali.increment()

print(ali.fname,ali.lname,ali.salary)
