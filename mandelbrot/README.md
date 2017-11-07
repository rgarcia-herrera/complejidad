# Fractales

Acá tenemos una implementacin en NetLogo y otra en Python del fractal de Mandelbrot.

En [mandelbrot.py](mandelbrot.py) también hay una implementación del Julia Set.

Con ese programita hice este gif animado:

<img src="julia.gif">


## Cómo correr la versión de Python

Recomiendo el uso de un [ambiente virtual](http://virtualenv.org).

    $ virtualenv venv
    [...] # se instala el ambiente
    $ source venv/bin/activate
    (venv) $  # ambiente activado
    (venv) $ pip install -r requirements.txt
    [...] # se instalan las bibliotecas
