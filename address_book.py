import pandas as pd
#Создаём адресную книгу
book = pd.DataFrame(columns=['ФИО', 'Адрес', 'Телефон', 'Дата рождения'])
while True:
    print("\n1 - добавить запись")
    print("2 - удалить запись")
    print("3 - изменить запись")
    print("4 - показать книгу")
    print("5 - закончить редактирование")
    l= input("Выберите действие: ")
    if l == '1':
        f = input("Введите ФИО: ")
        a = input("Введите адрес: ")
        t = input("Введите телефон: ")
        d = input("Введите дату рождения: ")
        o = pd.DataFrame([{'ФИО': f, 'Адрес': a,
                                 'Телефон': t, 'Дата рождения': d}])
        book = pd.concat([book,o], ignore_index=True)
        print("Запись добавлена.")

    elif l == '2':
        print(book)
        i = int(input("Введите индекс записи для удаления: "))
        if i in book.index:
            book = book.drop(i).reset_index(drop=True)
            print("Запись удалена.")
        else:
            print("Такой записи нет.")

    elif l == '3':
        print(book)
        i = int(input("Введите индекс записи для изменения: "))
        if i in book.index:
            field = input("Что изменить (ФИО/Адрес/Телефон/Дата рождения): ")
            if field in book.columns:
                book.at[i, field] = input("Новое значение: ")
                print("Запись изменена.")
            else:
                print("Неверное поле.")
        else:
            print("Такой записи нет.")

    elif l == '4':
        print(book)

    elif l == '5':
        print("Работа завершена.")
        break
    else:
        print("Неверный пункт меню.")
