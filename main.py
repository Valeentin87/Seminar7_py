# модуль для управления вводом пользователем
def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('Введите номер опции,которой хотите воспользоваться')
    print('1. Показать весь справочник')
    print('2. Найти номер телефона по имени или фамилии')
    print('3. Найти пользователя по номеру телефона')
    print('4. Добавить нового пользователя в справочник')
    print('5. Выход из справочника')
    number_menu = int(input('пункт меню = '))
    while(number_menu > 5 or number_menu < 1):
        print('введите корректное значение функции меню')
        number_menu = int(input('N = '))
    return number_menu
# модуль поиска номера телефона по имени и фамилии

def find_number_phone(name, surname):
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        for line in data:
            string_pars = line.split(sep = ',')
            if name == string_pars[0] and surname == string_pars[1]:
                find_number = string_pars[2] + ' ' + string_pars[3]
                return find_number
        result = f'пользователь {name, surname} в справочнике не числится'
        return result
# модуль для поиска Фамилии и Имени по номеру телефона
def find_name_user(phone_number):
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        for line in data:
            string_pars = line.split(sep=',')
            if phone_number == string_pars[2] :
                find_name = string_pars[0] + ' ' + string_pars[1]
                return find_name
        result = f'пользователь c номером телефона {phone_number} в справочнике не числится'
        return result

# модуль для записи нового пользователя
def new_user():
    data = ['имя', 'фамилия', 'номер телефона', 'тип телефона']
    user = ['','','','']
    for i in range(4):
        user[i] = str(input(f'введите {data[i]} '))
    new_user = ','.join(user)
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.write('\n'+ new_user)
    return new_user


# модуль для распечатывания всего справочника
def print_phone_book():
    with open('phone_book.txt', 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end= '')

n = menu()
while n!=5:
    if n == 1:
        print_phone_book()
        print('\n---------------------------------------------------------------------------------')
        n = menu()
    elif n == 4:
        g = new_user()
        print(f'вы добавили нового пользователя \n{g}')
        print('\n---------------------------------------------------------------------------------')
        n = menu()
    elif n == 5:
        print('\n---------------------------------------------------------------------------------')
        print('Спасибо за работу со справочником')
    elif n == 2:
        first_name = input('введите имя пользователя, которого хотите найти Name = ')
        second_name = input('введите фамилию пользователя, которого хотите найти')
        answer = find_number_phone(first_name, second_name)
        print(answer)
        print('\n---------------------------------------------------------------------------------')
        n = menu()
    elif n == 3:
        phone_search = input('введите номер телефона пользователя Phone_number = ')
        answer = find_name_user(phone_search)
        print(answer)
        print('\n---------------------------------------------------------------------------------')
        n = menu()

    else:
        print('работа над программой ведется')
        break
print('спасибо за работу со справочником')








