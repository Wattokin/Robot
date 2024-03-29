import gpiozero
import cwiid

robot = gpiozero.Robot(right=(17,18), left=(27,22))

print("Press and hold th 1-2 buttons on your wimote simultaneously")
wii = cwiid.Wiimote()
print("Connection established")
wii.rpt_mode = cwiid.RPT_BTN

while True:
        buttons = wii.state["buttons"]

        if (buttons & cwiid.BTN_LEFT):
                robot.left()
        if (buttons & cwiid.BTN_RIGHT):
                robot.right()
        if (buttons & cwiid.BTN_UP):
                robot.forward()
        if (buttons & cwiid.BTN_DOWN):
                robot.backward()
        if(buttons & cwiid.BTN_B):
                robot.stop()
