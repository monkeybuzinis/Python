#2D
import matplotlib.pyplot as plt

#if we already have X,Y value, then we use plt.scatter
plt.scatter(X, Y)
plt.show()

#if we have a function i.e Y=aX+b, we use plt.plot
plt.plot(X, Y)
plt.show()


#3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
#the line above can be written in another way
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # we can add 111 or not
ax.scatter(X[:,0], X[:,1], Y)
plt.show()

# For more information: https://matplotlib.org/stable/gallery/animation/random_walk.html#sphx-glr-gallery-animation-random-walk-py
