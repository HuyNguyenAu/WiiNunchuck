from nunchuck import nunchuck
import time

wii = nunchuck()
lowerBand = [0, 20]
upperBand = [235, 255]
deadBand = [100, 128, 148] 

def getValue():
  value = wii.getJoystickY()
  return value

def main():
 while True:
  print(getValue())
  time.sleep(0.1)

if __name__== "__main__":
    main()