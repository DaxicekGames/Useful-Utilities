#Created by Daxicek
#Version 1.1
from math import *
from random import *
from time import *
from keyboard import *

#----MATH---- (01xxxx)
PI = 3.14159265358979
TAU = PI * 2
E = 2.71828182846

#CIRCLE (0101xx)
def circle_circumference(radius):
    return radius * 2 * PI

def circle_area(radius):
    return radius * radius * PI

#FACTORIAL (0102xx)
def factorial(factorial):
    answer = factorial
    for i in range(1, factorial):
        answer = answer * i
    return answer

#PRIME (0103xx)
def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False

#TRIANGLE (0104xx)
def triangle_hypotenuse(pendant1, pendant2): #(010401)
    try:
        return sqrt(pendant1 * pendant1 + pendant2 * pendant2)
    except:
        print("ERROR: Invavalid values!")


def triangle_pendant(hypotenuse, pendant): #(010402)
    try:
        return sqrt(hypotenuse * hypotenuse - pendant * pendant)
    except:
        print("ERROR: Invavalid values!")

def triangle_area(a, b, c): #(O1O403)
    try:
        s = (a + b + c) / 2
        return sqrt(s * (s-a) * (s-b) * (s-c))
    except:
        print("ERROR: Invalid values!")

#TEST (0105xx)
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

#----RANDOM---- (02xxxx)
#RANDOM FLOAT (0201xx)
def randfloat(n_from, n_to, max_length):
    length = 1
    for i in range(max_length):
        length = length * 10

    n_from = n_from * length
    n_to = n_to * length

    return randint(n_from, n_to) / length

#RANDOM BOOL (0202xx)
def randbool():
    if randint(1, 2) == 1:
        return True
    else:
        return False

#RANDOM STRING (0203xx)
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

#RANDOM COLOR (0204xx)
def randcolor():
    return randint(0, 255), randint(0, 255), randint(0, 255)
        
#----TIME---- (03xxxx)
#STOPWATCH (0301xx)
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

#STOPWATCH TEST (0302xx)
def stopwatch_test():
    print("Start")
    stopwatch.start()
    input("\nPress enter to stop the stopwatch...\n")
    stopwatch.stop()
    print(f"Value: {stopwatch.time()}")
    stopwatch.reset()
    print(f"Reset: {stopwatch.time()}")

#TICK RATE (0302xx)
def tps(tick_rate):
    sleep(1/tick_rate)

#TICK RATE TEST (0303xx)
def tps_test():
    tps_value = int(input("TPS: "))
    while True:
        tps(tps_value)
        print("Tick")

#----PYGAME---- (04xxxx)
#PYGAME IMPORT (0401xx)
enable_pygame = False
if enable_pygame: #(040101)
    try:
        import pygame
        window = pygame.display.set_mode(700, 500)
    except:
        print("ERROR: Pygame isn't avalible!")

#SPRITE CLASS (0402xx)
class sprite():
    def __init__(self, image_name, scale, x, y):
        self = pygame.transform.scale(pygame.image.load(image_name), scale)
        self.x = x
        self.y = y
    def draw(self):
        window.blit(self, (self.x, self.y))


#BACKGROUND CLASS (0403xx)
class sprite():
    def __init__(self, image_name):
        self.image_name = image_name
        self = pygame.image.load(self.image_name)
        window.blit(self, (0, 0))

#----KEYBOARD---- (05xxxx)
#PRESS FOR TIME (0501xx)
def press_for_time(key, seconds):
    press(key)
    sleep(seconds)
    release(key)

#PRESS TIMES (0502xx)
def press_times(key, how_many, speed):
    for i in range(how_many):
        press_and_release(key)
        sleep(speed)

press_for_time("A", 2)
press_for_time("B", 2)
