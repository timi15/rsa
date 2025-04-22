def euclid_alg(a, b):
    while b != 0:
        d = a
        a = b
        b = d % a
    return a

# print(euklideszi_alg(15, 2))
