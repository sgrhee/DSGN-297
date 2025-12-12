import time
import board
import busio
#import adafruit_register
import adafruit_mpu6050 # required the adafruit_register library folder to be in CIRCUITPY/lib/
import neopixel_write # a simple method for setting a neopixel color
import digitalio
pin = digitalio.DigitalInOut(board.GP16)
pin.direction = digitalio.Direction.OUTPUT

i2c = busio.I2C(board.GP15, board.GP14) # the I2C pins used, (SCL, SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)
mpu.accelerometer_range = adafruit_mpu6050.Range.RANGE_2_G # acceleration values from -2G to +2G
mpu.gyro_range = adafruit_mpu6050.GyroRange.RANGE_250_DPS # angular velocity values from -250dps to +250dps
acc_range = 9.81*2
neopixel_write.neopixel_write(pin, bytearray([0,0,0]))
while True:
    x_acc = abs(round(mpu.acceleration[0],2))
    y_acc = abs(round(mpu.acceleration[1],2))
    z_acc = abs(round(mpu.acceleration[2],2))
    

    x2r = int(x_acc/acc_range * 255)
    y2g = int(y_acc/acc_range * 255)
    z2b = int(z_acc/acc_range * 255)
    neopixel_write.neopixel_write(pin, bytearray([y2g,x2r,z2b]))

    print("(%.2f, %.2f, %.2f " % (mpu.acceleration))
    #print("%.2f, %.2f, %.2f)" % (mpu.gyro))
    time.sleep(0.010)  
