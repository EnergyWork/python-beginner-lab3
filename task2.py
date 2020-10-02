"""
В списке чисел найти самую длинную последовательность, 
которая упорядочена по возрастанию. Если таких последовательностей 
несколько (с одинаковой максимальной длиной), то найти их все. 
Вывести на экран сам список, длину самой длинной упорядоченной 
по возрастанию последовательности, саму последовательность (или несколько).
"""

def check(tmp, res):
    if len(tmp) > 1:
        if len(res) >= 1:
            if len(tmp) == len(res[-1]):
                res.append(tmp)
            elif len(tmp) > len(res[-1]):
                res.clear()
                res.append(tmp)
        else:
            res.append(tmp)

arr = [1, 2, 3, 0, 1, 2, 0]
res = []
tmp = []
i = 0
while i < len(arr):
    if len(tmp) == 0 or arr[i] >= tmp[-1]:
        tmp.append(arr[i])
        i += 1
    else: 
        check(tmp, res)
        tmp = []
else:
    check(tmp, res)

print(arr)
for el in res:
    print(el, 'length = ' + str(len(el)), sep=' ')
