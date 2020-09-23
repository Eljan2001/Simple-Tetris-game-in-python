#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:33:53 2020

@author: user
"""

from tkinter import*
import random 
import time
root=Tk()
root.title("TETRIS")
canvas=Canvas(root, width=800, height=800, bg='black')
canvas.pack()
L=[]
for i in range(720):
    L.append(i)
variable=0

class objects:
    
    def __init__(self, canvas, variable):
        x=random.choice(L)    
        global choice
        choice=0
        
        object2=[x, -25, x+40, -25, x+40, -5, x, -5]
        object3=[x, -25, x+80, -25, x+80, -5, x, -5]
        object_list=[ object2, object3]
        self.variable=variable
        self.canvas=canvas
        self.entity=random.choice(object_list)
        
        if self.entity==object2:
            self.variable=2
        elif self.entity==object3:
            self.variable=3
            global colours
        colours=['red', 'blue', 'green', 'lightblue', 'pink', 'violet', 'grey']
        self.id=canvas.create_polygon(self.entity, fill=random.choice(colours))
        self.x=0
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
        global coordinates_list
        coordinates_list=[]
        self.x_1=0
        self.index=0
        self.r=0
        
    def turn_right(self, evt):
        self.r=1
    
    def turn_left(self, evt):
        self.r=2
    
    def draw(self):
        pos=self.canvas.coords(self.id)
        if pos[0]>0 and pos[2]<800:
            if self.r==1:
                pos=self.canvas.coords(self.id)
                if pos[2]>=800:
                    self.x=0
                    self.r=0
                elif pos[2]<800:    
                    self.x=2
                
            if self.r==2:
                pos=self.canvas.coords(self.id)
                if pos[0]<=0:
                    self.x=0
                    self.r=0
                elif pos[0]>0:    
                    self.x=-2
                
        if pos[2]>=800:
            if self.r==2:
                pos=self.canvas.coords(self.id)
                if pos[0]<=0:
                    self.x=0
                    self.r=0
                elif pos[0]>0:    
                    self.x=-2
        
            elif self.r==1:
                self.x=0
        if pos[0]<=0:
            if self.r==1:
                pos=self.canvas.coords(self.id)
                if pos[2]>=800:
                    self.x=0
                    self.r=0
                elif pos[2]<800:    
                    self.x=2
                
            if self.r==2:
                self.x=0
        self.canvas.move(self.id, self.x, 2)
        
        if len(coordinates_list)>self.index:
            if len(coordinates_list)>1:
                for i in coordinates_list[0:len(coordinates_list)+1]: 
                    pos=self.canvas.coords(self.id)
                    
                    if pos[7]==i[1] and \
                        ((pos[0]>=i[0] and pos[2]<=i[2])\
                         or (pos[0]>=i[0] and pos[2]>=i[2] and pos[0]<=i[2]) \
                             or (pos[0]<=i[0] and pos[2]<=i[2] and pos[2]>=i[0])\
                                 or (pos[0]<=i[0] and pos[2]>=i[2])):
                        

                        
                        x=random.choice(L)
                        self.variable=0
                        coordinates_list.append(self.canvas.coords(self.id))
                       
                        object2=[x, -25, x+40, -25, x+40, -5, x, -5]
                        object3=[x, -25, x+80, -25, x+80, -5, x, -5]
                        object_list=[object2, object3]
                        self.entity=random.choice(object_list)
                        
                        if self.entity==object2:
                            self.variable=2
                        elif self.entity==object3:
                            self.variable=3
                        self.id=canvas.create_polygon(self.entity, fill=random.choice(colours))
                        self.x=0
                        self.r=0
                    if ((pos[7]<=i[7] and pos[1]<i[1] and pos[7]>i[1]) or \
                        (pos[1]>i[1] and pos[1]<=i[7] and pos[7]>i[7])) and \
                        (pos[0]<i[0] and pos[2]==i[0]):
                        if self.r==1:                           
                            self.x=0                       
                            self.r=0
                        if self.r==2:
                            pos=self.canvas.coords(self.id)
                            if pos[0]<=0:
                                self.x=0
                                self.r=0
                            elif pos[0]>0:    
                                self.x=-2
                    if ((pos[7]<=i[7] and pos[1]<i[1] and pos[7]>i[1]) or \
                        (pos[1]>i[1] and pos[1]<=i[7] and pos[7]>i[7])) and \
                        (pos[0]==i[2] and pos[2]>i[2]):
                        if self.r==2:                           
                            self.x=0                       
                            self.r=0
                        if self.r==1:
                            pos=self.canvas.coords(self.id)
                            if pos[2]>=800:
                                self.x=0
                                self.r=0
                            elif pos[2]<800:    
                                self.x=2
                                        
            if len(coordinates_list)==1:
                    i=coordinates_list[0]
                    pos=self.canvas.coords(self.id)
                    
                    if pos[7]==i[1] and \
                        ((pos[0]>=i[0] and pos[2]<=i[2])\
                         or (pos[0]>=i[0] and pos[2]>=i[2] and pos[0]<=i[2]) \
                             or (pos[0]<=i[0] and pos[2]<=i[2] and pos[2]>=i[0])\
                                 or (pos[0]<=i[0] and pos[2]>=i[2])):                        
    
                        
                        x=random.choice(L)
                        self.variable=0
                        coordinates_list.append(self.canvas.coords(self.id))
                       
                        object2=[x, -25, x+40, -25, x+40, -5, x, -5]
                        object3=[x, -25, x+80, -25, x+80, -5, x, -5]
                        object_list=[object2, object3]
                        self.entity=random.choice(object_list)
                        
                        if self.entity==object2:
                            self.variable=2
                        elif self.entity==object3:
                            self.variable=3
                        self.id=canvas.create_polygon(self.entity, fill=random.choice(colours))
                        self.x=0
                        self.r=0
                    if ((pos[7]<=i[7] and pos[1]<i[1] and pos[7]>i[1]) or \
                        (pos[1]>i[1] and pos[1]<=i[7] and pos[7]>i[7])) and \
                        (pos[0]<i[0] and pos[2]==i[0]):
                        if self.r==1:                           
                            self.x=0                       
                            self.r=0
                        if self.r==2:
                            pos=self.canvas.coords(self.id)
                            if pos[0]<=0:
                                self.x=0
                                self.r=0
                            elif pos[0]>0:    
                                self.x=-2
                    if ((pos[7]<=i[7] and pos[1]<i[1] and pos[7]>i[1]) or \
                        (pos[1]>i[1] and pos[1]<=i[7] and pos[7]>i[7])) and \
                        (pos[0]==i[2] and pos[2]>i[2]):
                        if self.r==2:                           
                            self.x=0                       
                            self.r=0
                        if self.r==1:
                            pos=self.canvas.coords(self.id)
                            if pos[2]>=800:
                                self.x=0
                                self.r=0
                            elif pos[2]<800:    
                                self.x=2
                                        
        if self.variable==2:
            if self.canvas.coords(self.id)[7]>=800: 
                x=random.choice(L)
                self.x=0
                self.variable=0
                self.r=0
                coordinates_list.append(self.canvas.coords(self.id))
              
                object2=[x, -25, x+40, -25, x+40, -5, x, -5]
                object3=[x, -25, x+80, -25, x+80, -5, x, -5]
                object_list=[object2, object3]
                self.entity=random.choice(object_list)
                
                if self.entity==object2:
                    self.variable=2
                elif self.entity==object3:
                    self.variable=3
                self.id=canvas.create_polygon(self.entity, fill=random.choice(colours))
        if self.variable==3:
            
            if self.canvas.coords(self.id)[7]>=800:
                coordinates_list.append(self.canvas.coords(self.id))
                x=random.choice(L)
                self.variable=0
                self.x=0
                object2=[x, -25, x+40, -25, x+40, -5, x, -5]
                object3=[x, -25, x+80, -25, x+80, -5, x, -5]
                object_list=[ object2, object3]
                self.entity=random.choice(object_list)
                self.r=0
                if self.entity==object2:
                    self.variable=2
                elif self.entity==object3:
                    self.variable=3
                self.id=canvas.create_polygon(self.entity, fill=random.choice(colours))

Objects=objects(canvas, variable)
while 1:
    Objects.draw()
    root.update()
    root.update_idletasks()
    time.sleep(0.01)

root.mainloop()