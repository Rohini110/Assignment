harmonic_list = []


def get_factors(num):
    res = []
    f = 1
    while f*f <= num:
        if num % f == 0:
            res.append(f)
            if not num//f == f:
                res.append(num//f)
        f += 1
    return res


i = 0
while not len(harmonic_list) == 10:
    i += 1
    factors = get_factors(i)
    den = 0.0
    add = 0.0
    for j in factors:
        add += i/j
    den = float(add)/i
    harmonic_mean = len(factors)/den
    if harmonic_mean == int(harmonic_mean):
        harmonic_list.append(i)
print(harmonic_list)