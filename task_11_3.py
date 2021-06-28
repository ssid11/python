class MyTypeError(TypeError):
    def __init__(self):
        self._msg = "Ошибка типа. Введенные данные - не число"

    def __str__(self):
        return self._msg

def cancel(in_val, lst):
    if in_val == "stop":
        print(f"Введенный список {lst}")
        print("Работа закончена")
        exit(0)

print("""Запущен скрипт формирования списка из чисел.
Для выхода введите stop """)
my_lst = []
while True:
    a = input("Введите число:")
    cancel(a, my_lst)
    try:
        try:
            a = eval(a)
        except (TypeError,NameError) :
            raise MyTypeError()
        else:
            # Нужен для правильной обработки ввода выражений с вызовом функций
            if isinstance(a,(int,float,complex)):
                my_lst.append(a)
                print(F"Добавлен элемент {a}")
            else:
                print("Введенные данные не являются числом")
                continue
    except MyTypeError as er:
        print(er)
        continue

