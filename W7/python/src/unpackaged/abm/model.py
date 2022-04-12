# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:53:40 2022

@author: richa
"""

import random
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


num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

a = agentframework.Agent(environment, agents)

# Set up a set of coordinates of each agent
# Shuffling the list of agents each iteration before moving
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    random.shuffle(agents)

# Moving all agents coordinates as many times as the number of iterations
# All agents interact and change the environment
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

# Ploting all agents into a XY chart
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._y, agents[i]._x)
    print(agents[i]._y, agents[i]._x)
matplotlib.pyplot.show()
           
end = time.process_time()

# Calculating time how long the code runs
print("time = " + str(end - start) + " seconds")

# Writing out the environment as a CSV file after interactions
f2 = open('out.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)
f2.close()



