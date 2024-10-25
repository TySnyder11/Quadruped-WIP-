from math import *
import pygame 
import time
#from adafruit_servokit import ServoKit

class leg():
    a0=30.75
    a1=120
    a2=120
    
    def __init__(self,hip_x,hip_y,knee):
        self.hip_x = hip_x
        self.hip_y = hip_y
        self.knee = knee
    
    def set_position(self, x,y,z):
        self.find_theta(self, x,y,z)
    
    def find_theta(self, x,y,z):
        c0=a0+x
        if z == 0:
            theta0=(pi/2)-(acos(a0/(sqrt(pow(z,2)+pow(c0,2)))))
        else:
            theta0=(pi/2)-(acos(a0/(sqrt(pow(z,2)+pow(c0,2))))+atan(c0/z))
        x1=self.a0*cos(theta0)
        z1=self.a0*sin(theta0)
        b1=sqrt(pow(x+a0-x1,2)+pow(y,2)+pow(z-z1,2))
        Alpha0=acos((-(pow(b1,2))+pow(self.a1,2)+pow(a2,2))/(2*self.a1*self.a2))
        theta2=pi-Alpha0
        theta1=(pi/2)-(asin((self.a2*sin(Alpha0))/b1)+atan(y/sqrt(pow(x+a0-x1,2)+pow(z-z1,2))))

class quadruped:
    mode =1
    def __init__(self, Front_Right_Leg: leg, Front_Left_Leg: leg, Back_Right_Leg: leg, Back_Left_Leg: leg, clock):  
        self.RFL = Front_Right_Leg
        self.FLL = Front_Left_Leg
        self.BRL = Back_Right_Leg
        self.BLL = Back_Left_Leg