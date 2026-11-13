#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Используется присваивание "по ссылке"
class MyClass: field = 1 # Создали класс MyClass с одним полем field

a = MyClass()
a.field = 3
b = MyClass()
b = a #  Теперь b и a ссылаются на один и тот же объект
b.field = 4
print "a.field =", a.field, ' b.field =', b.field # a.field = 4  b.field = 4

# Используем "глубокое копирование"
import copy

c = copy.deepcopy(a)
c.field = 5
a.field = 6
print "c.field =", c.field, ' a.field =', a.field # c.field = 5  a.field = 6
