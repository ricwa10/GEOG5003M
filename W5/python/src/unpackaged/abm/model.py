# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:53:40 2022

@author: richa
"""

import operator
import matplotlib.pyplot
import time
import agentframework

start = time.process_time()

a = agentframework.Agent() 

# Creating a function to calculate the distance between two agents
def distance_between(agents_row_a, agents_row_b):

    """
    Parameters: Coordinates of each agent
    ----------
    agents_row_a : an integer or double number (no default)
    agents_row_b : an integer or double number (no default)

    Returns
    -------
    The distance between both agent coordinates.

    """           
    
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Set up a set of coordinates of each agent
for i in range(num_of_agents):
    agents.append(agentframework.Agent())


# Moving all agents coordinates as many times as the number of iterations
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

# Ploting all agents into a XY chart
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].y, agents[i].x)
matplotlib.pyplot.show()


# Calculating the distance between every two agents
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        #print(round(distance,2))
                
end = time.process_time()

# Calculating time how long the code runs
print("time = " + str(end - start) + " seconds")
