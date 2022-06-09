
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
    

    # if we donot want towork with class or object instace then we make staticmethod
    # we can acces it directaly using class
    @staticmethod
    def isopen(day):
        if day=='sunday':
            print("Close")
        else:
            print("OPen")


class Programer(Employe):
    
    def __init__(self, fname, lname, salary,language,country):
        # initializing super class constructor
        super().__init__(fname, lname, salary)
        self.lnguage=language
        self.country=country


    # overridden method
    def increment(self):
        self.salary=self.salary*(self.inc+0.5)



ahmad=Programer("Ahmad","Niazi",20000,"Python","Pakistan")

print(ahmad.fname,ahmad.lname,ahmad.salary,ahmad.lnguage,ahmad.country)
ahmad.increment()
print(ahmad.fname,ahmad.lname,ahmad.salary,ahmad.lnguage,ahmad.country)
