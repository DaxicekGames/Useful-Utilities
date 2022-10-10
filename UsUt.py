#Created by Daxicek
#Version 1.1
from math import *
from random import *
from time import *

#----MATH----
PI = 3.14159265358979
TAU = PI * 2
E = 2.71828182846

#CIRCLE
def circle_circumference(radius):
    return radius * 2 * PI

def circle_area(radius):
    return radius * radius * PI

#FACTORIAL
def factorial(factorial):
    answer = factorial
    for i in range(1, factorial):
        answer = answer * i
    return answer

#PRIME
def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False

#TRIANGLE
def triangle_hypotenuse(pendant1, pendant2):
    try:
        return sqrt(pendant1 * pendant1 + pendant2 * pendant2)
    except:
        return "ERROR: Invavalid values!"


def triangle_pendant(hypotenuse, pendant):
    try:
        return sqrt(hypotenuse * hypotenuse - pendant * pendant)
    except:
        return "ERROR: Invavalid values!"

def triangle_area(a, b, c):
    try:
        s = (a + b + c) / 2
        return sqrt(s * (s-a) * (s-b) * (s-c))
    except:
        return "ERROR: Invalid values!"

#TEST
def math_test():
    print(f"\n----------------\n\nPI: {PI} \nE: {E} \nTAU: {TAU} \n\n----------------\n")

    print(f"CIRCLE area: {circle_area(int(input('RADIUS (area): ')))}\n")
    print(f"CIRCLE circumference: {circle_circumference(int(input('RADIUS (circumference): ')))}\n\n----------------\n")

    print(f"TRIANGLE hypotenuse: {triangle_hypotenuse(int(input('PENDANT1 (triangle hypotenuse): ')), int(input('PENDANT2 (triangle hypotenuse): ')))}\n")
    print(f"TRIANGLE pendant: {triangle_pendant(int(input('HYPOTENUSE (triangle pendant): ')), int(input('PENDANT (triangle pendant): ')))}\n")
    print(f"TRIANGLE area: {triangle_area(int(input('A (triangle area): ')), int(input('B (triangle area): ')), int(input('C (triangle area): ')))}\n\n----------------\n")

    print(f"FACTORIAL: {factorial(int(input('FACTORIAL: ')))}\n\n----------------\n")

    print(f"PRIME: {is_prime(int(input('PRIME: ')))}\n")

#----COLORS----
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
CYAN = 0, 255, 255
AERO = 124, 185, 232
DARK_GREEN = 0, 128, 0
DARK_BLUE = 0, 0, 128
DARK_RED = 128, 0, 0
DARK_YELLOW = 128, 128, 0
GOLD = 255, 215, 0
ORANGE = 230, 153, 0
PURPLE = 137, 0, 255
PINK = 241, 156, 187

#----ALPHABET----
en_alphabet = "abcdefghijklmnopqrstuvwxyz"
en_alphabet_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ru_alphabet_capital = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
cz_alphabet = "aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzž"
cz_alphabet_capital = "AÁBCČDĎEÉĚFGHCHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ"
numbers = "0123456789"
sp_chars = "-_,.;:*+-/\|#&!?=<>()[]%"

#----RANDOM----
#RANDOM FLOAT
def randfloat(n_from, n_to, max_length):
    length = 1
    for i in range(max_length):
        length = length * 10

    n_from = n_from * length
    n_to = n_to * length

    return randint(n_from, n_to) / length

#RANDOM BOOL
def randbool():
    a = randint(1, 2)

    if a == 1:
        return True
    else:
        return False

#RANDOM STRING
def randstr(length, add_capitals, add_numbers, add_spaces, add_special_chars):
    string = str("")
    for i in range(length):

        while True:
            rand = randint(1, 5)

            if rand == 1:
                string = string + en_alphabet[randint(0, 25)]
                break
            if rand == 2 and add_capitals:
                string = string + en_alphabet_capital[randint(0, 25)]
                break
            if rand == 3 and add_numbers:
                string = string + str(numbers[randint(0, 9)])
                break
            if rand == 4 and add_spaces:
                string = string + " "
                break
            if rand == 5 and add_special_chars:
                string = string + str(sp_chars[randint(0, 23)])
                break
    return string

#RANDOM COLOR
def randcolor():
    return randint(0, 255), randint(0, 255), randint(0, 255)
        
#----TIME----
#STOPWATCH
class sw_class():
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
    def start(self):
        self.start_time = time()
    def stop(self):
        self.stop_time = time()
    def time(self):
        return self.stop_time - self.start_time
    def reset(self):
        self.start_time = 0
        self.stop_time = 0
stopwatch = sw_class()

#STOPWATCH TEST
def stopwatch_test():
    print("Start")
    stopwatch.start()
    input("\nPress enter to stop the stopwatch...\n")
    stopwatch.stop()
    print(f"Value: {stopwatch.time()}")
    stopwatch.reset()
    print(f"Reset: {stopwatch.time()}")

#TICK RATE
def tps(tick_rate):
    sleep(1/tick_rate)

#TICK RATE TEST
def tps_test():
    tps_value = int(input("TPS: "))
    while True:
        tps(tps_value)
        print("Tick")
