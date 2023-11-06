Import Rpi.GPIO as GPIO
import time
buzzer_pin=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)

def buzz(pitch,duration):
  period=1.0/pitch
  delay=period/2
  cycles=int(duration*pitch)

for I in range(cycles):
  GPIO.output(buzzer_pin,True)
  time.sleep(delay)
  GPIO.output(buzzer_pin,False)
  time.sleep(delay)

While True:
  pitch_s=input(“Enter pitch between(200 to 2000):”)
  pitch=float(pitch_s)
  duration_s=input(“Enter Duration in Seconds:”)
  duration=float(duration_s)
  buzz(pitch ,duration)
