# -*- coding: utf-8 -*-

# Вставка элемента в отсортированный массив
# так чтобы он оставался отсортированным

# 1. Через insert/append
def Insert1(b, value): # В функцию передаётся исходный массив b и значение value
  c = list(b) # Делаем копию списка
  for i, x in enumerate(b): # Пробегаем по исходному списку
    if x > value: # Если нашли элемент больше заданного
      c.insert(i, value) # Добавляем перед ним заданный
      return c # Возвращаем изменённый список
  c.append(value) # Если мы так и не нашли заданный элемент, добавляем значение в конец
  return c # возвращаем новый массив

# 2. Используя срезы
def Insert2(b, value):
  for i, x in enumerate(b): # i - индекс в массиве, x - значение
    if x > value:
      return b[:i] + [value] + b[i:] # Слияние 3-х массивов
  return b + [value]

# 3. Двоичный поиск (последнего числа меньшего value)
def Insert3(b, value):
  min, max = 0, len(b)
  while max - min > 0:
    m = (min + max) // 2 # Делим отрезок пополам
    if b[m] > value:
      max = m
    else:
      min = m + 1
  return b[:max] + [value] + b[max:]

# 4. Используя библиотеку bisect - двоичный поиск и вставка
def Insert4(b, value):
  from _bisect import insort
  l = list(b)
  insort(l, value)
  return l

# 5. Добавление путем создания нового списка (поэлементно)
def Insert5(b, value):
  p = []
  inserted = False
  for x in b:
    if x > value and not inserted:
      p.append(value)
      inserted = True
    p.append(x)
  if not inserted:
    p.append(value)
  return p

assert Insert3([11], 10) == [10, 11]
assert Insert3([], 10) == [10]
assert Insert3([3], 10) == [3, 10]
assert Insert3([3, 13], 10) == [3, 10, 13]
assert Insert3([2, 6, 8], 10) == [2, 6, 8, 10]
assert Insert3([2, 6, 8], 7) == [2, 6, 7, 8]
assert Insert3([2, 6, 8], 5) == [2, 5, 6, 8]
assert Insert3([2, 6, 8], 3) == [2, 3, 6, 8]
assert Insert3([2, 6, 8], 1) == [1, 2, 6, 8]
b = [2, 6, 8, 14, 15, 20]
assert Insert3(b, 10) == [2, 6, 8, 10, 14, 15, 20]
assert Insert3(b, 7) == [2, 6, 7, 8, 14, 15, 20]
assert Insert3(b, 5) == [2, 5, 6, 8, 14, 15, 20]
assert Insert3(b, 1) == [1, 2, 6, 8, 14, 15, 20]

assert Insert1([11], 10) == [10, 11]
assert Insert1([], 10) == [10]
assert Insert1([3], 10) == [3, 10]
assert Insert1([3, 13], 10) == [3, 10, 13]
assert Insert1([2, 6, 8], 10) == [2, 6, 8, 10]
assert Insert1([2, 6, 8], 7) == [2, 6, 7, 8]
assert Insert1([2, 6, 8], 5) == [2, 5, 6, 8]
assert Insert1([2, 6, 8], 3) == [2, 3, 6, 8]
assert Insert1([2, 6, 8], 1) == [1, 2, 6, 8]

assert Insert2([11], 10) == [10, 11]
assert Insert2([], 10) == [10]
assert Insert2([3], 10) == [3, 10]
assert Insert2([3, 13], 10) == [3, 10, 13]
assert Insert2([2, 6, 8], 10) == [2, 6, 8, 10]
assert Insert2([2, 6, 8], 7) == [2, 6, 7, 8]
assert Insert2([2, 6, 8], 5) == [2, 5, 6, 8]
assert Insert2([2, 6, 8], 3) == [2, 3, 6, 8]
assert Insert2([2, 6, 8], 1) == [1, 2, 6, 8]

assert Insert5([11], 10) == [10, 11]
assert Insert5([], 10) == [10]
assert Insert5([3], 10) == [3, 10]
assert Insert5([3, 13], 10) == [3, 10, 13]
assert Insert5([2, 6, 8], 10) == [2, 6, 8, 10]
assert Insert5([2, 6, 8], 7) == [2, 6, 7, 8]
assert Insert5([2, 6, 8], 5) == [2, 5, 6, 8]
assert Insert5([2, 6, 8], 3) == [2, 3, 6, 8]
assert Insert5([2, 6, 8], 1) == [1, 2, 6, 8]

print b


# 8.  Дан массив. Найти сумму и количество положительных элементов, расположенных между минимальным и максимальным элементами.
b = [12, 6, -2, 8, -5, 13, -34, 1, -4]
max = b[0]
min = b[0]
for x in b:
  if x > max:
    max = x
  if x < min:
    min = x

# 2. Составить программу, заменяющую отрицательные элементы массива нулями
b = [12, 6, -2, 8, -5, 13, -34, 1, -4]
p = [0 if x < 0 else x for x in b]
print p

 # 20. Даны массивы А и В. Вычислить суммы соответствующих (по индексу) элементов массивов.
# 21. Даны массивы А и В. Вычислить разность соответствующих  элементов массивов.
a = [28, 15, 4, -5, 6]
b = [3, 10, 1, -4, -8]
for k, v in enumerate(a):
  print a[k]+b[k],
print

# 1.  Составить программу нахождения чаще всего встречающегося элемента в массиве
b = [12, 6, 67, 3, 89, 3, 6, 79, 67, 76, 67]
d = {}
for x in b:
  if d.has_key(x):
    d[x] += 1
  else:
    d[x] = 1
max = 0
max_k = 0
for k in d:
  if d[k]>max:
    max = d[k]
    max_k = k
print {max_k:max}

# 3.  Дано произвольное значение b и произвольный массив. Найти сумму элементов массива G, меньших заданного b. """

