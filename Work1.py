documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def vvod():
    helper = '''
                                 Помощник по документообороту v1.0
                 Данная программа помощник для реализации ведения и хранения документов. 
            Программа напомнит вам какой документ кому принадлежит, и на какой полке он хранится.
    
                              Программа осуществляет следующие функции:
    p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    s – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    l – команда, которая выведет список всех документов в формате "passport 2207 876234 Василий Андреевич";
    sh - команда, котрая выведет количество полок, и какие документы на ней хранятся.
    a – команда, которая добавит новый документ в каталог и в перечень полок, спросив номер документа, тип,
    имя владельца и номер полки, на котором он будет храниться;
    d – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – команда, которая спросит номер новой полки и добавит ее в перечень.
    
    exit - Команда для выхода из программы.
    help - что бы посмотреть перечень команд.
    
    Внимание: p, s, l, sh, a, d, m, as, exit, help - это команды, которы вам надо вветси.
    Пример: Вы хотите узнать по номеру документа, кому пренадлежит документ(это команда p).
    Вам необходимо ввести команду в поле ввода. "Введите команду: p"; 
    '''
    print(helper)
    command_enter = True
    while command_enter:
        command = input('\nВведите команду: ')
        if command == 'p':
            p_people()
        elif command == 's':
            s_shelf()
        elif command == 'l':
            l_list_all_doc()
        elif command == 'sh':
            sh_directories()
        elif command == 'a':
            a_add()
        elif command == 'd':
            d_delete()
        elif command == 'm':
            m_move()
        elif command == 'as':
            as_add_shelf()
        elif command == 'help':
            print(helper[261:1269:])
        elif command == 'exit':
            command_enter = False
        else:
            print('Вы ввели не верную команду. Напишите команду help что бы ознакомиться со спсиком команд.')


def p_people():
    """
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит.
    """
    error = 0
    while error == 0:
        b = input('Введите номер документа: ')
        for dct1 in documents:
            error += 1
            if dct1['number'] == b:
                print(f'Документ на имя: {dct1["name"]}')
                error += 1
        if len(dct1) == error:
            print('Такой документ не найден. Проверьте номер документа.')
            error = 0


def s_shelf():
    error = 0
    while error == 0:
        b = input('Введите номер документа: ')
        for key, val in directories.items():
            error += 1
            if b in val:
                print(f'Полка номер: {key}')
                error += 1
        if len(directories) == error:
            print('Такой документ не найден. Проверьте номер документа.')
            error = 0


def l_list_all_doc():
    for dct1 in documents:
        print(f'- {" ".join(dct1.values())}.')


def sh_directories():
    for key, val in directories.items():
        print(f'Полка {key} с документами: {val}')


def a_add():
    number_shelf = 0
    new_doc = {}
    new_doc['type'] = input('ВВедите тип документа: ')
    new_doc['number'] = input('ВВедите номер документа: ')
    new_doc['name'] = input('ВВедите ФИО владельца документов: ')
    while number_shelf == 0:
        number_shelf = int(input('Документ добавлен в каталог. На какой полке он будет хранится: '))
        if number_shelf < 0 or number_shelf > len(directories):
            print(f'Полки с номером "{number_shelf}", не существует. Введите номер полки корректно.')
            print(f'На данный момент у вас {len(directories)} полки.')
            number_shelf = 0
    documents.append(new_doc)
    directories[str(number_shelf)].append(new_doc['number'])
    print(f'Документ "{" ".join(new_doc.values())}" добавлен и хранится на полке №{number_shelf}.')


def d_delete():
    error = 0
    while error == 0:
        b = input('Введите номер документа для его удаления: ')
        if b == '-1':
            error = 1
        else:
            for number, dct1 in enumerate(list(documents)):
                error += 1
                if dct1['number'] == b:
                    print(f'Документ "{" ".join(dct1.values())}" удален из каталога и с полки хранения', end=' ')
                    del(documents[number])
                    error += 1
                    for key, val in list(directories.items()):
                        for number_position, number_doc in enumerate(val):
                            if number_doc == b:
                                print(f'№{key}.')
                                del(directories[key][number_position])
            if len(dct1) == error:
                print('Такой документ не найден. Проверьте номер документа. Для выхода введите: -1')
                error = 0


def m_move():
    true_doc = True
    true_shelf = False
    error = 0
    while true_doc:
        b = input('Введите номер документа: ')
        for key, val in list(directories.items()):
            for number_position, number_doc in enumerate(val):
                error += 1
                if number_doc == b and true_shelf == False and true_doc == True:
                    print(f'Документ  №{number_doc} найден на полке №{key}')
                    del (directories[key][number_position])
                    true_shelf = True
                    true_doc = False
                if len(directories) == error and true_doc == True:
                    print('Такой документ не найден. Проверьте номер документа.')
                    error = 0
                while true_shelf:
                    number_shelf = int(input('Введите номер полки, куда переместить документ: '))
                    if number_shelf <= len(directories):
                        directories[str(number_shelf)].append(number_doc)
                        print(f'Документ {number_doc} перенесён на полку {number_shelf}.')
                        true_shelf = False
                    else:
                        print(f'Полки с номером {number_shelf} не существует. '
                              f'\nУ вас от 1 до {len(directories)} полок. Выбирите одну их них.')


def as_add_shelf():
    true_test = True
    print(f'На данный момент количетсова ваших полок: {len(directories)} шт.')
    while true_test:
        add_shelf = input('Хотите добавть ещё одну полку?(ДА введите +; НЕТ -) Ввод: ')
        if add_shelf == '+':
            directories.setdefault(str(len(directories)+1), [])
            print(f'{len(directories)}-я полка добавлена.')
            true_test = False
        elif add_shelf == "-":
            true_test = False
            pass
        else:
            print('Вы ввели что то кроме + или -. Определитесь :)')


vvod()
