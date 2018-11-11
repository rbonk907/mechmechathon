import RPi.GPIO as GPIO
import xbox

from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1A = 02

Motor1B = 03

Motor1E = 04

#Motor2A = 02

#Motor2B = 03

#Motor2E = 04

servo1A = 18


GPIO.setup(Motor1A,GPIO.OUT)

GPIO.setup(Motor1B,GPIO.OUT)

GPIO.setup(Motor1E,GPIO.OUT)

#GPIO.setup(Motor2A,GPIO.OUT)

#GPIO.setup(Motor2B,GPIO.OUT)

#GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(servo1A,GPIO.OUT)
pwm = GPIO.PWM(servo1A,50)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo1A, True)
    pwm.ChangeDutyCycle(duty)
    sleep(5)
    GPIO.output(servo1A, False)
    pwm.ChangeDutyCycle(0)




print "Test out your motors"

#x,y = joy.leftStick()
joy = xbox.Joystick()   #Initialize joystick
while not joy.Back():
    y_axis = joy.leftY()
    if joy.leftY() == 1:
            print "Left Up Pressed"
            GPIO.output(Motor1A,GPIO.HIGH) #clockwise
            #GPIO.output(Motor2A,GPIO.HIGH)
            GPIO.output(Motor1B,GPIO.LOW)
            #GPIO.output(Motor2B,GPIO.LOW)

            GPIO.output(Motor1E,GPIO.HIGH) #Turns motors on
            #GPIO.output(Motor2E,GPIO.HIGH)
            sleep(1)

    if joy.leftY() == -1:
            print "Left Down Pressed"
            GPIO.output(Motor1A,GPIO.LOW) #clockwise
            #GPIO.output(Motor2A,GPIO.LOW)
            GPIO.output(Motor1B,GPIO.HIGH)
            #GPIO.output(Motor2B,GPIO.HIGH)

            GPIO.output(Motor1E,GPIO.HIGH) #Turns motors on
            #GPIO.output(Motor2E,GPIO.HIGH)
            sleep(1)

    x_axis = joy.rightX()

    if joy.rightX() == 1:
            print "Right right Pressed"
            GPIO.output(Motor1A,GPIO.HIGH) #clockwise
            #GPIO.output(Motor2A,GPIO.LOW)
            GPIO.output(Motor1B,GPIO.LOW)
            #GPIO.output(Motor2B,GPIO.HIGH) #Anti-clockwise

            GPIO.output(Motor1E,GPIO.HIGH) #Turns motors on
            #GPIO.output(Motor2E,GPIO.HIGH)
            sleep(1)

    if joy.rightX() == -1:
            print "Right left pressed"
            GPIO.output(Motor1A,GPIO.LOW)
            #GPIO.output(Motor2A,GPIO.HIGH) #clockwise
            GPIO.output(Motor1B,GPIO.HIGH) #Anti-clockwise
            #GPIO.output(Motor2B,GPIO.LOW)

            GPIO.output(Motor1E,GPIO.HIGH) #Turns motors on
            #GPIO.output(Motor2E,GPIO.HIGH)
            sleep(1)

    if joy.A():
        print "A button pressed"

        SetAngle(60)

    #if joy.B():
    #    print "B button pressed"
    #    GPIO.output(servo1A,GPIO.LOW)
    #    sleep(1)

joy.close()
print "stopping motors"
GPIO.output(Motor1E,GPIO.LOW) # to stop the motor

GPIO.cleanup()
