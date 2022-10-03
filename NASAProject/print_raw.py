

import keyboard
import time
import csv
from pyOpenBCI import OpenBCICyton

def print_raw(sample):
    writer.writerow(sample.channels_data)

board = OpenBCICyton(port = '/dev/tty.usbserial-DM02584N', daisy = False)

f = open('/Users/jeffreyklinck/Desktop/NASA\Project/Happy/test1.csv', 'w')
writer = csv.writer(f)

while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            board.start_stream(print_raw)
            time.sleep(10)
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break

f.close()
