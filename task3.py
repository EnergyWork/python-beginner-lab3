"""
В списке чисел проверить, все ли элементы являются уникальными, т. е. 
каждое число встречается только один раз. 
Решить минимум двумя способами.
"""

arr = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]

# method 1
if len(arr) == len(list(set(arr))):
    print('Все элементы уникальны')
else:
    print('Есть не уникальные элементы')

# method 2
arr_tmp = sorted(arr)
flag = True
for i in range(1, len(arr_tmp)):
    if arr_tmp[i] == arr_tmp[i - 1]:
        print('Элемент {num} не уникальный'.format(num=arr_tmp[i]))
        flag = False
else:
    if flag:
        print('Все элементы уникальный')
