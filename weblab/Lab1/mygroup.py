groupmates = [
    {
        "name": "Елена",
        "surname": "Антипова",
        "exams": ["ТАП", "ЭС", "Web"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Иван",
        "surname": "Смирнов",
        "exams": ["УП", "ТАП", "КТП"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Петр",
        "surname": "Иванов",
        "exams": ["История", "Философия", "КТП"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Илья",
        "surname": "Петров"
        "exams": ["История", "УП", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "ЭС", "КТП"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)
