# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:53:40 2022

@author: richa
"""

import random
import operator
import matplotlib.pyplot

#Creating the container list for the agents
agents = []

# Assigning the first pair of coordinates to the agents list.
agents.append([random.randint(0,99),random.randint(0,99)]) 

# Random walk two steps (first pair).
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
    
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1


# Assigning the second pair of coordinates to the agents list.
agents.append([random.randint(0,99),random.randint(0,99)]) 

# Random walk two steps (second pair).
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    

if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

#Coordinates of both agents after moving randomly one step
print(agents)

# Distance between both agents after moving
distance = ((agents[0][0] - agents[1][0])**2 + (agents[0][1] - agents[1][1])**2)**0.5
print(round(distance,2))

#Coordinates of the agent that is furthest east
print("Furthest east agent coordinates =", max(agents, key=operator.itemgetter(1)))

#Coordinates of the agent that is furthest north
print("Furthest north agent coordinates =", max(agents, key=operator.itemgetter(0)))

#Ploting both agents into a XY chart
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

#Giving colour "red" to the furthest east agent
matplotlib.pyplot.scatter(max(agents, key=operator.itemgetter(1))[1],max(agents, key=operator.itemgetter(1))[0], color='red')

matplotlib.pyplot.show()

