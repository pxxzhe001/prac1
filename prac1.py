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
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)  
def increment(channel):
    print("button pressed")


GPIO.add_event_detect(7, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(11, GPIO.RISING, bouncetime=300)

def main():
    count = 0
    #check button click
    #loop
    while count < 8:
	time.sleep(1)
#        if GPIO.input(7):
#            print("input was high")
#            time.sleep(1)
#        else:
#            print("input was low")
#            time.sleep(1)
        if GPIO.event_detected(7):
            #print('Button pressed' + str(count))
            count += 1
#            print(count)
	if GPIO.event_detected(11):
            #print('Button pressed' + str(count))
            count -= 1
#	    print(count)
	#set count 8 to 0
	if count > 7:
	    count = 0
	#set negative count to max(7)
	if count < 0:
	    count = 7
	#change count to binary
	bcount = format(count,'03b')
	print(bcount)
	pout0 = int(bcount[0])
	pout1 = int(bcount[1])
	pout2 = int(bcount[2])
	GPIO.output(13,pout0)
	GPIO.output(15,pout1)
	GPIO.output(16,pout2)
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
