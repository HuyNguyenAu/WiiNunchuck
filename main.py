from nunchuck import nunchuck
import time

lowerBound = 0.0
center = 128.0
upperBound = 255.0 
dead = 10.0
deadband = [center - dead, center + dead]
wii = nunchuck()

def getRaw():
  return wii.getJoystickY()

def getValue():
  value = getRaw()
  # Deadband [118, 138].
  if value >= deadband[0] and value <= deadband[1]:
    return 0.0
  # Positive (138, 255].
  elif value > deadband[1] and value <= upperBound:  
    return round((value - deadband[1]) / (upperBound - deadband[1]), 1)
  # Negative [0, 118).
  elif value >= lowerBound and value < deadband[0]:  
    return round(-1.0 * ((deadband[0] - value) / deadband[0]), 1)
  return 0

def main():
 while True:
  print(getValue())
  time.sleep(0.1)

if __name__== "__main__":
    main()