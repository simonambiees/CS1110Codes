import myItem


class myList:
    def __init__(self):
        self.start = None
        self.len = 0

    def find(self, num):
        i = 0
        ans = self.start
        while i < num:
            ans = ans.next
            i += 1
        return ans

    def append(self, item):
        if self.len == 0:
            self.start = myItem.myItem(item)
        else:
            self.find(self.len - 1).next = myItem.myItem(item)
        self.len += 1

    def delete(self, item):
        if self.len == 0:
            print("no item in the list")
        else:
            for i in range(0, self.len - 1):
                if self.find(i) == item:
                    for j in range(i, self.len):
                        self.find(j - 1).next = self.find(j + 1)
                    self.len -= 1
                    break

    def has(self, item):
        has = False
        for i in range(0, self.len):
            if self.find(i) == item:
                has = True
                break

    def __len__(self):
        return self.len
