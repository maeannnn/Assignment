from person import Person


class Student(Person):
    def __init__(self, idNum, lastName, firstName, middleName, type, year, course, section):
        Person.__init__(idNum, lastName, firstName, middleName, type)

        self.year = year
        self.course = course
        self.section = section

    def getYearCourseSection(self):
        return f'{self.year}/{self.course}/{self.section}'


class Grade(Student):
    def __init__(self, introToComputing, archiOrg, sysFun, oop):
        self.introToComputing = introToComputing
        self.archOrg = archiOrg
        self.sysFun = sysFun
        self.oop = oop

    def getAve(self):
        return (int(self.introToComputing) + int(self.archOrg) + int(self.sysFun) + int(self.oop)) / 4
