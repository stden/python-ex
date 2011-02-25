# -*- coding: utf-8 -*-

# Пример со списками и словарями
l = [2,3,36,4]
# Добавление элемента в конец списка
l.append(56)
# Вставка элемента в середину списка
l.insert(3,999) # Вставить элемент 999 после 3-его элемента списка
print l
# l[6] = 10  # Шестого элемента нет => Будет ошибка

# Создаём словарь
d = {}
d[23] = 67
print d  # {23: 67}
d[5] = 231
print d  # {5: 231, 23: 67}
# Переписываем 23-ий элемент
d[23] = 554
d[23462356] = (2,3)
d[234656] = "sdfsgd"
for k in sorted(d.keys()):
  print "d[%s] = %s" % (k, d[k])
print d

b = [3,2,4]
c = list(b)
b.append(55)
print 'b =',b
print 'c =',c

class Test:
  value = 1

a = Test()
a.value = 2
b = a
b.value = 3
print 'a =',a.value
print 'b =',b.value




  