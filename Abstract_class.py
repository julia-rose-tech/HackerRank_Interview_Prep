# Example of abstract classes. From chatGPT: 
# In Python, an abstract class is a class that cannot be instantiated on its own and is meant to be subclassed by other classes. Abstract classes are used as a blueprint for other classes and may contain abstract methods, which are methods that have no implementation in the abstract class but must be implemented by any concrete (subclass) that inherits from the abstract class.

# Sample Input:
# The Alchemist
# Paulo Coelho
# 248

# Sample Output:
# Title: The Alchemist
# Author: Paulo Coelho
# Price: 248

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
        

class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price=price
        
    def display(self):
        print("Title: "+self.title)
        print("Author: "+self.author)
        print("Price: "+str(self.price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()