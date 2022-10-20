import  view
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
    phone_number = input('введите номер телефона для поиска пользователя')
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
        print('\n---------------------------------------------------------------------------------')

