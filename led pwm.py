import RPi.GPIO as GPIO
import time
Led_pin=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led_pin,GPIO.OUT)
pwm_led=GPIO.PWM(Led_pin,50)
pwm_led.start(100)
while True:
  duty_s=raw_input(“Enter Brightness between(0 to 100):”)
  duty=int(duty_s)
  pwm_led.ChangeDutyCycle(duty)
  time.sleep(1)
