# coding: utf-8

from time import sleep


def next_gen(universo, rule):
    """
    Genera un nuevo universo usando la regla de evolucion
    """

    # copiar el universo a una variable interna de la funcion
    u = universo[:]
    # repito la primera celda al final para condicion periodica
    u.append(u[-1])

    v = []  # inicializo nueva generacion

    for n in range(len(u)-1):
        vecindad = []
        # construimos la vecindad considerando tres celdas
        for i in [n - 1,
                  n,
                  n + 1]:
            vecindad.append(u[i])
        # aplicamos la regla por cada celda y sus vecinos
        v.append(rule[tuple(vecindad)])
    return v


def to_str(universo):
    """
    mejor aspecto para imprimir la lista de unos y ceros
    """
    return "".join(['#' if c == '1'
                    else ' '
                    for c in universo])


g0 = list("010000000000000000000000000000000000000000000000000000")

siga = {
    ('0', '0', '0'): '0',
    ('0', '0', '1'): '0',
    ('0', '1', '0'): '0',
    ('0', '1', '1'): '0',
    ('1', '0', '0'): '1',
    ('1', '0', '1'): '1',
    ('1', '1', '0'): '1',
    ('1', '1', '1'): '1',
}

alto = {
    ('0', '0', '0'): '0',
    ('0', '0', '1'): '0',
    ('0', '1', '0'): '1',
    ('0', '1', '1'): '1',
    ('1', '0', '0'): '0',
    ('1', '0', '1'): '0',
    ('1', '1', '0'): '1',
    ('1', '1', '1'): '1',
}

regla = siga  # regla inicial

# simulación de semáforo
while True:
    try:
        g1 = next_gen(g0, regla)
        print to_str(g1)
        g0 = g1[:]
        sleep(0.2)
    except KeyboardInterrupt:
        # para alternar el semáforo entre alto y siga usar Ctrl-C
        if regla == siga:
            regla = alto
            print "alto!"
        else:
            regla = siga
            print "siga!"
        sleep(0.3)  # doble Ctrl-C detiene la simulacion
