from myList import myList
from myItem import myItem

class MB:
    def __init__(self, friendship):
        self.friendship = friendship
        pass

    def sort_people(self, sort_by_name=False, sort_by_id=False, sort_by_age=False, sort_by_book=False, reverse=False):
        people_list = self.friendship.get_people_list()
        if people_list.len <= 1:
            return people_list
        cur = people_list.start.next.next
        while cur is not None:
            p = people_list.start.next
            x = cur.item
            if sort_by_age:
                while p is not cur and (p.item.age >= x.age) ^ reverse:
                    p = p.next
            elif sort_by_name:
                while p is not cur and (p.item.name <= x.name) ^ reverse:
                    p = p.next
            elif sort_by_book:
                while p is not cur and (p.item.current_book.len >= x.current_book.len) ^ reverse:
                    p = p.next
            elif sort_by_id:
                while p is not cur and (p.item.id <= x.id) ^ reverse:
                    p = p.next
            else:
                break
            while p is not cur:
                tmp = x
                x = p.item
                p.item = tmp
                p = p.next
            cur = cur.next
        return people_list

    def sort_book(self, sort_by_title=False, sort_by_author=False, reverse=False):
        book_list = self.friendship.get_books_list()
        if book_list.len <= 1:
            return book_list
        cur = book_list.start.next.next
        while cur is not None:
            p = book_list.start.next
            x = cur.item
            if sort_by_title:
                while p is not cur and (p.item.title <= x.title) ^ reverse:
                    p = p.next
            elif sort_by_author:
                while p is not cur and (p.item.author <= x.author) ^ reverse:
                    p = p.next
            else:
                break
            while p is not cur:
                tmp = x
                x = p.item
                p.item = tmp
                p = p.next
            cur.item = x
            cur = cur.next
        return book_list
        pass
