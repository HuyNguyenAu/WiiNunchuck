# Code adapted from: 1. https://www.hackster.io/infusion/using-a-wii-nunchuk-with-arduino-597254 2. 
# https://github.com/Boeeerb/Nunchuck/blob/master/Raspberry%20Pi/nunchuck.py

from smbus import SMBus
import time

dev_bus = 1
dev_addr = 0x52
dev_init_seq = [0xF0, 0x55, 0xFB, 0x00]
dev_delay = 0.1

maskButtonZ = 0x01
maskButtonC = 0x02

bus = SMBus(dev_bus)

class nunchuck:
    def __init__(self):
        bus.write_byte_data(dev_addr, dev_init_seq[0], dev_init_seq[1])
        bus.write_byte_data(dev_addr, dev_init_seq[2], dev_init_seq[3])
        time.sleep(dev_delay)

    def read(self):
        bus.write_byte(dev_addr, 0x00)
        time.sleep(dev_delay)
        return [bus.read_byte(dev_addr) for i in range(6)]

    def getJoystick(self):
        data = self.read()
        return data[0], data[1]

    def getAccel(self):
        data = self.read()
        return data[2], data[3], data[4]

    def getButtonZ(self):
        data = self.read()
        return (data[5] & maskButtonZ)

    def getButtonC(self):
        data = self.read()
        return (data[5] & maskButtonC)

    def getJoystickX(self):
        data = self.read()
        return data[0]

    def getJoystickY(self):
        data = self.read()
        return data[1]

    def getAccelX(self):
        data = self.read()
        return data[2]

    def getAccelY(self):
        data = self.read()
        return data[3]

    def getAccelZ(self):
        data = self.read()
        return data[4]
