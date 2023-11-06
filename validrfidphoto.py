import RPi.GPIO as GPIO
import SimpleMFRC522
import time
GPIO.setmode(GPIO.BCM)
from picamera import PiCamera
camera=PiCamera()
camera.resolution=(1024,768)
reader=SimpleMFRC522.SimpleMFRC522()
while True: 
  print(“Please Swipe your card”)

  id,text=reader.read()

  id1=str(id)

  text=str(text)

  text=text.strip()

  if text==‘bmw’:

      print(“Valid User”)

      camera.start_preview()

      time.sleep(2)

      camera.capture(test_photo.jpg’)

      camera.stop_preview()

GPIO.cleanup()
