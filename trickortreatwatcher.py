from gpiozero import  LED, MotionSensor, PWMLED, LightSensor
import time
from datetime import datetime
import os
import glob
import sys
from twython import Twython
CONSUMER_KEY = ' ***Your info *** '
CONSUMER_SECRET = ' ***Your info *** '
ACCESS_KEY = ' ***Your info *** '
ACCESS_SECRET = ' ***Your info *** '

from gpiozero import  LED, MotionSensor, PWMLED, LightSensor
import time
from datetime import datetime
import os
import glob
import sys
from twython import Twython
CONSUMER_KEY = ' ***Your Info *** '
CONSUMER_SECRET = '***Your Info ***'
ACCESS_KEY = '***Your Info ***'
ACCESS_SECRET = '***Your Info ***'

pir = MotionSensor(18)
red1 = LED(20)
red2 = LED(21)
green = PWMLED(25)
ldr = LightSensor(23)


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)


tempfile = open("/sys/bus/w1/devices/28-041591c231ff/w1_slave")
thetext = tempfile.read()
tempfile.close()
tempdata = thetext.split("\n")[1].split(" ")[9]
temperature = float(tempdata[2:])
temperature = str(temperature / 1000)

thetime = datetime.now().strftime('%-I:%M%P on %d-%m-%Y')

while True:
        ldr.wait_for_dark()
        print("Ready")
        pir.wait_for_motion()
        print("Motion Detected")
        print(ldr.value)
        red1.on()
        red2.on()
        green.pulse(fade_in_time=1.5, fade_out_time=1.5, n=4, background=True)
        api.update_status(status= temperature + " C at " + thetime + " #Raspberrypitrickortreat")
        time.sleep(10)
        red1.off()
        red2.off()
        green.off()
        time.sleep(10)
