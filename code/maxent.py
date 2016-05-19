import numpy as np
import matplotlib.pyplot as plt

# Cancer, Exercise, Smoking
# 000, 001, 010, 011, 100, 101, 110, 111

x = np.arange(0, 8)
p0 = np.ones(len(x))/len(x)
p0[0:4] *= 3
p0 /= p0.sum()

# Regions in which the conditional expectations are constrained
# P(C | S) = 0.3
# P(C | E) = 0.05
S = np.zeros(len(x), dtype="bool")
E = np.zeros(len(x), dtype="bool")
C = np.zeros(len(x), dtype="bool")

S[np.array([1, 3, 5, 7])] = 1
E[np.array([2, 3, 6, 7])] = 1
C[np.array([4, 5, 6, 7])] = 1

def constraints_badness(lam):
    p = p0*np.exp(lam[0]*C*S + lam[1]*C*E)
    p /= p.sum()

    return np.abs(p[C & S].sum()/p[S].sum() - 0.3) +\
            np.abs(p[C & E].sum()/p[E].sum() - 0.05)

import scipy.optimize
lam = scipy.optimize.minimize(constraints_badness, [0.0, 0.0], tol=1E-12).x

p = p0*np.exp(lam[0]*C*S + lam[1]*C*E)
p /= p.sum()

print(p[C & S].sum()/p[S].sum())
print(p[C & E].sum()/p[E].sum())
print(p[C & S & E].sum()/p[S & E].sum())

plt.plot(x, p0, "ro-")
plt.plot(x, p, "ko-")
plt.ylim([0, 1.1*max(p0.max(), p.max())])
plt.show()

