int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

lst_d.append('4')
lst_d.append('5')
print(id(lst_d))
x = isinstance('set_b', str)
print(x)
y = isinstance('2', float)
print(y)
l = (f"Anna has {lst_d[2]} apples and {lst_d[1]} peaches.")
print(l)
print('Anna has {} apples and {} peaches.'.format(5,2))
apples = 4
peaches = 3
print('Anna has {} apples and {} peaches.'.format(apples,peaches))
print('Anna has {1} apples and {1} peaches.'.format(apples,peaches))
print('Anna has {ap} apples and {pe} peaches.'.format(pe=18,ap=10))
a = 9
b = 6
def add_nums(a, b):
    return a + b
print(f'Anna has {add_nums(a,b)} apples and {b} peaches.')
print('Anna has %d apples' %a + 'and %d peaches.' % b)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
lst_1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_1)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)
lsti = []
for num in range(10):
    if num % 2 == 0:
        lsti.append(int(num / 2))
    else:
        lsti.append(num * 10)
print(lsti)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)
b = {number: number **2  for number in range (1, 11) if number % 2 == 1 }
print(b)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
l = {el: el ** 2 if el % 2 == 1 else el // 0.5 for el in range (1,11)}
print(l)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)
f = {}
for y in range (10):
    if y ** 3 % 4 == 0:
        f[y] = y ** 3
print(f)
dict_comprehension_1 = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension_1)
g = {}
for s in range(10):
    if s ** 3 % 4 == 0:
        g[s] = s ** 3
    else:
        g[s] = s
print(g)
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
print(sorted(lst_to_sort, reverse=True))
lst_to_sort_1 = list(map(lambda t: t+t, lst_to_sort))
print(lst_to_sort_1)
list_A = [2, 3, 4]
list_B = [5, 6, 7]
k = list(map(lambda x: list_B[0] - list_A [0]+ x,  list_A))
print(k)
