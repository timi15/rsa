def extended_euclid_alg(a, b):
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    s = 1

    while b != 0:
        r = a % b
        q = a // b
        a = b
        b = r
        x = x1
        y = y1
        x1 = q * x1 + x0
        y1 = q * y1 + y0
        x0 = x
        y0 = y
        s = -s

    x = s * x0
    y = -s * y0
    (d, x, y) = (a, x, y)

    return d, x, y

# print(kibovitett_euklideszi_alg(655, 321))
