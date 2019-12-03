# Package imports
import numpy as np
import matplotlib.pyplot as plt

# Initialization
N = 10000

Npern = 1000                           # Number of datasets/tests (can be equal to N but it's too many)
n = N//Npern * np.arange(1, Npern+1) # Sampling size for each dataset/test

pi_array = np.zeros(Npern)           # Estimated pi for each dataset/test

n_refs = np.arange(1, N+1)           # Sampling size for reference
pi_refs = np.pi*np.ones(N)           # Numpy.pi for reference

# Pi estimation for each dataset/test
for iCnt1 in range (Npern):
    x2 = np.random.rand(n[iCnt1])
    y2 = np.random.rand(n[iCnt1])
    pi_array[iCnt1] = np.where( x2**2+y2**2 <= 1)[0].shape[0] / n[iCnt1]

# Calibration
pi_array = 4*pi_array

# Plotting

fig, ax = plt.subplots(2, 1, figsize = (6, 4), dpi= 100)

ax[0].plot(n_refs, pi_refs, label="Numpy")
ax[0].plot(n, pi_array, '.-', markersize=2, linewidth=1, label="MC")
ax[0].set_xlabel("sampling size")
ax[0].set_ylabel("pi value")
ax[0].legend()

ax[1].plot(n, np.abs(pi_array-np.pi), '.-', markersize=2, linewidth=1, label="MC")
ax[1].plot(n, 1/np.sqrt(n), label="theory 1/sqrt(N)")
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[1].set_xlabel("sampling size")
ax[1].set_ylabel("abs. error")
ax[1].legend()

fig.tight_layout()

plt.show()
