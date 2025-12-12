import time
import board
import busio
import adafruit_mpu6050
import neopixel 

i2c = busio.I2C(board.GP15, board.GP14)
mpu = adafruit_mpu6050.MPU6050(i2c)
mpu.accelerometer_range = adafruit_mpu6050.Range.RANGE_2_G
mpu.gyro_range = adafruit_mpu6050.GyroRange.RANGE_250_DPS

din_pin = board.GP17     
num_pixels = 8           
ORDER = neopixel.GRB     

pixels = neopixel.NeoPixel(din_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

threshold = 5

while True:
    x_acc = abs(round(mpu.acceleration[0], 2))
    y_acc = abs(round(mpu.acceleration[1], 2))
    z_acc = abs(round(mpu.acceleration[2], 2))
    
    all_axes = [x_acc, y_acc, z_acc]
    
    if any(axis > threshold for axis in all_axes):
        if y_acc > x_acc and y_acc > z_acc:
            pixels.brightness = 0.1 

            pixels.fill((255, 0, 0)) 
            pixels.show()
        else:
            pixels.brightness = 1.0

            pixels.fill((255, 0, 0))
            pixels.show()
            time.sleep(0.1)
            
            pixels.fill((0, 0, 0))
            pixels.show()
            time.sleep(0.1)
    else:
        pixels.fill((0, 0, 0))
        pixels.show()

    print(f"({x_acc:.2f}, {y_acc:.2f}, {z_acc:.2f})")
    time.sleep(0.01)