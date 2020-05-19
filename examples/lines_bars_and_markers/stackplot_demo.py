"""
===========================
Stackplots and streamgraphs
===========================
"""

##############################################################################
# Stackplots
# ----------
#
# Stackplots draw multiple datasets as vertically stacked areas. This is
# useful when the individual data values and addtionally their cumulative
# value are of interest.


import numpy as np
import matplotlib.pyplot as plt

year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
population_by_contient = {
    'africa': [228, 284, 365, 477, 631, 814, 1044, 1275],
    'americas': [340, 425, 519, 619, 727, 840, 943, 1006],
    'asia': [1394, 1686, 2120, 2625, 3202, 3714, 4169, 4560],
    'europe': [220, 253, 276, 295, 310, 303, 294, 293],
    'oceania': [12, 15, 19, 22, 26, 31, 36, 39],
}

plt.stackplot(year, population_by_contient.values(),
              labels=population_by_contient.keys())
plt.legend(loc='upper left')
plt.title('World population')
plt.xlabel('Year')
plt.ylabel('Number of people (millions)')

plt.show()

##############################################################################
# Streamgraphs
# ------------
#
# Using the *baseline* parameter, you can turn an ordinary stacked area plot
# with baseline 0 into a stream graph.


# Fixing random state for reproducibility
np.random.seed(19680801)


def layers(n, m):
    """Return *n* random Gaussian mixtures, each of length *m*."""
    def bump(a):
        amplitude = 1 / (.1 + np.random.random())
        x = np.linspace(0, 1, m)
        y = 2 * np.random.random() - .5
        z = 10 / (.1 + np.random.random())
        a += amplitude * np.exp(-((x - y) * z)**2)
    a = np.zeros((m, n))
    for i in range(n):
        for j in range(5):
            bump(a[:, i])
    return a


d = layers(3, 100)

fig, ax = plt.subplots()
ax.stackplot(range(100), d.T, baseline='wiggle')
plt.show()
