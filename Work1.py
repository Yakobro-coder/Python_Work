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

print('Помощник по документообороту v1.0')

def p_people():
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

def a_add():
    number_shelf = 0
    new_doc = {}
    new_doc['type'] = input('ВВедите тип документа: ')
    new_doc['number'] = input('ВВедите номер документа: ')
    new_doc['name'] = input('ВВедите ФИО владельца документов: ')
    while number_shelf == 0:
        number_shelf = int(input('Документ добавлен в каталог. На какой полке он будет хранится: '))
        if number_shelf < 0 or number_shelf > len(directories):
            print(f'Полки с номером "{number_shelf}", не существует. Введите номер полки коректно.')
            print(f'На данный момент у вас {len(directories)} полки.')
            number_shelf = 0
    documents.append(new_doc)
    directories[str(number_shelf)].append(new_doc['number'])
    print(f'Документ "{" ".join(new_doc.values())}" добавлен и хранится на полке №{number_shelf}.')

def d_delete():
    error = 0
    while error == 0:
        b = input('Введите номер документа: ')
        for number, dct1 in enumerate(list(documents)):
            error += 1
            if dct1['number'] == b:
                print(f'Документ "{" ".join(dct1.values())}" удален из каталога и с полки хранения.')
                print(documents)
                del(documents[number])
                error += 1
                print(documents)
                for key, val in list(directories.items()):
                    for number_position, number_doc in enumerate(val):
                        if number_doc == b:
                            print(directories)
                            del(directories[key][number_position])
                            print(directories)
        if len(dct1) == error:
            print('Такой документ не найден. Проверьте номер документа.')
            error = 0

# def m_move():


# def as_add_shelf():


def vvod():
    a = input('Введите команду:')
    if a == 'p':
        number_doc()

d_delete()