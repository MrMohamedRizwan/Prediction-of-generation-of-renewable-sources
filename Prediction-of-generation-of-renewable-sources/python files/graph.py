import matplotlib.pyplot as plt
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,7]
plt.xlabel('Time')
# naming the y axis
plt.ylabel('Temperature')
# plotting the points 
plt.title('Graph of Temperature')
plt.plot(x, y)
plt.show()
  
# naming the x axis

  
# giving a title to my graph
a=4
b=8

for i in range(1,100):
    plt.xlabel('Time')
# naming the y axis
    plt.ylabel('Temperature')
# plotting the points 
    plt.title('Graph of Temperature')
    x.append(a)
    y.append(b)
    plt.plot(x, y)
    plt.show()
    if(i==2):
        a=5
        b=1
    a=a+1
    b=b+7
# # function to show the plot
plt.show()