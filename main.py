from nunchuck import nunchuck
import time

lowerBound = 0
center = 128
upperBound = 255 
dead = 10
deadband = [center - dead, center + dead]
wii = nunchuck()

# Raw output data from nunchuck.
def getRaw():
  return wii.getJoystickY()

# Convert raw data.
def getValue():
  value = getRaw()
  # Deadband [118, 138].
  if value >= deadband[0] and value <= deadband[1]:
    return 0
  # Positive (138, 255].
  elif value > deadband[1] and value <= upperBound:  
    return (value / (upperBound - deadband[1]))
  # Negative [0, 118).
  elif value >= lowerBound and value < deadband[0]:  
    return -1 * ((deadband[0]) - value / deadband[0])
  return 0

def main():
 while True:
  print(getValue())
  time.sleep(0.1)

if __name__== "__main__":
    main()