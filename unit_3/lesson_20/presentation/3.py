# Дана строка, содержащая только английские буквы (большие и маленькие). Добавить открывающиеся и закрывающиеся скобки
# по следующему образцу: "example" -> "(e(x(a(m)p)l)e)" (До середины добавлены открывающиеся скобки, после середины –
# закрывающиеся. В случае, когда длина строки четна в скобках, расположенных в середине, должно быть 2 символа.
# ("card -> (c(ar)d", но не "(c(a()r)d)").

my_str = 'example'


def add_parentheses(my_str):
    if len(my_str) <= 2:
        return f'({my_str})'
    return f'({my_str[0]}{add_parentheses(my_str[1:-1])}{my_str[-1]})'


print(add_parentheses(my_str))
