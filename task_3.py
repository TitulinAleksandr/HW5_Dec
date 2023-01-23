from datetime import datetime


def logger(old_function):

    def new_function(*args, **kwargs):
        # print(f'Вызываем {old_function.__name__} c аргументами {args} и {kwargs}')
        start = datetime.now()
        result = old_function(*args, **kwargs)
        # print(f'Вернули результат {result}')
        # print(start)
        my_text = f'{start}, {old_function.__name__}, {args}, {kwargs}, {result}\n'
        with open("gen.log", "a") as my_file:
            my_file.write(my_text)
        return result

    return new_function

@logger
def flat_generator(list_of_lists):

    for i in list_of_lists:
        for j in i:
            yield j

def test_3():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for item in flat_generator(list_of_lists_1):
        print(item)