import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.IN)
GPIO.setup(16,GPIO.IN)
While True:
  reading=GPIO.input(19)
  if reading==0:
  print(“First Button Pressed”)
  reading1=GPIO.input(16)
  if reading1==0:
    print(“Second Button Pressed”)
  time.sleep(1)
