import pygame
import serial

#Written by Brendon Brown
#2018
#This program uses pygame to read xbox 360 controller input and send serial data
#through an xbee connected to a serial port

#This creates the Controller class
class Controller:

    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.hatcount = self.joystick.get_numhats()
        self.axescount = self.joystick.get_numaxes()
        

serxb = serial.Serial('COM6', 9600)     #assumes xbee is connected to the COM6 port
test = Controller()
serxb.close()                   #makes sure the old port isn't open
serxb.open()                    #opens up port for communication

print(test.hatcount)            #for testing purposes
print(test.axescount)           #for testing purposes


while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            print("start")
            float LX = test.joystick.get_axis(0)
            float LY = test.joystick.get_axis(1)
            float RY = test.joystick.get_axis(3)
            float RX = test.joystick.get_axis(4)
            print(test.joystick.get_axis(0))    #testing purposes
            print(test.joystick.get_axis(1))    #testing purposes
            print(test.joystick.get_axis(2))    #testing purposes
            print(test.joystick.get_axis(3))    #testing purposes
            print(test.joystick.get_axis(4))    #testing purposes
            if 0.25 >= RY >= -0.25:
                if RX <= -0.75:
                    serxb.write("left".encode())
                elif RX >= 0.75:
                    serxb.write("right".encode())
                else:
                    serxb.write("stop".encode())
            elif 0.75 >= RY > 0.25:
                serxb.write("walk".encode())
            elif RY > 0.75:
                serxb.write("run".encode())
            elif -0.25 > RY >= -0.75:
                serxb.write("back".encode())
            elif RY < -0.75:
                serxb.write("slide".encode())
            if RX <= -0.75:
                serxb.write("left".encode())
            elif RX >= 0.75:
                serxb.write("right".encode())
                
            print("end")
