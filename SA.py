#!/usr/bin/env python
# coding: utf-8

# In[63]:


import matplotlib.pyplot as plt
import numpy
class coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    @staticmethod
    def get_distance(a,b):
        return numpy.sqrt(numpy.abs(a.x-b.x)+numpy.abs(a.y-b.y))

    @staticmethod
    def get_totaldistance(coords):
        dist=0
        for first,secound in zip(coords[:-1],coords[1:]):
            dist +=coordinate.get_distance(first,secound)
        dist +=coordinate.get_distance(coords[0],coords[-1])
        return dist
if __name__=='__main__':

    coords=[]
    n=int(input("inter count of cities"))
    for i in range(n):
        coords.append(coordinate(numpy.random.uniform(),numpy.random.uniform()))

    #SA algorithm
    cost0=coordinate.get_total_distance(coords)

    t=30
    factora=0.88
    t_init=t
    for i in range (500):
        print(i,'cost=',cost0)
        
        t=t*factora
        for j in range(100):
            r1,r2=numpy.random.randint(0,len(coords),size=2)
            temp=coords[r1]
            coords[r1]=coords[r2]
            coords[r2]=temp

            cost1=coordinate.get_total_distance(coords)

            if cost1<cost0:
                cost0=cost1
            else:
                x = numpy.random.uniform()
                deltaE=(cost0-cost1)
                if x < numpy.exp(deltaE/t):
                    cost0=cost1
                else:
                    temp=coords[r1]
                    coords[r1]=coords[r2]
                    coords[r2]=temp                               
       # draw plot
    fig=plt.figure(figsize=(10,5))
    ax1=fig.add_subplot(111)
    for first,secound in zip(coords[:-1],coords[1:]):
        ax1.plot([first.x,secound.x],[first.y,secound.y],'b')
    ax1.plot([coords[0].x,coords[-1].x],[coords[0].y,coords[-1].y],'b')
    for k in coords:
        ax1.plot(k.x,k.y,'ro')
    plt.show()


# In[ ]:





# In[ ]:




