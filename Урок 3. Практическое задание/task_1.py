"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from time import time

def work_time(func):
    '''Decorator for time calc'''
    def inner_func(*args, **kwargs):
        """Wrapper"""
        start_t = time()
        res = func(*args, **kwargs)
        print(f'Runnig time of {func} is { time()-start_t}')
        return res
    return inner_func

@work_time
def create_lst(n):
    """ list comprehensions"""
    return  list(range(n))

@work_time
def create_dict(n):
    """Dict comprehensions"""
    return {x:x for x in range(n)}

@work_time
def for_create_lst(n):
    """Itteration list"""
    my_lst = []
    for i in range(n):
        my_lst.append(i)
    return my_lst

@work_time
def for_create_dict(n):
    """Itteration dict"""
    my_dict = {}
    for i in range(n):
        my_dict[i] = i
    return

@work_time
def lst_reverse(in_lst):
    in_lst.reverse()
    return

@work_time
def lst_remove(in_lst, el):
    in_lst.remove(el)
    return

@work_time
def dict_get(in_dict, key):
    return in_dict.get(key)

lst_1 = create_lst(10000000)
for_create_lst(10000000)
dict_1 = create_dict(10000000)
for_create_dict(10000000)
print(lst_1[:10])
lst_reverse(lst_1)
print(lst_1[:10])
lst_remove(lst_1,50000)
dict_get(dict_1, 50000)
dict_1.pop(50000)
dict_get(dict_1, 50000)