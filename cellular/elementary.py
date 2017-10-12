def to_str(w):
    t = ""
    for row in w:
        for cell in row:
            if cell:
                t += "#"
            else:
                t += " "
        t += "\n"
    return t


def to_bool(x):
    if x == '1':
        return True
    else:
        return False


def to_tuple(x, width):
    R = [to_bool(n) for n in list(format(x, "#0%sb" % (width + 2)))[2:]]
    return tuple(R)


def next_gen(rule, trio):
    R = {}
    for n in range(8):
        R[to_tuple(n, 3)] = list(reversed(to_tuple(rule, 8)))[n]
    return R[trio]


def automata(ini, rule=30, gens=10):
    w = [ini, ]
    for i in range(gens):
        nw = []
        for j in range(len(w[0])):
            if j + 1 == len(w[0]):
                k = -1
            else:
                k = j + 1
            neighbours = (w[i][j - 1], w[i][j], w[i][k])
            nw.append(next_gen(rule, neighbours))
        w.append(nw)
    return w


init = [True if n == "1" else False
        for n in list("0000000000000001000000000000000")]

print to_str(automata(init, 193, 20))
