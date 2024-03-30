opened_classes = [x for x in range(1, 12)]
students_by_classes = {x: [] for x in range(1, 12)}

def add_student(name, grade):
    students_by_classes[grade].append(name)

def del_student(name):
    for grade, students_list in students_by_classes.items():
        if name in students_list:
            students_list.remove(name)
            print(f'Ученик по имени "{name}" успешно удален!')
        else:
            return print(f'Ученик по имени "{name}" не найден.')

def show_all_students():
    all_students = [student for students_list in students_by_classes.items() for student in students_list]
    print(f'Все ученики в школе: {all_students}')

while True:
    action = input('Введите действие: ')
    if action.lower() == 'добавить':
        student_name = input('Введите имя нового ученика: ')
        print(opened_classes)
        students_grade = int(input('Выберите класс для этого ученика: '))
        add_student(student_name, students_grade)
        print(f'Ученик по имени "{student_name}" успешно добавлен в {students_grade} класс!')
    elif action.lower() == 'удалить':
        name_to_del = input('Введите имя ученика для удаления: ')
        del_student(name_to_del)
    elif action.lower() == 'ученики':
        show_all_students()
    else:
        print('Я не понял, что мне делать!')