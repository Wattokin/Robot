import cwiid
import time

print("press and hold 1+2 buttons on yout wiimote")
wii = cwiid.Wiimote()
print("connection established")
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

while True:
        print(wii.state['acc'])
        time.sleep(0.01)
