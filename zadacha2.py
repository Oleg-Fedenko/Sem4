#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
#Если ключ не хешируем, используйте его строковое представление. reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}


def dictionary(one, two):
    dictum = {
        f'{one}': id(one),
        f'{two}': id(two)
    }

    return dictum


a = 4
b = 8
temp = dictionary(a, b)
print(temp)
