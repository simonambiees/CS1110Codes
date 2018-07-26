class myBooks:
    def __init__(self, title, author, edition=1, subject_label="unlabeled"):
        self.title = title
        self.author = author
        self.subject_label = subject_label
        self.edition_number = edition
        self.annotation = None
        self.recommendation_value = 0

    def __str__(self):
        message = self.title + " by " + self.author + " Edition NO." + str(self.edition_number)
        return message

    def set_label(self, label):
        self.subject_label = label
