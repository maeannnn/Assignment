class Person:

    def __init__(self, idNum, lastName, firstName, middleName, type):
        self.idNum = idNum
        self.lastName = lastName
        self.firstName = firstName
        self.middleName = middleName
        self.type = type

    def getIdNum(self):
        return self.idNum

    def getName(self):
        return self.lastName
        return self.firstName
        return self.middleName

    def getType(self):
        return self.type
    


