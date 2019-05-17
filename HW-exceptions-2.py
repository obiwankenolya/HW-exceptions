documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "3244324"},
    {"type": "passport", "number": "9384028", "name": "Брюс Уэйн"},

]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;

def get_document_owner(people):
    user_input = input('Введите номер документа: ')
    name = 0
    for person in people:
        if user_input == person['number']:
            print(person['name'])
            name += 1
    if name == 0:
        print('Документ не найден')


# get_document_owner(documents)


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";

def get_documents_info(people):
    for person in people:
        print(person['type'], person['number'], person['name'])


# get_documents_info(documents)


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;

def get_shelf_number_by_document_number(shelves):
    shelf = 0
    user_input = input('Введите номер документа: ')
    for shelf_num, document in shelves.items():
        if user_input in document:
            shelf += 1
            print(shelf_num)
    if shelf == 0:
        print('Документ не найден ни на одной из полок')


# get_shelf_number_by_document_number(directories)


# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.

def add_document_and_shelf(people, shelves):
    doc_num = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    owners_name = input('Введите имя владельца документа: ')
    shelf_num = input('Введите номер полки: ')
    documents.append({"type": doc_type, "number": doc_num, "name": owners_name})
    if shelf_num in directories.keys():
        directories[shelf_num].append(doc_num)
    else:
        directories[shelf_num] = list()
        directories[shelf_num].append(doc_num)
    print(documents)
    print()
    print(directories)


# add_document_and_shelf(documents, directories)


def get_all_names(people):
    for document in documents:
        try:
            document["name"]
        except KeyError:
            print('У документа нет владельца')
        else:
            print(document["name"])

# get_all_names(documents)


def main():
    user_input = input('Введите команду: ')
    if user_input == 'p':
        get_document_owner(documents)
    elif user_input == 'l':
        get_documents_info(documents)
    elif user_input == 's':
        get_shelf_number_by_document_number(directories)
    elif user_input == 'a':
        add_document_and_shelf(documents, directories)
    elif user_input == 'n':
        get_all_names(documents)

    else:
        print('Несуществующая команда')


main()
