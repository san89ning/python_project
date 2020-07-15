#importing matplotlib library
import matplotlib.pyplot as plt 

#importing numpy library
import numpy as np

#created an empty list
mylist = []

#accept input from user
n = int(input("Enter the number of values: "))

#iterate from 0 to n
for i in range(0,n):
    ele = int(input())
    mylist.append(ele)

#print the values of list
print(mylist)

#plot the values of list
plt.plot(mylist, label = 'input values')

#labelling x and y axis
plt.xlabel('-- x-axis -->')
plt.ylabel('-- y-axis -->')

plt.legend(loc = "upper left")
plt.show()