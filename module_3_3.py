def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('----1 п.------------')
print_params()          # Без параметров
print_params(a = 999, c = 121)
print_params(b = 25)
print_params(c = [1, 2, 3])

print('----2 п.------------')

values_list = [77, 'БАСКЕТБОЛ', True] # Параметры различных типов для списка
print_params(*values_list)

values_dict = {'a':'ЧислО','b':'Набор_букВ ','c':'ЛогикА'} # Словарь
print_params(**values_dict)

print('----3 п.------------')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
