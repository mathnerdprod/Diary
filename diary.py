# imports
import sys
from diary_classes import Student

students = [Student(name='Denys', surname='Potomkin', age=18),
            Student(name='Lena', surname='Partyka', age=17)]

def add_students(students: list) -> None:
    name = input('Enter student name: ')
    surname = input('Enter student surname: ')
    try:
        age = int(input('Enter student age: '))
    except ValueError:
        print('Invalid input')
        return
    add_student = Student(name, surname, age)
    students.append(add_student)
    print(f'Student {add_student.name} {add_student.surname} added')

def delete_students(students: list) -> None:
    for i, student in enumerate(students, 1):
        print(f'- {i}. {student}')
    student_id = input(f'Choose student: ')
    try:
        student_id = int(student_id) - 1
        try:
            del students[student_id]
        except IndexError:
            print('Invalid student number')
            return
    except ValueError:
        print('Invalid input')
        return

def add_grades(students: list) -> None:
    for i, student in enumerate(students, 1):
        print(f'- {i}. {student}')
    student_id = input(f'Choose student: ')
    try:
        student_id = int(student_id) - 1
        if not 0 <= student_id < len(students):
            print('Invalid student number')
            return
    except ValueError:
        print('Invalid input')
        return
    classes = input(f'Choose classes: '
                    f'\n - 1. Math'
                    f'\n - 2. Physics'
                    f'\n - 3. Chemistry\n')
    try:
        classes = int(classes)
    except ValueError:
        print('Invalid input')
        return
    grade = input(f'Enter grade: ')
    try:
        grade = float(grade)
        if not 1 <= grade <= 6:
            print('Grade must be between 1 and 6')
            return
    except ValueError:
        print('Invalid input')
        return
    if classes == 1:
        students[student_id].math.append(grade)
    elif classes == 2:
        students[student_id].physics.append(grade)
    elif classes == 3:
        students[student_id].chemistry.append(grade)
    else:
        print('Invalid input')
        return

def print_grades(students: list) -> None:
    for i in range(len(students)):
        print(f'- {i + 1}. {students[i]}')
    student_id = input(f'Choose student: ')
    try:
        student_id = int(student_id) - 1
    except ValueError:
        print('Invalid input')
        return
    print(f'Student {students[student_id].name} {students[student_id].surname} grades:\\n'
          f'Math: {students[student_id].math}\\n'
          f'Physics: {students[student_id].physics}\\n'
          f'Chemistry: {students[student_id].chemistry}\\n')

def main():
    print(f'{students}')
    choose = input(f'What do you want to do?'
                   f'\n - 1. Add new student'
                   f'\n - 2. Delete student'
                   f'\n - 3. Add new grade'
                   f'\n - 4. Print grades'
                   f'\n - 5. Exit\n')
    # check for stupids
    try:
        choose = int(choose)
    except ValueError:
        print('Invalid input')
        return
    # trying
    try:
        # add student
        if choose == 1:
            add_students(students)
        # delete student
        elif choose == 2:
            delete_students(students)
        # add new grade
        elif choose == 3:
            add_grades(students)
        # print grades
        elif choose == 4:
            print_grades(students)
        # exit
        elif choose == 5:
            sys.exit(0)

    # excepts...
    except (KeyboardInterrupt, SystemExit):
        print('Exit')
# we hate recursion
while True:
    main()