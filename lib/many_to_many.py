class Author:
    all = [] #class variable to track all Author instances
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        return [contract.book for contract in self.contracts()]
    def sign_contract(self, book, date, royalties):
        #create a new Contract object and return it
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    def __str__(self):
        return f"Author: {self.name}"
    
   

class Book:
    all = []
    def __init__(self, title):
       self.title = title 
       Book.all.append(self)
    def contracts(self):
        # Return a list of contracts where the book is self
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Return a list of authors associated with the book via contracts
        return [contract.author for contract in self.contracts()]
    def __str__(self):
        return f"Book: {self.title}"

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,value): 
        if isinstance(value, Author):
            self._author = value
        else:

            raise Exception("the author must be an instance of the Author class") 
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self,value):
        if isinstance(value, Book):
            self._book = value 
        else:
            raise Exception("The book should be an instance of the Book class")
    #a getter for the date property
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception("The date property should be a string that represents the date when the contract was signed")
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._royalties = value
        else:
            raise Exception("The royalties property should be a number that represents the percentage of royalties that the author will receive for the book.")
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
