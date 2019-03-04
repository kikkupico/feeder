import time
import RPi.GPIO as GPIO

def feed(): 
  # Use BCM GPIO references
  # instead of physical pin numbers
  GPIO.setmode(GPIO.BCM)
   
  # Define GPIO signals to use
  # Physical pins 11,15,16,18
  # GPIO17,GPIO22,GPIO23,GPIO24
  StepPins = [6,13,19,26]
   
  # Set all pins as output
  for pin in StepPins:
    # print ("Setup pins")
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)
   
  # Define advanced sequence
  # as shown in manufacturers datasheet
  Seq = [[1,0,0,1],
         [1,0,0,0],
         [1,1,0,0],
         [0,1,0,0],
         [0,1,1,0],
         [0,0,1,0],
         [0,0,1,1],
         [0,0,0,1],       
         ]

  StepCount = len(Seq)
  StepDir = -1 # Set to 1 or 2 for clockwise
              # Set to -1 or -2 for anti-clockwise
   
  WaitTime = 1/float(1000)

  # Initialise variables
  StepCounter = 0

  i=0
  steps_per_turn = 1440
  total_steps = 5*steps_per_turn

  # Start main loop
  while i<=total_steps:  
    i += 1  
    # print (StepCounter,)
    # print (Seq[StepCounter])
   
    for pin in range(0, 4):
      xpin = StepPins[pin]
      if Seq[StepCounter][pin]!=0:
        # print (" Enable GPIO %i" %(xpin))
        GPIO.output(xpin, True)
      else:
        GPIO.output(xpin, False)
   
    StepCounter += StepDir
   
    # If we reach the end of the sequence
    # start again
    if (StepCounter>=StepCount):
      StepCounter = 0
    if (StepCounter<0):
      StepCounter = StepCount+StepDir

    # alternate turn direction
    if i%steps_per_turn==0:
      StepDir = -StepDir    
   
    # Wait before moving on
    time.sleep(WaitTime)

if __name__ == "__main__":
  feed()
