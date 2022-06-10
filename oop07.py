
# Class
class Employe:

    # Class_instance/Variable
    inc=1.5


    # Constructor
    def __init__(self,fname,lname,salary) :
        self.fname=fname
        self.lname=lname
        self.salary=salary

    # Instance-Method
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
    

    # if we donot want towork with class or object instace then we make staticmethod
    # we can acces it directaly using class
    @staticmethod
    def isopen(day):
        if day=='sunday':
            print("Close")
        else:
            print("OPen")

    
    # Magic/Dunder-method
    def __add__(self,other):
        return (self.salary+other.salary)





ali=Employe("Ali","Khan",40000)
ahamad=Employe("Ahmad","Niaz",20000)

print(ali+ahamad)