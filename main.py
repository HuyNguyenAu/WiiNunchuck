from nunchuck import nunchuck
import time

wii = nunchuck()
lowerBound = 34
upperBound = 239
neutral = 136

def getValue():
  value = wii.getJoystickY()
  if (value >= lowerBound and value <= upperBound):
    return value

def main():
 while True:
  print(getValue())
  time.sleep(0.1)

if __name__== "__main__":
    main()