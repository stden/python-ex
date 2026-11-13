#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Создание и использование классов
# Public и Private методы

class Thing: # Thing - название класса
  """ Класс "Один предмет" - мы будем создавать объекты этого класса по количеству предметов
  """
  # 2 поля, Поле = Аттрибут = Свойство
  name = "" # Название товара (поле)
  price = 10 # Цена товара (поле)

  def __init__(self, name):
    """ Конструктор - метод который вызывается при создании объекта
     self - это экземпляр класса для которого вызывается эта функция """
    self.name = name

  def __mulPercent(self, percents):
    """ Закрытый метод (имя начинается с 2-х подчёркиваний) """
    return self.price * (100 + percents) / 100.0

  def finalPrice(self):
    """ Метод для вычисления цены с добавлением НДС 18% """
    return self.__mulPercent(18)

  def printInfo(self):
    """ Печать информации об объекте"""
    print self.name, 'price =', self.price, ' finalPrice=', self.finalPrice()

  def increasePrice(self, value):
    """ Увеличить цену """
    self.price += value

  def decreasePrice(self, value):
    """ Уменьшить цену """
    self.price -= value

a = Thing("car")
a.printInfo()

class Rectangle: # Начало описания класса "Прямоугольник"
  # Поля (свойства)
  height = 1 # Высота по-умолчанию
  width = 3 # Ширина по-умолчанию
  # Метод
  def Square(self):
    return self.height * self.width

R1 = Rectangle() # R1 - это объект класса Rectangle
R1.height = 23
print R1.height, R1.width, R1.Square() # 23 3 69

# Глубокое копирование объекта
from copy import deepcopy

R2 = R1 # R2 теперь указывает на тот же объект что и R1
R1.height = 1 # Меняем высоту R1, меняется и R2
R3 = deepcopy(R1) # R3 - "глубокая копия" R1
R3.height = 2 # Меняем высоту R3
print 'R1.height =', R1.height  # R1.height = 1
print 'R2.height =', R2.height  # R2.height = 1
print 'R3.height =', R3.height  # R3.height = 2

R2 = Rectangle()
print R2.Square()

print help(Thing)






  