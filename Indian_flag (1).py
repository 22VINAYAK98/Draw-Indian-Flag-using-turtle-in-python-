#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle 
# Getting a Screen 
ws = turtle.Screen() 
# Defing a turtle Instance 
flagTurtle = turtle.Turtle() 
# initially penup() 
flagTurtle.penup() 
# Initially setting position  
flagTurtle.goto(-180, 60)     
  
  
  
# For First Rectangle and filling  
# Orange color to Rectangle 
class Indian_flag:
    
    def orange():
    
        flagTurtle.pendown() 
        flagTurtle.begin_fill() 
        flagTurtle.fillcolor("orange") 
        flagTurtle.left(90) 
        flagTurtle.forward(90) 
        flagTurtle.right(90) 
        flagTurtle.forward(400) 
        flagTurtle.right(90) 
        flagTurtle.forward(90) 
        flagTurtle.right(90) 
        flagTurtle.forward(400) 
        flagTurtle.end_fill() 



    # For Second Rectangle 
    def white():
        
        flagTurtle.left(90) 
        flagTurtle.forward(90) 
        flagTurtle.left(90) 
        flagTurtle.forward(400) 
        flagTurtle.left(90) 
        flagTurtle.forward(90) 
        flagTurtle.left(90) 
        flagTurtle.forward(400) 
        flagTurtle.left(90) 
        flagTurtle.forward(90) 



    # For Third Rectangle and filling  
    # Green color to Rectangle 
    def green():
        
        flagTurtle.begin_fill() 
        flagTurtle.fillcolor("green") 
        flagTurtle.forward(90) 
        flagTurtle.left(90) 
        flagTurtle.forward(400) 
        flagTurtle.left(90) 
        flagTurtle.forward(90) 
        flagTurtle.left(90) 
        flagTurtle.forward(400) 
        flagTurtle.end_fill() 



    # For making Ashoka Chakra  
    # At middle of the flag. 
    # And coloring it Blue 


    def ahokchakra():
        
        turtle.penup()
        turtle.goto(23,10)
        turtle.color("blue")
        for spoke in range(0,24):
            turtle.goto(23,10)
            turtle.right(15)
            turtle.pendown()
            turtle.forward(45)
            turtle.penup()

        turtle.penup() 
        turtle.goto(23, -28)
        turtle.color("blue")
        turtle.pendown() 
        turtle.begin_fill() 
        #flagTurtle.fillcolor("blue") 
        turtle.circle(42) 
        #flagTurtle.end_fill()


    # It helps to hold the screen  
turtle.done()


# In[ ]:




