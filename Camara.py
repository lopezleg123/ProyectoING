from picamera import PiCamera

camera = PiCamera()

camera.start_preview(alpha=192)
camera.capture('foo.jpg')
camera.stop_preview()

