Import picamera

camera=picamera.PiCamera()

camera.resolution=(640,480)

camera.start_recording('/home/pi/Desktop/test_video.h264’)

camera.wait_recording(15)

camera.stop_recording()

Print(‘Finished’)
