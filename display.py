import sys

from student import Student, Grade
from teacher import Teacher, Load

student = []
teacher = []


def addStudent():
    while True:
        print()
        print('T = Add Teacher')
        print('S = Add student')
        print()

        add = input('Choose T or S: ')
        add = add.upper()
        print()

        if add == 'S':
            idNum: str = input('Enter ID number: ')
            lastName = input('Enter Last name: ')
            firstName = input('Enter First Name: ')
            middleName = input('Enter Middle name: ')
            type = input('Enter Type: ')
            year = input('Enter Year level: ')
            course = input('Enter Course: ')
            section = input('Enter Section: ')
            print('_____________________________________________________________________________________________________')
            introToComputing = int(input('Enter Introduction to Computing grade: '))
            archOrg = int(input('Enter Architecture and Organization grade: '))
            sysFun = int(input('Enter System Fundamentals grade: '))
            oop = int(input('Enter Object-oriented Programming grade: '))

            student1 = Grade(introToComputing, archOrg, sysFun, oop)
            student1.lastName = lastName
            student1.firstName = firstName
            student1.middleName = middleName
            student1.type = type
            student1.year = year
            student1.course = course
            student1.section = section
            student1.append(student1)


        elif add == 'T':
            idNum = input('Enter ID number: ')
            lastName = input('Enter Last name: ')
            firstName = input('Enter FirstName: ')
            middleName = input('Enter Middle name: ')
            type = input('Enter Type: ')
            print('_____________________________________________________________________________________________________')
            department = input('Enter Department: ')
            position = input('Enter position: ')
            subjects = input('Enter Subjects: ')

            teacher1 = Load(subjects)
            teacher1.department = department
            teacher1.position = position
            teacher1.idNum = idNum
            teacher1.lastName = lastName
            teacher1.firstName = firstName
            teacher1.middleName = middleName
            teacher1.type = type
            teacher1.append(teacher1)

        else:
            menu()

        print()
        answer = input('Enter another? [y/n]: ')
        answer = answer.lower()

        if answer == 'y':
            break
        menu()


def delRecord():
    print()
    print('T = delete from Teacher')
    print('S = delete from Student')
    print('DT = Delete Teacher Record')
    print('DS = Delete Student Record')
    print('C = clear all')
    print()

    delete = input('What do you want to delete? ')
    delete = delete.upper()

    if delete == 'S':
        i: int = int(input('Enter Index number: '))
        student.pop(i)
    elif delete == 'T':
        i: int = int(input('Enter Index number: '))
        teacher.clear()
    elif delete == 'DT':
        teacher.clear()
    elif delete == 'DS':
        student.clear()
    elif delete == 'C':
        student.clear()
        teacher.clear()
    else:
        delRecord()

    menu()


def searRecord():
    print()
    print('T = search for Teacher')
    print('s - Search for Student')
    print()

    search = input('What type do you want to search? ')
    search = search.upper()

    if search == 'S':
        i = int(input('Enter Index number: '))
        print(
            f'{i} \t | {student[i].getType()} \t | {student[i].getName()} \t | {student[i].getID()} \t | {student[i].getYrCrSec()} \t | {student[i].getAve()} ')
    elif search == 'T':
        i = int(input('Enter Index number: '))
        print(
            f'{i} \t | {teacher[i].getType()} \t | {teacher[i].getName()} \t | {teacher[i].getID()} \t | {teacher[i].getDeptPost()} \t | {teacher[i].getSub()}')
    else:
        searRecord()
    menu()


def displayRecord():
    print()
    print('TD = display teacher')
    print('SD - display student')
    print('DA - display all')
    print()

    display1 = input('What type do you want to display? ')
    display1 = display1.upper()

    if display1 == 'SD':
        print()
        print('--------------------------------------------------------------------------------------------------')
        i = 0
        for s in student:
            print(
                f'{i} \t | {student.getType()} \t | {student.getName()} \t | {student.getID()} \t | {student.getYrCrSec()} \t | {student.getAve()}')
            i += 1
            print('----------------------------------------------------------------------------------------------')

    elif display1 == 'TD':
        print()
        print('--------------------------------------------------------------------------------------------------')
        i = 0
        for t in teacher:
            print(
                f'{i} \t | {teacher.getType()} \t | {teacher.getName()} \t | {teacher.getID()} \t | {teacher.DeptPost()} \t | {teacher.getSubject()}')
            i += 1
            print('----------------------------------------------------------------------------------------------')

    elif display1 == 'DA':
        print()
        print('--------------------------------------------------------------------------------------------------')
        i = 0
        for s in student:
            print(
                f'{i} \t | {student.getType()} \t | {student.getName()} \t | {student.getID()} \t | {student.getYrCrSec()} \t | {student.getAve()}')
            i += 1

        i = 0
        for t in teacher:
            print(
                f'{i} \t | {teacher.getType()} \t | {teacher.getName()} \t | {teacher.getID()} \t | {teacher.DeptPost()} \t | {teacher.getSubject()}')
            i += 1
        print('-----------------------------------------------------------------------------------------------------')

    else:
        displayRecord()
    menu()


def menu():
    print('------------------Menu---------------------')
    print('DR - delete record       SR - search record')
    print('A  - add record          M  - display all')
    print()

    choice = input('Enter a function: ')
    choice = choice.upper()

    if (choice == 'DR'):
        delRecord()
    elif (choice == 'A'):
        addStudent()
    elif (choice == 'SR'):
        searRecord()
    elif (choice == 'M'):
        displayRecord()
    else:
        print()


menu()
