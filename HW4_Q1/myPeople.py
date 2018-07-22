import myList

class myPeople:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.current_book = myList()
        self.borrowed_book = myList()
        self.friends = myList()
    
    def add_current_book(self, book):
        self.current_book.append(book)
        self.borrowed_book.append(book)

    def delete_current_book(self, book):
        self.current_book.delete(book)

    def add_friend(self, person):
        self.friends.append(person)

    def check_friendship(self, person):
        return self.friends.has(person)
