from teacher import Teacher


class Load(Teacher):
    def __init__(self, subjects):
        self.subjects = subjects

    def getSub(self):
        return self.subjects