from time import sleep

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


def next_gen(universo, rule):
    # copiar el universo
    u = universo[:]
    # repito la primera celda al final para condicion periodica
    u.append(u[-1])

    v = []  # nueva generacion

    for n in range(len(u)-1):
        vecindad = []
        for i in [n - 1, n, n + 1]:
            vecindad.append(u[i])
        v.append(rule[tuple(vecindad)])
    return v


def to_str(universo):
    return "".join(['#' if c == '1' else ' '  for c in universo])


g0 = list("010000000000000000000000000000000000000000000000000000")
regla = siga

while True:
    try:
        g1 = next_gen(g0, regla)
        print to_str(g1)
        g0 = g1[:]
        sleep(0.2)
    except KeyboardInterrupt:
        if regla == siga:
            regla = alto
            print "alto!"
        else:
            regla = siga
            print "siga!"
        sleep(0.3)
