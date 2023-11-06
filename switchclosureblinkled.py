import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
While True:
  reading=GPIO.input(19)
  if reading==0:
  print(“First Button Pressed”)
  While True:
    GPIO.output(20,1)
    time.sleep(1)
    GPIO.output(20,0)
    time.sleep(1)
    reading1=GPIO.input(16)
    if reading1==0:
      break
  reading1=GPIO.input(16)
  if reading1==0:
  print(“Second Button Pressed”)
  while True:
    GPIO.output(21,1)
    time.sleep(1)
    GPIO.output(21,0)
    time.sleep(1)
    reading=GPIO.input(19)
    if reading==0:
      break
time.sleep(1)
