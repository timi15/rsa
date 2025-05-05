from core.fast_exponentiation import fast_exponentiation_alg
from core.extended_euclid import extended_euclid_alg
from core.euclid import euclid_alg
from core.chinese_remainder_theorem import chinese_remainder_theorem_alg
from core.miller_rabin import isPrime
import random


def prime_generation():
    while True:
        p = random.randint(5000, 10000)
        if isPrime(p) == 'ProbablyPrime':
            break

    while True:
        q = random.randint(5000, 10000)
        if isPrime(q) == 'ProbablyPrime' and q != p:
            break

    return p, q


def key_generation():
    p, q = prime_generation()

    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 0

    while True:
        e_gen = random.randrange(2, phi_n)
        if euclid_alg(phi_n, e_gen) == 1:
            e = e_gen
            break

    d = extended_euclid_alg(phi_n, e)[2]
    while d < 0:
        d += phi_n

    return (e, n), d ,(p, q)


def encrypt(m, e, n):
    return fast_exponentiation_alg(m, e, n)


def decrypt(c, d, p, q):
    return chinese_remainder_theorem_alg(c, d, p, q)
