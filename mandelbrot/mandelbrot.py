import numpy as np
import png
from colour import Color
blue = Color("black")
red = Color("darkblue")
yes = Color("darkgreen")
palette = list(red.range_to(blue, 50)) + list(blue.range_to(yes, 51))

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


width = 1400
height = 1200

xscale = Scale(domain=[0, width - 1], range=[-2, 1])
yscale = Scale(domain=[0, height - 1], range=[-1, 1])

colorscale = Scale(domain=[0, 1], range=[0, 255])

plot = []

for i in range(width):
    row = []
    for j in range(height):
        counter = in_set(complex(xscale.linear(i),
                                 yscale.linear(j)))
        row += [int(colorscale.linear(c))
                for c in palette[counter].get_rgb()]
    plot.append(tuple(row))


with open('mandelbrot.png', 'wb') as f:
    w = png.Writer(height, width)
    w.write(f, plot)
