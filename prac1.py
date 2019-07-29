#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <names>
Student Number: <studnum>
Prac: <Prac Num>
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time

# Logic that you write
    #set pin mode to board
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.IN) 
def increment(channel):
    print("button pressed")


GPIO.add_event_detect(11, GPIO.RISING, callback=increment, bouncetime=300)

def main():
    count = 0
    #check button click
    while count < 8:
        if GPIO.input(7):
            print("input was high")
            time.sleep(1)
        else:
            print("input was low")
            time.sleep(1)
        if GPIO.event_detected(11):
            print('Button pressed' + str(count))
            count += 1

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
