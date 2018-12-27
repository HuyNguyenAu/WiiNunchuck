from nunchuck import nunchuck
import time

wii = nunchuck()
lowerBound = 34
upperBound = 239
neutral = 136

# TODO 255 and 0 come up randomly?
value_prev = 0

def getValue():
  value = wii.getJoystickY()
  if (value >= lowerBound and value <= upperBound):
    global value_prev
    value_prev = value
    return value
  else:
    return value_prev

def main():
 while True:
  print(getValue())
  time.sleep(0.1)

if __name__== "__main__":
    main()