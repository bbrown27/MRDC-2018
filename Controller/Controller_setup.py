import pygame
import serial

#Written by Brendon Brown
#Last updated Feburary 15, 2019
#This program uses pygame to read xbox 360/PSX controller input and send serial data
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
        self.buttcount = self.joystick.get_numbuttons()
#end of controller class
        

serxb = serial.Serial('COM6', 9600)     #assumes xbee is connected to the COM6 port
test = Controller()             #creates controller class under name test
serxb.close()                   #makes sure the old port isn't open
serxb.open()                    #opens up port for communication

print(test.hatcount)            #for testing purposes
print(test.axescount)           #for testing purposes
print(test.buttcount)           #for testing purposes

lx = test.joystick.get_axis(0) #generates the X axis of the left joystick
ly = test.joystick.get_axis(1) #generates the Y axis of the left joystick
ry = test.joystick.get_axis(3) #generates the y axis of the right joystick
rx = test.joystick.get_axis(4) #generates the X axis of the right joystick


while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:

#Encoding Table
#Right Motor: Stop = 0, Forward = 2, Forward+ = 6, Backward = 4, Backward- = 8
#Left Motor: Stop = 1, Forward = 3, Forward+ = 7, Backward = 5, Backward- = 9
            
            if abs(lx - test.joystick.get_axis(0)) > 0.1:
                lx = test.joystick.get_axis(0)      #generates the X axis of the left joystick
                print(test.joystick.get_axis(0))    #testing purposes
            if abs(ly - test.joystick.get_axis(1)) > 0.1:
                ly = test.joystick.get_axis(1)      #generates the Y axis of the left joystick
                print(test.joystick.get_axis(1))    #testing purposes
                if 0.25 >= ry >= -0.25:
                    serxb.write("0".encode())
                elif 0.75 >= ry > 0.25:
                    serxb.write("4".encode())
                elif ry > 0.75:
                    serxb.write("8".encode())
                elif -0.25 > ry >= -0.75:
                    serxb.write("2".encode())
                elif ry < -0.75:
                    serxb.write("6".encode())
            if abs(rx - test.joystick.get_axis(3)) > 0.1:
                rx = test.joystick.get_axis(3)      #generates the X axis of the right joystick
                print(test.joystick.get_axis(3))    #testing purposes
            if abs(ry - test.joystick.get_axis(4)) > 0.1:
                ry = test.joystick.get_axis(4)      #generates the Y axis of the right joystick
                print(test.joystick.get_axis(4))    #testing purposes
                if 0.25 >= ly >= -0.25:
                    serxb.write("1".encode())
                elif 0.75 >= ly > 0.25:
                    serxb.write("5".encode())
                elif ly > 0.75:
                    serxb.write("9".encode())
                elif -0.25 > ly >= -0.75:
                    serxb.write("3".encode())
                elif ly < -0.75:
                    serxb.write("7".encode())


# Button to int format (Playstation buttons have not been recorded)
# A = 0 = Square
# B = 1 =
# X = 2
# Y = 3
# LB = 4
# RB = 5
# Back = 6
# Start = 7
# Left Joystick Button = 8
# Right Joystick Button = 9
            
        if event.type == pygame.JOYBUTTONDOWN:
            if test.joystick.get_button(0):
                print("0 has been activated")
                serxb.write("A".encode())
            if test.joystick.get_button(1):
                print("1 has been activated")
                serxb.write("B".encode())
            if test.joystick.get_button(2):
                print("2 has been activated")
                serxb.write("X".encode())
            if test.joystick.get_button(3):
                print("3 has been activated")
            if test.joystick.get_button(4):
                print("4 has been activated")
            if test.joystick.get_button(5):
                print("5 has been activated")
            if test.joystick.get_button(6):
                print("6 has been activated")
            if test.joystick.get_button(7):
                print("7 has been activated")
            if test.joystick.get_button(8):
                print("8 has been activated")
            if test.joystick.get_button(9):
                print("9 has been activated")
            
            print("end")

        if event.type == pygame.JOYHATMOTION:
            print("Hat motion is not readable at this time")
            print("end")
            
