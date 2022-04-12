# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:53:40 2022

@author: richa
"""

import operator
import matplotlib.pyplot
import time
import agentframework
import csv

start = time.process_time()

# Opening the raster file to be used as agents' environment
with open('in.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
#    print(environment)

a = agentframework.Agent(environment) 

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
    
    return (((agents_row_a._x - agents_row_b._x)**2) + ((agents_row_a._y - agents_row_b._y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Set up a set of coordinates of each agent
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))


# Moving all agents coordinates as many times as the number of iterations
# All agents interact and change the environment
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

# Ploting all agents into a XY chart
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._y, agents[i]._x)
matplotlib.pyplot.show()


# Calculating the distance between every two agents
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        #print(round(distance,2))
                
end = time.process_time()

# Calculating time how long the code runs
print("time = " + str(end - start) + " seconds")

# Writing out the environment as a CSV file after interactions
f2 = open('out.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)
f2.close()









