# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 16:54:06 2022

@author: richa
"""
import random

class Agent():
    
    # Set up a set of coordinates of an agent
    def __init__(self, environment, agents):
        self.environment = environment
        self.agents = agents
        self._y = random.randint(0,99)
        self._x = random.randint(0,99) 
        self.store = 0
        

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
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
        
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

    # Each agent interacts and changes the environment
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10   

    # Each agent searching for close neighbours, and sharing resources
    def share_with_neighbours(self, neighbourhood):
     for agent in self.agents:
         distance = self.distance_between(agent) 
         if distance <= neighbourhood:
             sum1 = self.store + agent.store
             average = sum1 /2
             self.store = average
             agent.store = average
             #print("sharing " + str(distance) + " " + str(average))
             
    # Calculating the distance of an agent to each of the other agents
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5 

    

    
    
    
    