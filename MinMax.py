# def min(*args, **kwargs):
#     key = kwargs.get("key", None)
#     return None
#
#
# def max(*args, **kwargs):
#     key = kwargs.get("key", None)
#     return None

def min(arg1, *args, default=None, key=lambda x: x):
    if args:
        # Если у нас список аргументов, то не церемонимся
        # и начинаем сразу с первого элемента
        result = arg1
        started = True
        iterable = args
    else:
        # Если у нас iterable первым аргументом, то
        # поцеремонимся и начнём в цикле for (это позволяет
        # избавиться от обращения по индексу)
        result = default
        started = False
        iterable = arg1
    # Проходимся по элементам iterable-объекта
    for item in iterable:
        if not started:
            # Если первого элемента ещё не существует,
            # то ставим его
            result = item
            started = True
            continue
        # Если предыдущий элемент существует, то сравниваем
        if key(item) < key(result):
            result = item
    return result

def max(arg1, *args, default=None, key=lambda x: x):
    if args:
        # Если у нас список аргументов, то не церемонимся
        # и начинаем сразу с первого элемента
        result = arg1
        started = True
        iterable = args
    else:
        # Если у нас iterable первым аргументом, то
        # поцеремонимся и начнём в цикле for (это позволяет
        # избавиться от обращения по индексу)
        result = default
        started = False
        iterable = arg1
    # Проходимся по элементам iterable-объекта
    for item in iterable:
        if not started:
            # Если первого элемента ещё не существует,
            # то ставим его
            result = item
            started = True
            continue
        # Если предыдущий элемент существует, то сравниваем
        if key(item) > key(result):
            result = item
    return result

print(min(2,3,4,1))
print(max(2,3,4,5,6,9))
# help(min)
