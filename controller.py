import view
import model
#n = view.menu()
def klick_menu(number):

        if number == 1:
            return model.print_phone_book()
            #print('\n---------------------------------------------------------------------------------')
            #n = view.menu()
        elif number == 4:
            g = model.new_user()
            return g
            #print(f'вы добавили нового пользователя \n{g}')
            #print('\n---------------------------------------------------------------------------------')
            #n = view.menu()
        elif number == 5:
            #print('\n---------------------------------------------------------------------------------')
            return view.output('Спасибо за работу со справочником')
        elif number == 2:
            first_name = input('введите имя пользователя, которого хотите найти Name = ')
            second_name = input('введите фамилию пользователя, которого хотите найти')
            answer = model.find_number_phone(first_name, second_name)
            return view.output(answer)
            #print('\n---------------------------------------------------------------------------------')
            #n = view.menu()
        elif number == 3:
            phone_search = input('введите номер телефона пользователя Phone_number = ')
            answer = model.find_name_user(phone_search)
            return view.output(answer)
            #print('\n---------------------------------------------------------------------------------')
            #n = view.menu()

        else:
            return view.output('спасибо за работу со справочником')

