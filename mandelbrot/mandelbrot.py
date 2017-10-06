import numpy as np


class Scale:
    """
    Rescale numbers, see D3js scale object.

    Intended use::

        s = Scale(domain=[1, 100],
        range=[0, 1])
        s.linear(50)  # 0.5

    """

    def __init__(self, domain, range=(0, 1)):
        self.domain = domain
        self.range = range

    def linear(self, a):
        """
        Linear scale.
        """
        mx = float(
            (max(self.range) - min(self.range))) \
            / (max(self.domain) - min(self.domain))
        return mx * (a - min(self.domain)) + min(self.range)


def square(x):
    return x**2


def in_set(x):
    counter = 0
    a = 0
    b = 0
    while (a**2 + b**2) < 4 and counter < 100:
        aux = a
        a = a ** 2 - b ** 2 + x.real
        b = 2 * aux * b + x.imag
        counter += 1
    return counter


width = 18
height = 18

xscale = Scale(domain=[0, width - 1], range=[-2, 1])
yscale = Scale(domain=[0, height - 1], range=[-1, 1])

a = np.zeros((width, height), dtype=complex)
plot = np.zeros((width, height), dtype=int)

for i in range(width):
    for j in range(height):
        a[i][j] = complex(xscale.linear(i), yscale.linear(j))

print a

for i in range(width):
    for j in range(height):
        plot[i][j] = in_set(a[i][j])

print plot
