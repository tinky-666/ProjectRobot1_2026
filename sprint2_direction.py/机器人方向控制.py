# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, sleep, button_a, button_b
import tinybit

running = True

while True:

    if button_a.was_pressed():
        running = True
    if button_b.was_pressed():
        running = False
        tinybit.car_stop()
        display.clear()
    if not running:
        sleep(50)
        continue

    tinybit.car_run(150)
    display.show(Image.ARROW_S)
    for i in range(10):
        if button_b.was_pressed():
            running = False
            break
        sleep(100)
    if not running:
        continue

    tinybit.car_back(150)
    display.show(Image.ARROW_N)
    for i in range(10):
        if button_b.was_pressed():
            running = False
            break
        sleep(100)
    if not running:
        continue

    tinybit.car_left(150)
    display.show(Image.ARROW_E)
    for i in range(10):
        if button_b.was_pressed():
            running = False
            break
        sleep(100)
    if not running:
        continue

    tinybit.car_right(150)
    display.show(Image.ARROW_W)
    for i in range(10):
        if button_b.was_pressed():
            running = False
            break
        sleep(100)
    if not running:
        continue

    tinybit.car_spinleft(150)
    display.show(Image.ARROW_E)
    for i in range(10):
        if button_b.was_pressed():
            running = False
            break
        sleep(100)
    if not running:
        continue

    tinybit.car_spinright(150)
    display.show(Image.ARROW_W)
    for i in range(10):
        if button_b.was_pressed():
            running = False
            break
        sleep(100)
    if not running:
        continue

    tinybit.car_stop()
    display.clear()
    for i in range(10):
        if button_b.was_pressed():
            running = False
            break
        sleep(100)
