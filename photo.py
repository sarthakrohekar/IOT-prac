from picamera import PiCamera

from time import sleep

camera = PiCamera()

Camera.resolution=(1024,768)

While True:

  camera.start_preview()

  sleep(5)

  camera.capture(‘test_photo.jpg’)

  camera.stop_preview()
