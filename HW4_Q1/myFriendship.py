import myList
import myPeople
import myBooks
import random
class myFriendship:
    def __init__(self):
        self.people = myList.myList()
        self.books = myList.myList()

    # prints current people with books
    def get_info(self):
        for i in range(0, self.people.len):
            print(self.people.find(i).item)

    # returns people list
    def get_people_list(self):
        return self.people

    # returns book list
    def get_books_list(self):
        return self.books

    # prints current people (with books) sorted by name
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
                    if temp_people.find(j).item.name > temp_people.find(j + 1).item.name:
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
    
    # prints current people (with books) sorted by age
    def sort_people_age(self, reverse=False):
        temp_people = self.people
        for i in range(0, temp_people.len):
            for j in range(0, temp_people.len - 1):
                if reverse:
                    if int(temp_people.find(j).item.age) < int(temp_people.find(j + 1).item.age):
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
                    if int(temp_people.find(j).item.age) > int(temp_people.find(j + 1).item.age):
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

    # prints current people (with books) sorted by id
    def sort_people_id(self, reverse=False):
        temp_people = self.people
        for i in range(0, temp_people.len):
            for j in range(0, temp_people.len - 1):
                if reverse:
                    if int(temp_people.find(j).item.id) < int(temp_people.find(j + 1).item.id):
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
                    if int(temp_people.find(j).item.id) > int(temp_people.find(j + 1).item.id):
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

    # prints current people (with books) sorted by number of books
    def sort_people_books(self, reverse=False):
        temp_people = self.people
        for i in range(0, temp_people.len):
            for j in range(0, temp_people.len - 1):
                if reverse:
                    if int(temp_people.find(j).item.current_book.len) < int(temp_people.find(j + 1).item.current_book.len):
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
                    if int(temp_people.find(j).item.current_book.len) > int(temp_people.find(j + 1).item.current_book.len):
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

    # return a book with info about people's ids
    def return_book(self, title, edition, borrow_person_id, lend_person_id):
        person_to_borrow = None
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == int(borrow_person_id):
                index = i
                person_to_borrow = self.people.find(index).item
                break
        person_to_lend = None
        for j in range(0, self.people.len):
            if self.people.find(j).item.id == int(lend_person_id):
                index = j
                person_to_lend = self.people.find(index).item
                break
        ans = None
        for i in range(0, person_to_borrow.current_book.len):
            if person_to_borrow.current_book.find(i).item.title == title and person_to_borrow.current_book.find(i).item.edition_number == int(edition):
                ans = person_to_borrow.current_book.find(i)
                person_to_borrow.current_book.delete(ans)
                break
        if ans is None:
            print("Didn't find a book called " + title + " in the possession of " + person_to_borrow.name)
        elif ans is not None:
            person_to_lend.current_book.append(ans.item)
            print("Success!")

    # borrow a book with info about people's ids
    def borrow_book(self, title, edition, borrow_person_id, lend_person_id):
        person_to_borrow = None
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == int(borrow_person_id):
                index = i
                person_to_borrow = self.people.find(index).item
                break
        if person_to_borrow.is_friend_with(lend_person_id):
            person_to_lend = None
            for j in range(0, self.people.len):
                if self.people.find(j).item.id == int(lend_person_id):
                    index = j
                    person_to_lend = self.people.find(index).item
                    break
            ans = None
            for i in range(0, person_to_lend.current_book.len):
                if person_to_lend.current_book.find(i).item.title == title and person_to_lend.current_book.find(i).item.edition_number == int(edition):
                    ans = person_to_lend.current_book.find(i)
                    person_to_lend.current_book.delete(ans)
                    break
            if ans is None:
                print("Didn't find a book called " + title + " in the possession of " + person_to_lend.name)
            elif ans is not None:
                person_to_borrow.current_book.append(ans.item)
                person_to_borrow.borrowed_book.append(ans.item)
                print("Success!")
        else:
            print("The lender is not a friend with the borrower")

    # setting up a relationship
    def add_friend(self, id_first, id_second):
        first_person = None
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == int(id_first):
                first_person = self.people.find(i)
        second_person = None
        for i in range(0, self.people.len):
            if self.people.find(i).item.id == int(id_second):
                second_person = self.people.find(i)               
        check = True
        for i in range(0, first_person.item.friends.len):
            if first_person.item.friends.find(i).item == second_person.item:
                check = False
                print("Second person is already a friend of the first person.")
                break
        if check:
            first_person.item.add_friend(second_person.item)
            print("Successfully added second person to the friends list of the first person.")

    # sabotage a relationship LOL
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

# initializing simulation data
friendship_one = myFriendship()
# initializing people
for i in range(0, 6):
    person = myPeople.myPeople("Person" + str(i), 100 + i, random.randint(20, 60))
    friendship_one.people.append(person)
# initializing books
for i in range(0, 20):
    for j in range(1, random.randint(1, 3)):
        book = myBooks.myBooks("Book" + str(i), "Simon" + str(i), j)
        friendship_one.books.append(book)
