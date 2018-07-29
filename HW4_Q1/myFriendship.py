import myList
import myPeople
import myBooks
import MB
import random
class myFriendship:
    def __init__(self):
        self.people = myList.myList()
        self.books = myList.myList()

    # prints current people with books
    def get_info(self):
        for i in range(0, self.people.len):
            print(self.people.find(i).item)

    def get_people_list(self):
        return self.people

    def get_books_list(self):
        return self.books

    # prints current people with books sorted
    def sort_people_name(self, reverse=False):
        temp_people = self.people
        for i in range(0, temp_people.len):
            for j in range(0, temp_people.len - 1):
                if reverse:
                    if temp_people.find(j).item.name < temp_people.find(j + 1).item.name:
                        if j == 0:
                            t2 = temp_people.find(j)
                            t3 = temp_people.find(j + 1)
                            t4 = temp_people.find(j + 1).next
                            t2.next = t4
                            t3.next = t2
                            temp_people.start.next = t3
                        else:
                            t2 = temp_people.find(j)
                            t3 = temp_people.find(j + 1)
                            t4 = temp_people.find(j + 1).next
                            t2.next = t4
                            t3.next = t2
                            temp_people.find(j - 1).next = t3
                else:
                    if temp_people.find(j).item.name < temp_people.find(j + 1).item.name:
                        if j == 0:
                            t2 = temp_people.find(j)
                            t3 = temp_people.find(j + 1)
                            t4 = temp_people.find(j + 1).next
                            t2.next = t4
                            t3.next = t2
                            temp_people.start.next = t3
                        else:
                            t2 = temp_people.find(j)
                            t3 = temp_people.find(j + 1)
                            t4 = temp_people.find(j + 1).next
                            t2.next = t4
                            t3.next = t2
                            temp_people.find(j - 1).next = t3
        for k in range(0, temp_people.len):
            print(temp_people.find(k).item)

    def return_book(self, title, edition, borrow_person_id, lend_person_id):
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == borrow_person_id:
                index = i
                person_to_borrow = self.people.find(index).item
                break
        for j in range(0, self.people.len):
            if self.people.find(j).item.id == lend_person_id:
                index = j
                person_to_lend = self.people.find(index).item
                break
        ans = None
        for i in range(0, person_to_borrow.current_book.len):
            if person_to_borrow.current_book.find(i).item.title == title:
                ans = person_to_borrow.current_book.find(i)
                person_to_borrow.current_book.delete(ans)
                break
        if ans is None:
            print("Didn't find a book called " + title + " in the possession of " + person_to_lend.name)
        elif ans is not None:
            person_to_lend.current_book.append(ans.item)

    def borrow_book(self, title, edition, borrow_person_id, lend_person_id):
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == borrow_person_id:
                index = i
                person_to_borrow = self.people.find(index).item
                break
        if person_to_borrow.is_friend_with(lend_person_id):
            for j in range(0, self.people.len):
                if self.people.find(j).item.id == lend_person_id:
                    index = j
                    person_to_lend = self.people.find(index).item
                    break
            ans = None
            for i in range(0, person_to_lend.current_book.len):
                if person_to_lend.current_book.find(i).item.title == title:
                    ans = person_to_lend.current_book.find(i)
                    person_to_lend.current_book.delete(ans)
                    break
            if ans is None:
                print("Didn't find a book called " + title + " in the possession of " + person_to_lend.name)
            elif ans is not None:
                person_to_borrow.current_book.append(ans.item)
                person_to_borrow.borrowed_book.append(ans.item)
        else:
            print("The lender is not a friend with the borrower")

    def add_friend(self, id_first, id_second):
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == id_first:
                first_person = self.people.find(i).item
                break
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == id_second:
                second_person = self.people.find(i).item
                break
        check = True
        for i in range(first_person.friends.len):
            if first_person.friends.find(i).item == second_person:
                check = False
                print("Second person is already a friend of the first person.")
                break
        if check:
            first_person.add_friend(second_person)
            print("Successfully added second person to the friends list of the first person.")

    def delete_friend(self, id_first, id_second):
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == id_first:
                first_person = self.people.find(i).item
                break
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == id_second:
                second_person = self.people.find(i).item
                break
        check = False
        for i in range(first_person.friends.len):
            if first_person.friends.find(i).item == second_person:
                check = True
                break
        if check:
            first_person.break_friend(second_person)
            print("Successfully deleted second person as a friend of the first person.")

    def menu():
        print("select an option: ")
        print("---inappropriate input will cause program to exit---")
        print("[1]use simulation data")
        print("[2]create people and books yourself (very painful process to enter large amount of data. Don't do this!)")
        level_one = input()
        if level_one == "1":
            library_one = myFriendship()
            for i in range(0, 6):
                person = myPeople.myPeople("Person" + str(i), 100 + i, random.randint(20, 60))
                library_one.people.append(person)
            for i in range(0, 20):
                for j in range(1, random.randint(1, 3)):
                    book = myBooks.myBooks("Book" + str(i), "Simon" + str(i), j)
                    library_one.books.append(book)
            for i in range(0, library_one.books.len):
                library_one.people.find(random.randint(0, library_one.people.len - 1)).item.current_book.append(library_one.books.find(i).item)
            print("\n\nselect an option: ")
            print("---inappropriate input will cause program to exit---")
            print("[1]create friendships")
            print("[2]deleting friendships")
            print("[3]borrow books")
            print("[4]return books")
            level_two = input()
            if level_two == "1":
                first_id = input("Your id: ")
                check = True
                while check:
                    second_id = input("The other person's ID: ")
                    library_one.add_friend(first_id, second_id)
                    decision = input("Continue adding friends? y/n")
                    if decision == "n":
                        raise SystemExit
            elif level_two == "2":
                first_id = input("Your id: ")
                check = True
                while check:
                    second_id = input("The other person's ID: ")
                    library_one.add_friend(first_id, second_id)
                    decision = input("Continue deleting friends? y/n")
                    if decision == "n":
                        raise SystemExit

library_one = myFriendship()
person_one = myPeople.myPeople("PersonA", 111, 10)
person_two = myPeople.myPeople("PersonB", 112, 11)
person_three = myPeople.myPeople("PersonC", 113, 12)

# book_zero = myBooks.myBooks("PlaceHolder", "Admin", 1)
book_one = myBooks.myBooks("BookA", "Simon", 1)
book_two = myBooks.myBooks("BookB", "Simon", 1)
book_three = myBooks.myBooks("BookC", "Simon", 1)
book_four = myBooks.myBooks("BookD", "Simon", 1)
book_five = myBooks.myBooks("BookE", "Simon", 1)
book_six = myBooks.myBooks("BookF", "Simon", 1)
# person_one.current_book.append(book_zero)
# person_two.current_book.append(book_zero)
# person_three.current_book.append(book_zero)
person_one.current_book.append(book_one)
person_one.current_book.append(book_two)
person_two.current_book.append(book_three)
person_two.current_book.append(book_four)
person_three.current_book.append(book_five)
person_three.current_book.append(book_six)
library_one.add_people(person_one)
library_one.add_people(person_two)
library_one.add_people(person_three)
library_one.get_info()

library_one.borrow_book("BookD", 1, 113, 112)
library_one.return_book("BookA", 1, 112, 111)



