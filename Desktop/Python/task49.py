'''Задача №49.
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')   #читаем файл ( в папке должен быть прикреплен этот файл(phonebook.txt))

    while (choice != 7):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new number ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            lastname = input('lastname ')
            print(delete_by_lastname(phone_book, lastname))
        elif choice == 5:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt, phone_book')  #сохранение

def show_menu():   #всегда вызываем
    print("\n Выберите необходимое действие: \n"
          "1. Отобразить весь справочник \n"
          "2. Найти абонента по фамилии \n"
          "3. Найти абонента по номеру телефона \n"
          "4. Добавить абонента в справочник \n"
          "5. Изменить данные \n"
          "6. Сохранить справочник в текстовом формате \n"
          "7. Закончить работу \n")
    choice = int(input())    # берет введенную пользователем цифру, находит ее и возвращает
    return choice

# 1 значение  2 значение  3 значеине  4 зачение
# Иванов,     Иван,       111,        описание Иванова
# Петров,     Петр,       222,        описание Петрова
# Васичкина,  Василиса,   333,        описание Васичкиной
# Питонов,    Антон,      777,        умеет в Питон
# 555,        333,        789,         dfdf

# def read_txt(filename):
#     phone_book = []   # Создаем пустой список
#     fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']  # Создаем оглавление
#             #phonebook.txt   кодировка файла   открываем в новой переменной phb
#     with open(filename, 'r', encoding='utf-8') as phb:  # загружаем файл с помощью контекстного меню
#                       #чтение и открытие файла
#         for line in phb:  # перебираем наш файл(принимает значение(Иванов, Иван))
#             record = dict(zip(fields, line.split(',')))  # создаем словарь(список из словарей) после zip вставляем элементы из списка
#                 dict(((Фамилия, Иванов), (Имя, Точка), (Номер, 8928)))  #внутрь словаря закидываем кортеджи(ключ, значение(фамилия, Иванов))
#         phone_book.append(record) # записывем человеа в список
#     return phone_book    #возвращаем список

# def write_txt(filename, phone_book):
#     with open('phonebook.txt', 'w', encoding='utf-8') as phout:  #появится файл
#         for v in range(len(phone_book)):                         #перебираем индекс нашего списка который состоит из словарей
#             s = ''                                         #создаем пустую строку
#             for v in phone_book[i].values():               # phone book[i] это 1 контакт в словаре
#                 s+=v+ ','                                 # собираем нашу строку
#             phout.write(f'{s[:-1]}\n')                #записываем с каждлй новой строки
#         #                 обрезаем последний симбвол
            

#readline построчно 