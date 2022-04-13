# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:53:40 2022

@author: richa
"""

import random
import tkinter
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot
import matplotlib.animation
import time
import agentframework
import csv


# Importing data from a "html" file
import requests
import bs4
   
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs) 


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

# Creating a figure to show agents
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)




# Set up a set of coordinates of each agent
# Shuffling the list of agents each iteration before moving
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)  
    agents.append(agentframework.Agent(environment, agents, y, x))
    random.shuffle(agents)
    print(agents[i]._y, agents[i]._x)
        
a = agentframework.Agent(environment, agents, y, x)
    

carry_on = True

# Updating the movement and behaviour of all agents
def update(frame_number):
    fig.clear()
    global carry_on

    # Moving all agents coordinates as many times as the number of iterations
    # All agents interact and change the environment
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
           
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
            
    # Ploting all agents into a XY chart
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._y, agents[i]._x)
        
# Creating a stopping condition by a generator function      
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on):
        yield a
        a = a + 1
                
# Adding a function to run the model
def run():
     animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
     canvas.draw()
     

# Building the main window and creating the layout
root = tkinter.Tk()

root.wm_title("Agent-based model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

# Creating the menu and associating it to the "run" function
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()

end = time.process_time()

# Calculating time how long the code runs
print("time = " + str(end - start) + " seconds")

# Writing out the environment as a CSV file after interactions
f2 = open('out.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)
f2.close()



