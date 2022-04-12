# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:53:40 2022

@author: richa
"""

import random
import operator
import matplotlib.pyplot
import time

start = time.process_time()

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
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

   
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

# Ploting all agents into a XY chart
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()


# Calculating the distance between every two agents
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(round(distance,2))
      
end = time.process_time()

# Calculating time how long the code runs
print("time = " + str(end - start) + " seconds")