import busio
import RPi.GPIO as GPIO
import board
from adafruit_pn532.i2c import PN532_I2C
from time import sleep, time, localtime, asctime

i2c = busio.I2C(board.SCL, board.SDA)


pn532 = PN532_I2C(i2c, debug=False) #setup pn532
ic, ver, rev, support = pn532.firmware_version #get firmware version
pn532.SAM_configuration()

def check_card():
    global uidSave, cardTime
    # Check if a card is available to read if yes save it
    uid = pn532.read_passive_target(timeout=0.5)
    # Try again if no card is available.
     
    # Check if a card is available to read if yes save it
    
    print("Found card with UID:", [hex(i) for i in uid])
    cardTime = time() 
    return uid



while True:
    print (check_card())
    sleep(1)    
