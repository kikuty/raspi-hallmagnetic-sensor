import RPi.GPIO as GPIO
from time import sleep

SLEEPTIME = 1
PIN = 18
  
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def event_callback():
        print("Magnetic field is detected")

GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback = event_callback, bouncetime = 200) 

try:
    while True:
        sleep(SLEEPTIME)

except KeyboardInterrupt:
    print("\nprogram stopped")
    GPIO.cleanup()
