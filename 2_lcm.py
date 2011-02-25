# -*- coding: utf-8 -*-

# Наибольший общий делитель
def GCD(x,y):
    return x if y == 0 else GCD(y,x%y)

# Наименьшее общее кратное
def LCM(x,y):
    return x*y / GCD(x,y)

print LCM(10,15)
print LCM(10,0)
print LCM(0,30)
print LCM(60,144)
  