import png
from colour import Color
black = Color("black")
blue = Color("darkblue")
yellow = Color('yellow')
green = Color("darkgreen")
palette = list(blue.range_to(green, 33)) \
          + list(green.range_to(yellow, 34)) \
          + list(yellow.range_to(black, 35))


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


m = Mandelbrot(width=500, height=400)
m.plot()
