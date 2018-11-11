import RPi.GPIO as GPIO
import xbox

from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1A = 02

Motor1B = 03

Motor1E = 04

Motor2A = 02

Motor2B = 03

Motor2E = 04
py

GPIO.setup(Motor1A,GPIO.OUT)

GPIO.setup(Motor1B,GPIO.OUT)

GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)

GPIO.seup(Motor2B,GPIO.OUT)

GPIO.setup(Motor2E,GPIO.OUT)

joy = xbox.Joystick()   #Initialize joystick

print "Test out your motors"

y_axis = joy.leftY()

if joy.leftY() = 1:
        GPIO.output(Motor1A,GPIO.HIGH) #clockwise
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)

        GPIO.output(Motor1E,GPIO.HIGH) #Turns motors on
        GPIO.output(Motor2E,GPIO.HIGH)

if joy.leftY() = -1:
        GPIO.output(Motor1A,GPIO.LOW) #clockwise
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.HIGH)

        GPIO.output(Motor1E,GPIO.HIGH) #Turns motors on
        GPIO.output(Motor2E,GPIO.HIGH)

x_axis = joy.rightX()

if joy.rightX() = 1:
        GPIO.output(Motor1A,GPIO.HIGH) #clockwise
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH) #Anti-clockwise

        GPIO.output(Motor1E,GPIO.HIGH) #Turns motors on
        GPIO.output(Motor2E,GPIO.HIGH)

if joy.rightX() = -1:
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.HIGH) #clockwise
        GPIO.output(Motor1B,GPIO.HIGH) #Anti-clockwise
        GPIO.output(Motor2B,GPIO.LOW)

        GPIO.output(Motor1E,GPIO.HIGH) #Turns motors on
        GPIO.output(Motor2E,GPIO.HIGH)
