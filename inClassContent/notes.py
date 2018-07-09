'''class Person:
    '''This class will allow me to make people!
    object attributes: my_name, my_gender, my_age, my_friends'''
    def __init__(self,name,gender,age):
        self.my_name = name
        self.my_gender = gender
        self.my_age = age
        self.my_friends = []
    def person_kind(): # WHY NO self?
        if self.my_gender[0] == 'm':return 'lad'
        elif self.my_gender[0] == 'f':return 'lass'
        else: return 'martian'
    def introduce_myself(self): # WHY HAVE self?
        print("Hi, I'm " + self.my_name+", and I'm a "+ str(self.my_age)+"-year-old "+self.person_kind())
    def add_friend(nice_person):
        self.my_friends.append(nice_person)
    def show_friends():
        return self.my_friends
        
Simon = Person("Simon", "male", 17)
Betty = Person("Betty", "female", 17)
print(Simon.my_age)
print(Betty.introduce_myself())'''

class Chair:
    def __init__(self, person = None, next = None):
        self.my_person = person
        self.next = next
    def set_data(self, person):
        self.my_person = person
    def get_date(self):
        return self.my_person
    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next
