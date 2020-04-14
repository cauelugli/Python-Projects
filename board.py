from pyfirmata import Arduino, util
import time

Uno = Arduino('COM3')

print('Hello World')

while True:
    Uno.digital[3].write(1)
    print('led on')
    time.sleep(0.1)

    Uno.digital[3].write(0)
    print('led off')
    time.sleep(0.1)

