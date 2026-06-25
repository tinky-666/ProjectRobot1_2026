# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image
import tinybit

display.show(Image.ARROW_S)
tinybit.car_run(150)
while True:

    if button_a.was_pressed():
        tinybit.car_run(150)
        display.show(Image.ARROW_S)
    if button_b.was_pressed():
        tinybit.car_stop()
        display.clear()
    sleep(50)
