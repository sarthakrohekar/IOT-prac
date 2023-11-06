import time
import RPi.GPIO as GPIO
GPIO.clearup()
GPIO.setmode(GPIO.BCM)

stepPins = [17,18,22,23]

for pin in stepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin,False)

time.sleep(0.5)

stepCounter = 0
WaitTime = 0.0015

StepCount2 = 8
Seq2 = []
Seq2 = range(0,StepCount2)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

Seq = Seq2
StepCount = StepCount2

try:
  while 1==1:
    for pin in range(0,4)
      xpin = StepPins[pin]
      if seq[stepCounter][pin]!=0
        GPIO.output(xpin,False)
      else:
        GPIO.output(xpin,False)
    StepCounter+=1

    if (stepCounter == StepCount):
      stepCounter=0
    if (stepCounter<0):
      stepCounter = stepCount

    time.sleep(WaitTime)
except:
  GPIO.cleanup()

finally:
  GPIO.cleanup()
  for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
