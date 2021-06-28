def rnd_str(num=3):
    """ Возвращает случайную строку символов. Параметр - ее длина. По умолчанию 3"""
    import random
    out_str =''
    for i in range(num):
        out_str = out_str + chr(random.randint(65,122))
    return out_str


