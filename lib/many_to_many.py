class Author:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Author: {self.name}"


class Book:
    def __init__(self, title):
       self.title = title 
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
            self._author == value
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