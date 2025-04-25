from core.extended_euclid import extended_euclid_alg
from core.fast_exponentiation import fast_exponentiation_alg


def chinese_remainder_theorem_alg(c, d, p, q):
    c1 = fast_exponentiation_alg(c, d % (p - 1), p)
    c2 = fast_exponentiation_alg(c, d % (q - 1), q)

    M = p * q
    M1 = q
    M2 = p

    (GCD, y1, y2) = extended_euclid_alg(M1, M2)

    m = c1 * M1 * y1 + c2 * M2 * y2

    while m < 0:
        m = m + M

    return m

# print(chinese_remainder_theorem_alg(15, 23, 5, 11))
