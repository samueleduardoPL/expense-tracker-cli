import datetime

class expense: 

    def __init__(self, id,description, amount):
        self.id = id
        self.description = description
        self.amount = amount
        self.month = datetime.datetime.now().strftime("%m")
        self.year = datetime.datetime.now().year



