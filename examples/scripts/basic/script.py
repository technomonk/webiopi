# Imports
import webiopi

# Enable debugging output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO
SWITCH = 21
SERVO  = 23
LED0   = 24
LED1   = 25

# -------------------------------------------------- #
# Initialization part - WebIOPi will call setup()    #
# -------------------------------------------------- #
def setup():
    webiopi.debug("Basic script Setup")
    # Setup GPIOs
    GPIO.setFunction(SWITCH, GPIO.IN)
    GPIO.setFunction(SERVO, GPIO.PWM)
    GPIO.setFunction(LED0, GPIO.PWM)
    GPIO.setFunction(LED1, GPIO.OUT)
    
    GPIO.pwmWrite(LED0, 0.5)        # set to 50% ratio
    GPIO.pwmWriteAngle(SERVO, 0)    # set to 0 (neutral)
    GPIO.digitalWrite(LED1, GPIO.HIGH)

# -------------------------------------------------- #
# Termination part - WebIOPi will call destroy()     #
# -------------------------------------------------- #
def destroy():
    webiopi.debug("Basic script Destroy")
    # Reset GPIO functions
    GPIO.setFunction(SWITCH, GPIO.IN)
    GPIO.setFunction(SERVO, GPIO.IN)
    GPIO.setFunction(LED0, GPIO.IN)
    GPIO.setFunction(LED1, GPIO.IN)