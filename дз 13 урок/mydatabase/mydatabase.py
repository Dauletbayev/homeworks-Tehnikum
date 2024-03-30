import sqlite3

conn = sqlite3.connect('mydatabase.db')
sql = conn.cursor()

# sql.execute("CREATE TABLE students(id INTEGER, name TEXT, age INTEGER, grade TEXT);")
# sql.execute('INSERT INTO students VALUES (4, "Pavel", 17, "3")')

def all_students():
    all_info = sql.execute('SELECT * FROM students').fetchall()
    for info in all_info:
        print(info)
def get_student_by_name(search_name):
    sql.execute('SELECT * FROM students WHERE name=?', (search_name,))
    print(sql.fetchone())

def update_student_grade(name_search, new_grade):
    sql.execute('UPDATE students SET grade=? WHERE name=?', (new_grade, name_search))
    sql.execute('SELECT * FROM students WHERE name=?', (name_search,))
    print(sql.fetchone())

def delete_student(del_name):
    sql.execute('DELETE FROM students WHERE name=?', (del_name,))
    print(f'Ученик по имени "{del_name}" успешно удален!')

conn.commit()

while True:
    action = input('Введите действие: ')
    if action.lower() == 'поиск':
        name_to_search = input('Введите имя для поиска: ')
        get_student_by_name(name_to_search.title())
    elif action.lower() == 'все ученики':
        all_students()
    elif action.lower() == 'обновить':
        name_to_search = input('Введите имя ученика: ')
        grade = input('Введите новую оценку: ')
        update_student_grade(name_to_search.title(), grade)
    elif action.lower() == 'удалить':
        name_to_del = input('Введите имя для удаления: ')
        delete_student(name_to_del.title())
    else:
        print('Не понял!')

conn.close()
