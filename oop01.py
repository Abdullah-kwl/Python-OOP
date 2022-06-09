class Employe:
    def __init__(self,fname,lname,salary) :
        self.fname=fname
        self.lname=lname
        self.salary=salary


ali=Employe("Ali",'Khan',40000)
ahmad=Employe("Ahmad","Kamal",35000)


print(ali.fname , ali.lname , ali.salary)
print(ahmad.fname,ahmad.lname,ahmad.salary)

