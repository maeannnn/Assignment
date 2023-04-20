from student import Student


class Grade(Student):
    def __init__(self, introToComputing, archiOrg, sysFun, oop):
        self.introToComputing = introToComputing
        self.archOrg = archiOrg
        self.sysFun = sysFun
        self.oop = oop

    def getAve(self):
        return (int(self.introToComputing) + int(self.archOrg) + int(self.sysFun) + int(self.oop)) / 4
