import myList


"git.enableSmartCommit": true,
    "explorer.confirmDelete": false,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length=120",
        "--ignore=E402,F841,F401,E302,E305,E501,W293",
    ],

class myPeople:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.name = name
        self.current_book = myList.myList()
        self.borrowed_book = myList.myList()
        self.lent_book = myList.myList()
        self.friends = myList.myList()
    
    def __str__(self):
        message = "Name: " + self.name + "  ID: " + str(self.id) + "\n    Who has books:\n"
        for i in range(0, self.current_book.len):
            message += "        " + str(self.current_book.find(i).item) + "\n"
        message += "    Who borrowed books:\n"
        for j in range(0, self.borrowed_book.len):
            message += "        " + str(self.borrowed_book.find(j).item) + "\n"
        message += "    Who has friends:\n"
        for k in range(0, self.friends.len):
            message += "        " + str(self.friends.find(k).item.name) + "\n"
        return message
        
    def return_book(self, title, edition):
        ans = None
        for i in range(0, self.current_book.len):
            if self.current_book.find(i).item.title == title and self.current_book.find(i).item.edition_number == edition:
                ans = self.current_book.find(i)
                self.current_book.delete(ans)
                break
        if ans is None:
            print("Didn't find a book called " + title + " in the possession of " + self.name)
        return ans
        
    def add_friend(self, person):
        self.friends.append(person)

    def find_book(self, title, edition):
        ans = None
        for i in range(0, self.current_book.len):
            if self.current_book.find(i).item.title == title & self.current_book.find(i).edition_number == edition:
                ans = self.current_book.find(i)
        if ans is None:
            print("Didn't find a book called " + title + " in the possession of " + self.name)
        return ans