# setting up friendship environment
for i in range(0, friendship_one.books.len):
    friendship_one.people.find(random.randint(0, friendship_one.people.len - 1)).item.current_book.append(friendship_one.books.find(i).item)
friendship_one.get_info()

# first start up menu
def start_up():
    print("\n\nselect an option: ")
    print("---using simulation data above---")
    print("---inappropriate input will cause program to exit---")
    print("---To borrow a book, you must first make the owner your friend")
    menu(friendship_one)

# actual menu for selecting actions
def menu(friendship_one):
    print("[1]create friendships")
    print("[2]deleting friendships")
    print("[3]borrow books")
    print("[4]return books")
    print("[5]check if friend has book")
    print("[6]rank a book")
    print("[7]annotate a book")
    print("[8]--AdministratorOnly--sort people by name")
    print("[9]--AdministratorOnly--sort people by age")
    print("[10]--AdministratorOnly--sort people by id")
    print("[11]--AdministratorOnly--sort people by number of books in possession")
    level_two = input()
    if level_two == "1":
        first_id = input("Your id: ")
        # execution loop in case user wants to execute again
        check = True
        while check:
            second_id = input("The other person's ID: ")
            friendship_one.add_friend(first_id, second_id)
            decision = input("Continue adding friends? y/n ")
            # case when user stops adding friends
            if decision == "n":
                status_check = input("Check system status? y/n ")
                if status_check == "y":
                    friendship_one.get_info()
                    raise SystemExit
                elif status_check == "n":
                    print("\n\n\n")
                    friendship_one.get_info()
                    start_up()
                else:
                    raise SystemExit
    elif level_two == "2":
        first_id = input("Your id: ")
        # execution loop in case user wants to execute again
        check = True
        while check:
            second_id = input("The other person's ID: ")
            friendship_one.delete_friend(first_id, second_id)
            decision = input("Continue deleting friends? y/n")
            # case when user stops deleting friends
            if decision == "n":
                status_check = input("Check system status? y/n ")
                if status_check == "y":
                    friendship_one.get_info()
                    raise SystemExit
                elif status_check == "n":
                    print("\n\n\n")
                    friendship_one.get_info()
                    start_up()
                else:
                    raise SystemExit
    elif level_two == "3":
        borrow_id = input("Your id: ")
        # execution loop in case user wants to execute again
        check = True
        while check:
            lend_id = input("The lender's ID: ")
            title = input("Book title: ")
            edition = input("Book edition: ")
            friendship_one.borrow_book(title, edition, borrow_id, lend_id)
            decision = input("Continue borrowing books? y/n ")
            if decision == "n":
                status_check = input("Check system status? y/n ")
                if status_check == "y":
                    friendship_one.get_info()
                    raise SystemExit
                elif status_check == "n":
                    print("\n\n\n")
                    friendship_one.get_info()
                    start_up()
                else:
                    raise SystemExit
    elif level_two == "4":
        borrow_id = input("Your id: ")
        # execution loop in case user wants to execute again
        check = True
        while check:
            lend_id = input("The lender's ID: ")
            title = input("Book title: ")
            edition = input("Book edition: ")
            friendship_one.return_book(title, edition, borrow_id, lend_id)
            decision = input("Continue deleting books? y/n ")
            # case when user stops deleting books
            if decision == "n":
                status_check = input("Check system status? y/n ")
                if status_check == "y":
                    friendship_one.get_info()
                    raise SystemExit
                elif status_check == "n":
                    print("\n\n\n")
                    friendship_one.get_info()
                    start_up()
                else:
                    raise SystemExit
    elif level_two == "5":
        borrow_id = input("Your id: ")
        # execution loop in case user wants to execute again
        check = True
        while check:
            lend_id = input("The lender's ID: ")
            title = input("Book title: ")
            edition = input("Book edition: ")
            # locating two people
            person_to_borrow = None
            for i in range(0, friendship_one.people.len):
                if friendship_one.people.find(i).item.id == int(borrow_id):
                    index = i
                    person_to_borrow = friendship_one.people.find(index).item
                    break
            if person_to_borrow.is_friend_with(lend_id):
                person_to_lend = None
                for j in range(0, friendship_one.people.len):
                    if friendship_one.people.find(j).item.id == int(lend_id):
                        index = j
                        person_to_lend = friendship_one.people.find(index).item
                        break
                ans = None
                for i in range(0, person_to_lend.current_book.len):
                    if person_to_lend.current_book.find(i).item.title == title and person_to_lend.current_book.find(i).item.edition_number == int(edition):
                        ans = person_to_lend.current_book.find(i)
                        break
                if ans is None:
                    # checking friend's friends if they have the book
                    print("Didn't find a book called " + title + " in the possession of " + person_to_lend.name)
                    friends_friend = input("Do you want to check on friend's friend? y/n ")
                    if friends_friend == "y":
                        friends_book_check = False
                        for i in range(0, person_to_lend.friends.len):
                            for j in range(0, person_to_lend.friends.find(i).item.current_book.len):
                                if person_to_lend.friends.find(i).item.current_book.find(j).item.title == title and person_to_lend.friends.find(i).item.current_book.find(j).item.edition_number == int(edition):
                                    print("Found book in possession of " + person_to_lend.friends.find(i).item.name)
                                    friends_book_check = True
                                    break
                        if not friends_book_check:
                            print("Didn't find the book.")
                elif ans is not None:
                    print("Success! Found book!")
            else:
                print("The lender is not a friend with the borrower")
            decision = input("Continue looking for books? y/n ")
            # case when the user stops looking for books
            if decision == "n":
                status_check = input("Check system status? y/n ")
                if status_check == "y":
                    friendship_one.get_info()
                    raise SystemExit
                elif status_check == "n":
                    print("\n\n\n")
                    friendship_one.get_info()
                    start_up()
                else:
                    raise SystemExit
    elif level_two == "6":
        check = True
        ranker_id = input("Your id: ")
        # execution loop in case user wants to execute again
        while check:
            book_title = input("Book title: ")
            book_edition = input("Book edition number: ")
            value = input("Recommendation value from 1 to 5: ")
            ranker = None
            for i in range(0, friendship_one.people.len):
                if friendship_one.people.find(i).item.id == int(ranker_id):
                    index = i
                    ranker = friendship_one.people.find(index).item
                    break
            # check if user has read the book. cannot rank without reading
            read_the_book = False
            for i in range(0, ranker.borrowed_book.len):
                if ranker.borrowed_book.find(i).item.title == book_title and ranker.borrowed_book.find(i).item.edition_number == int(book_edition):
                    read_the_book = True
                    book_index = i
            if read_the_book:
                ranker.borrowed_book.find(book_index).item.number_of_rank += 1
                ranker.borrowed_book.find(book_index).item.recommendation_value = (ranker.borrowed_book.find(book_index).item.recommendation_value + int(value)) / float(ranker.borrowed_book.find(book_index).item.number_of_rank)
                print("Ranked.")
            else:
                print("You never read the book. Cannot rank. Enter to try again.")
                x = input()
                friendship_one.get_info()
                start_up()
            decision = input("Continue ranking books? y/n ")
            # case when user stops
            if decision == "n":
                status_check = input("Check system status? y/n ")
                if status_check == "y":
                    friendship_one.get_info()
                    raise SystemExit
                elif status_check == "n":
                    print("\n\n\n")
                    friendship_one.get_info()
                    start_up()
                else:
                    raise SystemExit
    elif level_two == "7":
        check = True
        annotator_id = input("Your id: ")
        # execution loop in case user wants to execute again
        while check:
            book_title = input("Book title: ")
            book_edition = input("Book edition number: ")
            value = input("Annotation: ")
            annotator = None
            for i in range(0, friendship_one.people.len):
                if friendship_one.people.find(i).item.id == int(ranker_id):
                    index = i
                    annotator = friendship_one.people.find(index).item
                    break
            # check if user has read the book. cannot annotate without reading
            read_the_book = False
            for i in range(0, ranker.borrowed_book.len):
                if annotator.borrowed_book.find(i).item.title == book_title and annotator.borrowed_book.find(i).item.edition_number == int(book_edition):
                    read_the_book = True
                    book_index = i
            if read_the_book:
                annotator.borrowed_book.find(book_index).item.Annotation = value
                print("Annotated.")
            else:
                print("You never read the book. Cannot annotate. Enter to try again.")
                x = input()
                friendship_one.get_info()
                start_up()
            decision = input("Continue annotating books? y/n ")
            # case when user stops
            if decision == "n":
                status_check = input("Check system status? y/n ")
                if status_check == "y":
                    friendship_one.get_info()
                    raise SystemExit
                elif status_check == "n":
                    print("\n\n\n")
                    friendship_one.get_info()
                    start_up()
                else:
                    raise SystemExit

    # administrator actions that require password
    elif level_two == "8":
        passwd = input("Admin password (found in README.md): ")
        if passwd == "1110":
            reverse = input("Ascending or descending order? a/d ")
            if reverse == "a":
                friendship_one.sort_people_name()
            elif reverse == "d":
                friendship_one.sort_people_name(True)
            else:
                raise SystemExit
    elif level_two == "9":
        passwd = input("Admin password (found in README.md): ")
        if passwd == "1110":
            reverse = input("Ascending or descending order? a/d ")
            if reverse == "a":
                friendship_one.sort_people_age()
            elif reverse == "d":
                friendship_one.sort_people_age(True)
            else:
                raise SystemExit
    elif level_two == "10":
        passwd = input("Admin password (found in README.md): ")
        if passwd == "1110":
            reverse = input("Ascending or descending order? a/d ")
            if reverse == "a":
                friendship_one.sort_people_id()
            elif reverse == "d":
                friendship_one.sort_people_id(True)
            else:
                raise SystemExit
    elif level_two == "11":
        passwd = input("Admin password (found in README.md): ")
        if passwd == "1110":
            reverse = input("Ascending or descending order? a/d ")
            if reverse == "a":
                friendship_one.sort_people_books()
            elif reverse == "d":
                friendship_one.sort_people_books(True)
            else:
                raise SystemExit
    else:
        raise SystemExit
start_up()
