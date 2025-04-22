def fast_exponentiation_alg(base, exp, mod):
    base = base % mod
    if exp == 0:
        return 1
    elif exp == 1:
        return base

    elif exp % 2 == 0:
        return fast_exponentiation_alg(base * base % mod, exp / 2, mod)

    else:
        return base * fast_exponentiation_alg(base, exp - 1, mod) % mod

# print(gyorshatvanyozas_alg(7, 315, 631))
