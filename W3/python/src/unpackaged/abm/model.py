# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:53:40 2022

@author: richa
"""

import random
import operator
import matplotlib.pyplot

num_of_agents = 10
num_of_iterations = 100

agents = []


# Set up a set of coordinates of each agent
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Agents coordinates before moving randomly
print("Agents' coordinates before moving =", agents)

# Moving all agents coordinates as many times as the number of iterations
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
        
# Agents coordinates after moving randomly
print("Agents' coordinates after moving =",agents)

'''

distance = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(distance)

'''

# Ploting all agents into a XY chart
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

