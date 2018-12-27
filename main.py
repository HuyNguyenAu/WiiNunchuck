# Code adapted from:
# 1. https://www.hackster.io/infusion/using-a-wii-nunchuk-with-arduino-597254
# 2. https://github.com/Boeeerb/Nunchuck/blob/master/Raspberry%20Pi/nunchuck.py

from smbus import SMBus
import time

dev_bus = 1
dev_addr = 0x52
delay = 0.1
bus = SMBus(dev_bus)

def getJoystickX():
    bus.write_byte_data(dev_addr, 0x00)
    time.sleep(delay)
    return bus.read_byte(dev_addr)

def init():
    bus.write_byte_data(dev_addr, 0xF0, 0x55)
    bus.write_byte_data(dev_addr, 0xFB, 0x00)
    time.sleep(delay)
    
def main():
    init()
    
    while True:
        print(getJoystickX())

if __name__== "__main__":
    main()