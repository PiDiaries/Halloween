from gpiozero import  LED, MotionSensor, PWMLED, LightSensor
import time
import os
import glob
import sys
from twython import Twython
CONSUMER_KEY = ' ***Your info *** '
CONSUMER_SECRET = ' ***Your info *** '
ACCESS_KEY = ' ***Your info *** '
ACCESS_SECRET = ' ***Your info *** '

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


def read_temp_raw():
    f = open(device_file, 'r') # Opens the temperature device file
    lines = f.readlines() # Returns the text
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(60)
        lines = read_temp_raw()

    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c



while True:
    if ldr.value <0.05:
        print("Ready")
        pir.wait_for_motion()
        print("Motion Detected")
        print(read_temp())
        print(ldr.value)
        red1.on()
        red2.on()
        green.pulse(fade_in_time=1.5, fade_out_time=1.5, n=4, background=True)
        api.update_status(status='Tweet test '+temp+' c')
        time.sleep(10)
        red1.off()
        red2.off()
        green.off()
        time.sleep(10)
