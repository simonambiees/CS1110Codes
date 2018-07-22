import myList
import myPeople
import myBooks
class myLibrary:
    def __init__(self):
        self.people = myList.myList()
        self.books = myList.myList()

    def add_people(self, person):
        self.people.append(person)

    def add_book(self, book):
        self.books.append(book)

    def get_info(self):
        for i in range(0, self.people.len):
            print(self.people.find(i).item)

library_one = myLibrary()
person_one = myPeople.myPeople("A", 111, 10)
person_two = myPeople.myPeople("B", 112, 10)
person_three = myPeople.myPeople("C", 113, 10)
book_one = myBooks.myBooks("BookA", "Simon", 1)
book_two = myBooks.myBooks("BookB", "Simon", 1)
book_three = myBooks.myBooks("BookC", "Simon", 1)
book_four = myBooks.myBooks("BookD", "Simon", 1)
book_five = myBooks.myBooks("BookE", "Simon", 1)
book_six = myBooks.myBooks("BookF", "Simon", 1)
person_one.borrow_book(book_one)
person_one.borrow_book(book_two)
person_two.borrow_book(book_three)
person_two.borrow_book(book_four)
person_three.borrow_book(book_five)
person_three.borrow_book(book_six)
library_one.add_people(person_one)
library_one.add_people(person_two)
library_one.add_people(person_three)

person_one.return_book("BookA", 1)
print(person_one)