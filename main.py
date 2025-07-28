"""
SETUP FROM HOME DIR
// Clone The ServoBlaster from Github
git clone git://github.com/richardghirst/PiBits.git

// enter the install directory and build
cd PiBits/ServoBlaster/user
make servod
"""

from MeArm import Servo
import time
servo = Servo()

# increase Servo 0 for 3 seconds
for _ in range (1, 30):
    servo.increase(0)
    time.sleep(0.1)


# decrease Servo 0 for 3 seconds
for _ in range (1, 30):
    servo.decrease(0)
    time.sleep(0.1)