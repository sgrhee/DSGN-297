import board
import pwmio
import time
import adafruit_hcsr04

servo = pwmio.PWMOut(board.GP15, variable_frequency=True)
servo.frequency = 50 # hz
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP16, echo_pin=board.GP17)
min_servo = int(65535*0.5/20)
range_servo = int(65535*2.0/20)

while True:
    # pulse 0.5 ms to 2.5 ms out of a possible 20 ms (50Hz)
    # for 0 degrees to 180 degrees
    # so duty_cycle can be 65535*0.5/20 to 65535*2.5/20
    # but check this, some servo brands might only want 1-2 ms
    try:
        distance = sonar.distance
        if distance > 50 and distance < 750: 
            distance = 40
        elif distance > 750:
            distance = 0
        servo.duty_cycle = (int((distance/40) * range_servo + min_servo))
        
    except RuntimeError:
        print("Retrying!")

    time.sleep(0.01)
    