
# Class
class Employe:

    # Class_instance/Variable
    inc=1.5


    # Constructor
    def __init__(self,fname,lname,salary) :
        self.fname=fname
        self.lname=lname
        self.salary=salary

    # Method
    def increment(self):
        self.salary=self.salary*self.inc
    
    # Class-Method
    @classmethod
    def increment_chng(cls,val):
        cls.inc=val

    # Class-Methos as a Constructor
    @classmethod
    def str_parse(cls,string):
        fname , lname , salary = string.split("-")
        return cls(fname,lname,int(salary))
    



# Object creation
ali=Employe.str_parse("Ali-Khan-40000") 

# printing object instance
print(ali.fname,ali.lname,ali.salary)
print(ali.fname,ali.lname,type(ali.salary))



ahmad=Employe("Ahmad","jamal",5000)
print(ahmad.fname,ahmad.lname,ahmad.salary)