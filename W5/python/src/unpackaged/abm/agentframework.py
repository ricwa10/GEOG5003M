# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 16:54:06 2022

@author: richa
"""
import random

class Agent():
    
    # Set up a set of coordinates of an agent
    def __init__(self):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)

    # Protecting the self.y and self.x variables
    def gety(self):
        return self._y
    def getx(self):
        return self._x
        
    def sety(self, value):
        self._y = value
    def setx(self, value):
        self._x = value

    def dely(self):
        del self._y
    def delx(self):
        del self._x

    # Defining the method "move" to randomly move the agents
    def move(self):
        if random.random() < 0.5:
            self.y = (self._y + 1) % 100
        else:
            self.y = (self._y - 1) % 100
        
        if random.random() < 0.5:
            self.x = (self._x + 1) % 100
        else:
            self.x = (self._x - 1) % 100
