# Package imports
import numpy as np
import matplotlib.pyplot as plt

# Initialization
N = 10000
x = np.random.rand(N)
y = np.random.rand(N)

circ_x = np.linspace(0,1,100)
circ_y = np.sqrt(1-circ_x**2)

# Hit-or-miss determination (w/o loop)
hit_x  = x[x**2+y**2 <= 1]  #Select only elements of x which satisfies x**2+y**2 <= 1
hit_y  = y[x**2+y**2 <= 1]
miss_x = x[x**2+y**2 > 1]
miss_y = y[x**2+y**2 > 1]

# Bug check
if (hit_x.shape[0] + miss_x.shape[0] != N) or (hit_y.shape[0] + miss_y.shape[0] != N):
    print("Bug was found in code! Fix me!")

# Pi estimator and report
pi_mc = 4* hit_x.shape[0]/N
print("N                :", N)
print("Pi (Monte Carlo) :", pi_mc)
print("Pi (Numpy)       :", np.pi)
print("Abs. Error       :", np.abs(pi_mc-np.pi))

# Plotting

fig, ax = plt.subplots(1, 1, figsize = (6, 4), dpi= 100)

ax.plot( hit_x,  hit_y,  '.', c='C0')
ax.plot(miss_x, miss_y,  '.', c='C3')
ax.plot(circ_x, circ_y, '--', c='w')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

ax.set_aspect('equal', 'box')
ax.set_facecolor("k")
plt.show()
