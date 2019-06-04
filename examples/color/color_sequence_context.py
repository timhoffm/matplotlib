"""
=============================================
Using color sequences for parametrized curves
=============================================

A set of parametrized curves can be nicely visualized by varying the color
with the parameter.

Setting the color for a sequence of plots can be achieved by

This example samples the colors equidistantly from a colormap. The colors
are used for a color cycle context.

For ease of use, we encapsulate all the color handling logic in the context
manager ``color_context``.
"""

import contextlib
import numpy as np
import matplotlib.pyplot as plt


@contextlib.contextmanager
def color_context(n, cmap='jet'):
    """Set the color cycle to *n* values equally sampled from *cmap*."""
    if not isinstance(n, int):
        n = len(n)
    colors = plt.get_cmap(cmap)(np.linspace(0, 1, n))
    with plt.rc_context({'axes.prop_cycle': plt.cycler(color=colors)}):
        yield


##############################################################################
# We use the Planck power-spectral density in dependence of the temperature
# *T* as an example curve:

def planck(l, T):
    hc = 6.626 * 3 * 1e-26
    hc_kB = 6.626 * 3 / 1.38 * 1e-3  # hc / k_B
    return 8 * np.pi * hc / l**5 / (np.exp(hc_kB/(l*T)) - 1)

wavelengths = np.linspace(1e-7, 2e-6, 201)
temperatures = np.linspace(2000, 6000, 11)

with color_context(temperatures, 'jet'):
    for T in temperatures:
        plt.plot(wavelengths*1e9, planck(wavelengths, T), label=f'{T}K')
plt.legend()
plt.xlabel('Wavelength [nm]')
plt.ylabel('Spectral density')

plt.show()
