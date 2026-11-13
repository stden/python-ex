# -*- coding: utf-8 -*-

def DOS2Windows(src_filename,dst_filename):
  """ Перекодирование файла из кодировки DOS в кодировку Windows-1251 """
  f = open(src_filename, 'rb')
  content = f.read().decode("cp866")
  f.close()
  print content # Печатается нормальная Unicode строка
  f = open(dst_filename, 'wb')
  f.write(content.encode('windows-1251'))
  f.close()

DOS2Windows('dos.txt','windows.txt')

# Различные примеры на строки

print u"Первая строка\nПерешли на новую строку"
print r"First\nSecond" # Выводим строку "как есть", служебные последовательности символов тоже выводятся "как есть"
# r от RAW - сырой

# "Многострочная строка"
print u""" Начало длинной-предлинной строки
        Long-long TEXT

        И здесь ещё какой-то текст
          и ещё строка.. целое сочинение!
        -----------------------

 Окончание длинной-предлинной строки"""

s = "  test "
print ">"+s+"<"
print ">"+s.strip()+"<"
s = u"Привет"
print s[:-1]
word = u'Да'+u'Нет' # Конкатенация строк
print u"Не"+word[4]

print ur"test\\\\" # Сырая Unicode строка
print u"test\\\u0026"

print "Обычная русская строка"
print "Обычная русская строка".decode("utf-8")
print unicode('Привет','windows-1251')
print 'Привет'.decode('windows-1251')
print u'Привет'.encode('windows-1251')

print u'Hello' == 'Hello' # True
print u'Привет' == ("Привет".decode('windows-1251')) # False
