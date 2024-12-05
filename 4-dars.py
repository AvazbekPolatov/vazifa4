class LowerCaseDescriptor:
    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value.lower()

class MyClass1:
    my_attr = LowerCaseDescriptor()

class MyClass2:
    my_attr = LowerCaseDescriptor()

obj1 = MyClass1()
obj2 = MyClass2()

obj1.my_attr = "HELLO"
obj2.my_attr = "WORLD"

print(obj1.my_attr)  
print(obj2.my_attr)  
# --------------------------------------------------------------------------

# 2-masala
class PositiveValueDescriptor:
    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        self._value = value

class MyClass1:
    my_attr = PositiveValueDescriptor()

class MyClass2:
    my_attr = PositiveValueDescriptor()

#
obj1 = MyClass1()
obj2 = MyClass2()

obj1.my_attr = 10
obj2.my_attr = 20

print(obj1.my_attr)  
print(obj2.my_attr)  

# -----------------------------------------------------------------------------

# 3-masala

from datetime import datetime, timedelta

today = datetime.today()
print("Bugungi sana:", today)

seven_days_later = today + timedelta(days=7)
seven_days_earlier = today - timedelta(days=7)

print("7 kun keyin:", seven_days_later)
print("7 kun oldin:", seven_days_earlier)

# ---------------------------------------------------------------

# 4-masala
from datetime import datetime

birth_year = int(input("Tug'ilgan yilingizni kiriting: "))
today = datetime.today()
age = today.year - birth_year

if today.month == 1 and today.day == 1:
    print("Tug'ilgan kuningiz bilan!")
else:
    print(f"Sizning yoshingiz: {age}")

# -------------------------------------------------------------------------------------

# 5-masala

from datetime import datetime

time1 = input("Birinchi vaqtni kiriting (HH:MM:SS formatida): ")
time2 = input("Ikkinchi vaqtni kiriting (HH:MM:SS formatida): ")

time1 = datetime.strptime(time1, "%H:%M:%S")
time2 = datetime.strptime(time2, "%H:%M:%S")

delta = abs((time2 - time1).total_seconds())
print(f"Jami soniyalar: {delta}")

# ---------------------------------------------------------------------------------------

# 6-masala

import math

diameter = float(input("Aylana diametrini kiriting: "))
radius = diameter / 2
area = math.pi * (radius ** 2)

print(f"Aylana yuzasi: {area}")

# ---------------------------------------------------------------------------------

# 7-masala

import math

number = float(input("Sonni kiriting: "))

if number < 0:
    raise ValueError("Son manfiy bo'lishi mumkin emas")

sqrt = math.sqrt(number)
cbrt = number ** (1/3)

print(f"Kvadrat ildiz: {sqrt}")
print(f"Kub ildiz: {cbrt}")

# -------------------------------------------------------------------------------------

# 8-masala

import random

# Tasodifiy 5 ta butun son (1 dan 100 gacha)
integers = [random.randint(1, 100) for _ in range(5)]
print("Tasodifiy butun sonlar:", integers)

# Tasodifiy 3 ta haqiqiy son (0 dan 1 gacha)
floats = [random.random() for _ in range(3)]
print("Tasodifiy haqiqiy sonlar:", floats)

# O'rtacha qiymatni hisoblash
average = sum(integers + floats) / (len(integers) + len(floats))
print("O'rtacha qiymat:", average)
