import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

# EXERCISE 1

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, .8, .8])

axes.plot(x, y, 'b')
axes.set_xlabel('x') # Notice the use of set_ to begin methods
axes.set_ylabel('y')
axes.set_title('title')
plt.show()

# EXECISE 2

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.2, 0.2]) # inset axes

# Larger Figure Axes 1
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('x')
axes2.set_ylabel('y')

plt.show()


# EXERCISE 3

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.3, 0.3]) # inset axes

axes1.plot(x, z, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('z')
axes1.set_xlim([0, 100])
axes1.set_ylim([0, 10000])

axes2.plot(x, y, 'b')
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_xlim([20, 22])
axes2.set_ylim([30, 50])

plt.show()

# EXERCISE 4

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,3))

axes[0].plot(x, y, 'b',ls='-')
axes[0].set_xlim([0, 100])
axes[0].set_ylim([0, 200])

axes[1].plot(x, z, 'r')
axes[1].set_xlim([0, 100])
axes[1].set_ylim([0, 10000])

plt.tight_layout()
plt.show()

