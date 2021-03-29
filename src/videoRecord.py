import picamera
import datetime

now = datetime.datetime.now()
print(now.hour, now.minute)

camera = picamera.PiCamera()
#camera.resolution = (640, 480)
camera.start_recording('my_first_video.h264')
camera.wait_recording(60)
camera.stop_recording()

now = datetime.datetime.now()
print(now.hour, now.minute)
