import myList
import myPeople
import myBooks
class myFriendship:
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

    def borrow_book(self, title, edition, borrow_person_id, lend_person_id):
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == borrow_person_id:
                index = i
                person_to_borrow = self.people.find(i).item
                break
        for j in range(0, self.people.len):
            if self.people.find(j).item.id == lend_person_id:
                index = j
                person_to_lend = self.people.find(j).item
                break
        ans = None
        for i in range(0, person_to_lend.current_book.len):
            if person_to_lend.current_book.find(i).item.title == title & person_to_lend.current_book.find(i).edition_number == edition:
                ans = person_to_lend.current_book.find(i)
        if ans is None:
            print("Didn't find a book called " + title + " in the possession of " + person_to_lend.name)

        person_to_borrow.current_book.append(ans)
        person_to_borrow.borrowed_book.append(ans)


library_one = myFriendship()
person_one = myPeople.myPeople("PersonA", 111, 10)
person_two = myPeople.myPeople("PersonB", 112, 10)
person_three = myPeople.myPeople("PersonC", 113, 10)
person_one.add_friend(person_two)
person_two.add_friend(person_one)
person_two.add_friend(person_three)
person_three.add_friend(person_one)
book_one = myBooks.myBooks("BookA", "Simon", 1)
book_two = myBooks.myBooks("BookB", "Simon", 1)
book_three = myBooks.myBooks("BookC", "Simon", 1)
book_four = myBooks.myBooks("BookD", "Simon", 1)
book_five = myBooks.myBooks("BookE", "Simon", 1)
book_six = myBooks.myBooks("BookF", "Simon", 1)
library_one
library_one.add_people(person_one)
library_one.add_people(person_two)
library_one.add_people(person_three)

person_one.return_book("BookA", 1)
library_one.get_info()
