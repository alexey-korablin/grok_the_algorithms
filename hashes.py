# В Python роль хэш-таблиц играют словари


def simple_book():
    book = dict()
    book['apple'] = 0.67
    book['milk'] = 1.49
    book['avocado'] = 1.49

    print(book)
    print(book['avocado'])


simple_book()


def prepare_phone_book():
    book = dict()
    book['jenny'] = 8675309
    book['emergency'] = 911
    return book


def create_phone_book(name):
    phone_book = prepare_phone_book()
    result = phone_book.get(name)

    if not result:
        phone_book[name] = input('Please input the phone number: ')
        result = phone_book.get(name)

    return {'name': name, 'number': result}


print(create_phone_book('jenny'))
print(create_phone_book('peter'))

