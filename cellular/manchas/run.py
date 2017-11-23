from model import Universe

# inicializar simulacion
u = Universe(width=50, height=80)  # usaremos u para la simulacion en t
v = Universe(width=50, height=80)  # v para la simulacion en t + 1
u.randomiza_phenotipo()

# cuatro tiempos
for t in range(11):
    # grafica generacion
    u.plot("t%02i.png" % t)
    print "t%02i.png" % t

    v.g = u.g.copy()
    # actualizamos estado en cada patch
    for p in v.g.nodes():
        # cada patch de t+1 elige bando considerando los vecinos en t
        p.diferenciar(u.inner_neighbors(p),
                      u.outer_neighbors(p),
                      w=0.38)
    u.g = v.g.copy()
