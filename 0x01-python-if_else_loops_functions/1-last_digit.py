#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number)
d = 1000
while (d >= 10):
    last = last % d
    d = d / 10
if number < 0 and last > 0:
    last = last * -1
if last > 5:
    print(f"Last digit of {number} is {last:.0f} and is greater than 5")
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {last:.0f} and is less than 6 and not 0")
elif last == 0:
    print(f"Last digit of {number} is {last:.0f} and is 0")
