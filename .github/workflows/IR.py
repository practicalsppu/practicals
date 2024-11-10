import RPi.GPIO as GPIO
import time

sensor = 16
buzzer = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

GPIO.output(buzzer,False)
print('IR SENSOR READYput(buzzer, False)...')
print('')

try:
    while True:
        if GPIO.input(sensor):
            GPIO.output(buzzer, False)
            print('Objet Detected')
            while GPIO.input(sensor):
                time.sleep(0.2)
            else:
                GPIO.output(buzzer, True)
                
except KeyboardInterrupt:
    GPIO.cleanup()