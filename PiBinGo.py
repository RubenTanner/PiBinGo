import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)  # Right IR sensor module
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Activation button
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Left IR sensor module
GPIO.setup(5, GPIO.OUT)  # Left motor control
GPIO.setup(7, GPIO.OUT)  # Left motor control
GPIO.setup(11, GPIO.OUT)  # Right motor control
GPIO.setup(13, GPIO.OUT)  # Right motor control

# Motor stop/brake
GPIO.output(5, 0)
GPIO.output(7, 0)
GPIO.output(11, 0)
GPIO.output(13, 0)

flag = 0
while True:
    j = GPIO.input(12)
    if j == 1:  # Activated when button is pressed
        flag = 1
        print("PiBinGo is a Go!", j)

    while flag == 1:
        j = GPIO.input(12)
        i = GPIO.input(3, 16)  # Listening for output from right IR sensor
        k = GPIO.input(16)  # Listening for output from left IR sensor
        if i == 0:  # Obstacle detected on right IR sensor
            print("Obstacle detected on Right", i)
            # Move in reverse direction
            GPIO.output(5, 1)  # Left motor turns anticlockwise
            GPIO.output(7, 0)
            GPIO.output(11, 1)  # Right motor turns antilockwise
            GPIO.output(13, 0)
            time.sleep(1)

            # Turn robot left
            GPIO.output(5, 0)  # Left motor turns clockwise
            GPIO.output(7, 1)
            GPIO.output(11, 0)  # Right motor turns clockwise
            GPIO.output(13, 1)
            time.sleep(2)

        if j == 1:  # De activate PiBinGo on button push
            flag = 0
            print("PiBinGo be gone", j)
            GPIO.output(5, 0)
            GPIO.output(7, 0)
            GPIO.output(11, 0)
            GPIO.output(13, 0)
            time.sleep(1)
