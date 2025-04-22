from core.chinese_remainder_theorem import chinese_remainder_theorem_alg
from core.fast_exponentiation import fast_exponentiation_alg


def sign(m, d, p, q):
    return chinese_remainder_theorem_alg(m, d, p, q)


def verify(m, s, e, n):
    return m == fast_exponentiation_alg(s, e, n)
