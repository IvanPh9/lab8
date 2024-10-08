# Пищик Іван, тім лід, словник та функція додавання студентів до словника
# Функція для додавання студента до словника через введення з клавіатури
def add_student_from_input():
    name = str(input("Введіть прізвище та ім'я: "))
    # Перевірка, чи студент з таким прізвищем таа ім'ям вже є в словнику
    if name in students_data:
        print(f"Студент {name} вже існує!")
        return
    group= str(input("Введіть номер групи: "))
    course = int(input("Введіть курс: "))

    # Введення оцінок за предмети
    subjects_grades = {}
    print("Введіть предмети та оцінки (для завершення введіть 'стоп'): ")
    while True:
        subject = input("Предмет: ")
        if subject.lower() == "стоп":
            break
        grade = int(input(f"Оцінка за {subject}: "))
        subjects_grades[subject] = grade

    # Додаємо студента до словника
    full_name = f"{name}"
    students_data[full_name] = {
        "group": group,
        "course": course,
        "subjects_grades": subjects_grades
    }

# Створюємо порожній словник для зберігання інформації про студентів
students_data = {'Іванов Іван': {'group': "КН-39.1", 'course': 2, 'subjects_grades': {'Пайтон': 97, 'ЧМ': 92, 'ММДО': 99}},
                 'Петрова Софія': {'group': "КН-39.2", 'course': 2, 'subjects_grades': {'Пайтон': 83, 'ЧМ': 72, 'ММДО': 91}},
                 'Піддубна Марія': {'group': "КН-39.1", 'course': 2, 'subjects_grades': {'Пайтон': 81, 'ЧМ': 98, 'ММДО': 61}},
                 'Розумний Ігор': {'group': "КН-39.2", 'course': 2, 'subjects_grades': {'Пайтон': 73, 'ЧМ': 67, 'ММДО': 88}},
                 'Ніжна Ірина': {'group': "КН-39.1", 'course': 2, 'subjects_grades': {'Пайтон': 84, 'ЧМ': 97, 'ММДО': 98}}
                 }

# Виводимо інформацію про студентів(Рожченко Іван: зробив з дії функцію)
def print_students_data():
    print("\nІнформація про студентів:")
    for student, data in students_data.items():
        print(f"{student} (Група {data['group']}, Курс {data['course']}): {data['subjects_grades']}")

# Функція для видалення студента за прізвищем і ім'ям(Рожченко Іван)
def data_remove(key):
    if key in students_data:
        students_data.pop(key)
        print(f"{student} видалений/на зі списку студентів")
    else:
        print("<--Студента/ку не знайдено-->")

# Наступний студент: додати функцію видалення по прізвищу та ім'ям, організувати діалог між користувачем та програмою(Рожченко Іван)

# Діалог з користувачем(Рожченко Іван)
number = 0
while True:
    if number == 0:
        print("\n<1>Вивести список студентів"
            "\n<2>Додати студента/ку"
            "\n<3>Видалити студента/ку"
            "\n<0>Завершити програму")
        number += 1
    answer = int(input("\nВиберіть дію: "))
    if answer == 0:
        break;
    elif answer == 1:
        print_students_data()
    elif answer == 2:
        add_student_from_input()
    elif answer == 3:
        student = str(input("Введіть прізвище і ім'я: "))
        data_remove(student)
    else:
        print("Помилка введення")
print("Програму завершено")

# Наступний студент: додати функцію обрахунку середнього балу студента за прізвищем, додати відповідну дію до діалогу