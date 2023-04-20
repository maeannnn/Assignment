from person import Person


class Teacher(Person):
    def __init__(self, idNum, lastName, firstName, middleName, type, department, position):
        Person.__init__(idNum, lastName, firstName, middleName, type)
        self.department = department
        self.position = position

    def getDepartPost(self):
        return f'{self.department}{self.position}'

class Load(Teacher):
    def __init__(self, subjects):
        self.subjects = subjects

    def getSub(self):
        return self.subjects