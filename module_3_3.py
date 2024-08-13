def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print('0 ------------Добавочная проверка------------')
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [33, 'AAAAAA', False]
print_params()
print_params(*values_list)
print('1 -------------Промежуточная проверка----------')
values_dict = {'a': 77, 'b': 'FFFFF', 'c': True}
print_params(**values_dict)
print('2 ------------Итоговая проверка--------------')
values_list_2 = [888, 'КЛЯКСА']
print_params(*values_list_2, 42)
