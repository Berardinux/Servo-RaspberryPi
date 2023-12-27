import GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)
servo.start(0)
angle = 0

def map_value(value, in_min, in_max, out_min, out_max):
  return np.interp(value, [in_min, in_max], [out_min, out_max])

try:
  while True:
    duty = map_value(angle, 0, 179, 2, 12)
    servo.ChangeDutyCycle(duty)
    if angle == 178:
      angle = 0
    else:
      angle = angle + 1
    print(f"{angle}°")
    time.sleep(.1)
finally:
  servo.stop()
  GPIO.cleanup()