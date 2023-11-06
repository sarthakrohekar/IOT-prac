import Rpi.GPIO as GPIO
import time
button_pin=37
buzzer_pin=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(13,GPIO.OUT)
def buzz(pitch,duration):
  period=1.0/pitch
  delay=period/2
  cycles=int(duration*pitch)

  for i in range(cycles):
    if(GPIO.input(button_pin)==0):
      GPIO.output(buzzer_pin,GPIO.HIGH)
      time.sleep(delay)
    else:
      GPIO.output(buzzer_pin,GPIO.LOW)
      time.sleep(delay)

While True:
  pitch_s=input(“Enter pitch between(200 to 2000):”)
  pitch=float(pitch_s)
  duration_s=input(“Enter Duration in Seconds:”)
  duration=float(duration_s)
  buzz(pitch ,duration)
