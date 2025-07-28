import os

SNums = [0,1,2,3] #Numbers of the Servos we'll be using in ServoBlaster
SName = ["Waist","Left","Right","Claw"] #Names of Servos
AInis = [90,152,90,60] #Initial angle for Servos 0-3
AMins = [0,60,40,60] #Minimum angles for Servos 0-3
AMaxs = [180,165,180,180] #Maximum angles for Servos 0-3
ACurs = AInis #Current angles being set as the intial angles
Step = 5

class Servo(object):
    
    def __init__(self):
        print ("SERVO INFO START")
        for i in range(4):

            print(SNums[i],AInis[i],AMins[i],AMaxs[i],ACurs[i])
        print ("SERVO INFO END")
        os.system('sudo /home/pi/PiBits/ServoBlaster/user/servod --idle-timeout=2000')
        print("Servo Controller Started")
    
    def increase(self, Servo):
        if ACurs[Servo] < AMaxs[Servo]:
            ACurs[Servo] = ACurs[Servo]+Step
            # micro = (1000 + (ACurs[Servo] * 5.555))
            micro = (1000 + (ACurs[Servo] * 8.3333))
            print(ACurs[Servo],micro)
            os.system("echo %d=%dus > /dev/servoblaster" % (SNums[Servo],micro))
        else:
            print("Max Angle Reached",SName[Servo], "Servo")

    def decrease(self, Servo):
        if ACurs[Servo] > AMins[Servo]:
            ACurs[Servo] = ACurs[Servo]-Step
            # micro = (1000 + (ACurs[Servo] * 5.555))
            micro = (1000 + (ACurs[Servo] * 8.3333))
            print(ACurs[Servo],micro)
            os.system("echo %d=%dus > /dev/servoblaster" % (SNums[Servo],micro))

        else:
            print("Min Angle Reached",SName[Servo], "Servo")
