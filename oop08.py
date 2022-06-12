# we have little pro ject to do

# crating libraray managment system which handle the following 
# 1.customer should be able to display all the books
# 2.handle the process when customer request to borrow book
# 3.handle the process when customer return a book

from re import template


class Library:
    
    # initializing
    def __init__(self,name,books):
        self.name=name
        self.books=books
        print(f"Welcome '{self.name}' to our Libreay")
 

    # all books
    def mybooks(self):                                                                             
        print(">We have following book avalable")
        print(self.books)
      

    # borrow book
    def borrows(self,book):
        self.book=book
        if book in self.books:
            print(">Congratulation you got the book")
            self.books.remove(self.book)
        else:
            print(">No such book is Available")

    # return book
    def returns(self,book):
        self.book=book
        if book in self.books:
            print(">We have alrady this book")

        else:
            self.books.append(self.book)
            print(">Thanks to return the book")
     








    

if __name__ == '__main__':

    books=["book1","book2","book3","book4","book5"]
    name=input("Enter your name : ")
    name=Library(name,books)

    while  True:

        print("""
    if you want to see all the books press 1                    
    if you want to borrow a book press 2                          
    if you want to return a book press 3
    if you want to Quit press 4""")

        try:
            value=int(input(">"))
        except:
            print("Enter correct value")
            continue

        if value==1:
            name.mybooks()
        elif value==2:
            book_name=input(">Enter book name you want to borrow : ")
            name.borrows(book_name)
        elif value==3:
            book_name=input(">Enter book name you want to return : ")
            name.returns(book_name)
        elif value==4:
            break
            
        else:
            print("Enter correct value")
            continue
