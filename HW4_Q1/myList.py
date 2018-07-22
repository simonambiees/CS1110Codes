import myItem


class myList:
    def __init__(self):
        self.start = myItem.myItem("")
        self.len = 0

    def find(self, num):
        i = 0
        ans = self.start.next
        while i < num:
            ans = ans.next
            i += 1
        return ans

    def append(self, item):
        if self.len == 0:
            self.start.next = myItem.myItem(item)
        else:
            self.find(self.len - 1).next = myItem.myItem(item)
        self.len += 1

    def delete(self, item):
        if self.len == 0:
            print("no item in the list")
        else:
            for i in range(0, self.len):
                if self.find(i) == item:
                    index = i
            if index == 0:
                self.start.next = self.find(index + 1)
                self.len -= 1
            else:
                if index < self.len:
                    self.find(index - 1).next = self.find(index + 1)
                elif index == self.len:
                    self.find(index - 1).next = None

    def has(self, item):
        has = False
        for i in range(0, self.len):
            if self.find(i) == item:
                has = True
                break

    def __len__(self):
        return self.len
