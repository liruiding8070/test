import matplotlib.pyplot as plt

xx = [0]
yy = [1]
step = 0.1
x = 0
y = 1
for i in range(10):
    x = x+step
    y = 1.1*y-0.2*x/y
    xx.append(x)
    yy.append(y)

plt.plot(xx, yy)
plt.show()