'''
PICO / Micropython demo program to find / move 180 degree rotation of small RC Servo
 MG90S Servo Specs
 Rotational range 180 degrees
 Signal Frequeny for PWM is 50 hz (20 msecs)
 Duty cycle range for full Rotation range 1~2 msec
 duty_16() takes values of 0 to 65535 for duty cycle of 0 to 100
 0 = 0% = 0 msec        65535 = 100% = 20 msec
 
 
 
 Estimated Min, Mid, Max duty cycles for 0, 90, 180 degrees
 Min 1000
 Mid 4750  = (Min + ((Max - Min) / 2)
 Max 8500
'''

from machine import Pin, PWM
import utime


MG90S_servo = PWM(Pin(14))
MG90S_power = Pin(15, Pin.OUT)
MG90S_power.value(1)

MG90S_servo.freq(50)


Ang_000 = 1500
Ang_180 = 8000
Angle = 120

Move_to = int(Ang_000 + ((Ang_180 - Ang_000)/(180/Angle)))

print("Moving")
MG90S_servo.duty_u16(Ang_000)
utime.sleep(2)
print("Moving")
MG90S_servo.duty_u16(Move_to)
utime.sleep(2)
print("Moving")
MG90S_servo.duty_u16(Ang_180)
utime.sleep(2)

print("Turning off")
MG90S_power.value(0)