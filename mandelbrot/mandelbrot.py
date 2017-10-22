import png
from colour import Color
import random
import numpy as np

black = Color("black")
white = Color("white")
blue = Color("blue")
yellow = Color('yellow')
green = Color("darkgreen")

palette = list(black.range_to(yellow, 10)) \
          + list(yellow.range_to(green, 30)) \
          + list(green.range_to(blue, 30)) \
          + list(blue.range_to(white, 31))

#palette = list(white.range_to(black, 101))


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


class Julia:
    def __init__(self, c=None, width=800, height=600, depth=100):
        self.width = width
        self.height = height

        self.xscale = Scale(domain=[0, width - 1],
                            range=[-2, 2])
        self.yscale = Scale(domain=[0, height - 1],
                            range=[-1.5, 1.5])

        if c == None:
            while True:
                c = complex(random.random() * (2 - (-2) + 2),
                            random.random() * (1.5 - (-1.5) + 1.5))
                z = c
                for i in range(depth):
                    if abs(z) > 2:
                        break
                    z = z * z + c
                if i > 10 and i < 100:
                    break
            self.c = c
        else:
            self.c = c


        self.colorscale = Scale(domain=[0, 1],
                                range=[0, 255])

        self.depth = depth

    def in_set(self, z):
        for i in range(self.depth):
            z = z * z + self.c
            if abs(z) > 2.0:
                return i
        return self.depth

    def plot(self, filename='julia.png'):
        plot = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                z = complex(self.xscale.linear(j),
                            self.yscale.linear(i))
                counter = self.in_set(z)

                row += [int(self.colorscale.linear(c))
                        for c in palette[counter].get_rgb()]
            plot.append(tuple(row))

        with open(filename, 'wb') as f:
            w = png.Writer(width=self.width,
                           height=self.height)
            w.write(f, plot)



class Mandelbrot:

    def in_set(self, x):
        counter = 0
        a = 0
        b = 0
        while (a**2 + b**2) < 4 and counter < self.depth:
            aux = a
            a = a ** 2 - b ** 2 + x.real
            b = 2 * aux * b + x.imag
            counter += 1
        return counter

    def __init__(self, width=800, height=600, depth=100):
        self.width = width
        self.height = height

        self.xscale = Scale(domain=[0, width - 1], range=[-2, 1])
        self.yscale = Scale(domain=[0, height - 1], range=[-1, 1])

        self.colorscale = Scale(domain=[0, 1],
                                range=[0, 255])

        self.depth = depth

    def plot(self, filename='mandelbrot.png'):
        plot = []

        for i in range(self.height):
            row = []
            for j in range(self.width):
                counter = self.in_set(complex(self.xscale.linear(j),
                                              self.yscale.linear(i)))
                row += [int(self.colorscale.linear(c))
                        for c in palette[counter].get_rgb()]
            plot.append(tuple(row))

        with open(filename, 'wb') as f:
            w = png.Writer(width=self.width,
                           height=self.height)
            w.write(f, plot)


#m = Mandelbrot(width=500, height=400, depth=140)
#m.plot()

i = 0
for x in np.linspace(-2, 2, 10):
    n = 0    
    for y in np.linspace(-1.5, 1.5, 10):
        j = Julia(c=complex(x, y), width=400, height=400, depth=100)
        j.plot("julia_%03d_%03d.png" % (n, i))
        print "julia_%03d_%03d.png" % (n, i)
        n += 1
    i += 1
