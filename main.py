from nunchuck import nunchuck
import time

wii = nunchuck()

def main():
 while True:
  print(wii.getJoystickY())
  time.sleep(0.5)

if __name__== "__main__":
    main()