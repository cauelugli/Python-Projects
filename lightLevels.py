from pyfirmata import Arduino, util
import time

Uno = Arduino('COM3')
blinktime = 2

def low_1():
    Uno.digital[8].write(1)
    #time.sleep(blinktime)
    #Uno.digital[8].write(0)

def low_2():
    Uno.digital[8].write(1)
    Uno.digital[7].write(1)
    time.sleep(blinktime)
    Uno.digital[8].write(0)
    Uno.digital[7].write(0)

def med_1():
    Uno.digital[8].write(1)
    Uno.digital[7].write(1)
    Uno.digital[6].write(1)
    time.sleep(blinktime)
    Uno.digital[8].write(0)
    Uno.digital[7].write(0)
    Uno.digital[6].write(0)

def med_2():
    Uno.digital[8].write(1)
    Uno.digital[7].write(1)
    Uno.digital[6].write(1)
    Uno.digital[5].write(1)
    time.sleep(blinktime)
    Uno.digital[8].write(0)
    Uno.digital[7].write(0)
    Uno.digital[6].write(0)
    Uno.digital[5].write(0)


def high_1():
    Uno.digital[8].write(1)
    Uno.digital[7].write(1)
    Uno.digital[6].write(1)
    Uno.digital[5].write(1)
    Uno.digital[4].write(1)
    time.sleep(blinktime)
    Uno.digital[8].write(0)
    Uno.digital[7].write(0)
    Uno.digital[6].write(0)
    Uno.digital[5].write(0)
    Uno.digital[4].write(0)


def high_2():
    Uno.digital[8].write(1)
    Uno.digital[7].write(1)
    Uno.digital[6].write(1)
    Uno.digital[5].write(1)
    Uno.digital[4].write(1)
    Uno.digital[3].write(1)
    #time.sleep(blinktime)
    #Uno.digital[8].write(0)
    #Uno.digital[7].write(0)
    #Uno.digital[6].write(0)
    #Uno.digital[5].write(0)
    #Uno.digital[4].write(0)
    #Uno.digital[3].write(0)
