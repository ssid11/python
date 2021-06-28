class MyZeroDivide(ZeroDivisionError):
    def __init__(self):
        self._msg = "Попытка деления на ноль"

    def __str__(self):
        return self._msg

def cancel(in_val):
    if in_val == "stop":
        print("Работа закончена")
        exit(0)

print("""Запущен скрипт вычисления частного целых чисел.
Для выхода введите stop """)
while True:
    a = input("Введите делимое:")
    cancel(a)
    a = int(a)
    b = input("Введите делитель:")
    cancel(b)
    b = int(b)
    try:
        if not b:
            raise MyZeroDivide()
    except MyZeroDivide as er:
        print(er)
    else:
        print(f"Частное деления чисел {a} и {b} равно {a/b:.3f}")








