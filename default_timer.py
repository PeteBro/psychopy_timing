from psychopy import core, visual, event
import serial
import time
from tqdm import tqdm

# Set parameters
flips = 60
interval = 60

# Set up the EEG trigger port
#port = serial.Serial('COM3', 115200, timeout=1)

# Create window
win = visual.Window(fullscr=True)

# Get time array
t = {}

# Start trials
for i in tqdm(range(flips)):
    #win.callOnFlip(port.write(bytes[1]))
    win.timeOnFlip(t, str(i))
    _ = win.flip()
    core.wait(interval)

# Cleanup
win.close()