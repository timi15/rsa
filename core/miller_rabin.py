from core.fast_exponentiation import fast_exponentiation_alg
import random


def isStrongPrime(n, a):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d / 2
        s = s + 1
    t = fast_exponentiation_alg(a, d, n)
    if t == 1:
        return "ProbablyPrime"
    while s > 0:
        if t == n - 1:
            return "ProbablyPrime"
        t = (t * t) % n
        s = s - 1

    return "Composite"


def isPrime(n, k=8):
    for i in range(1, k + 1):
        a = random.randint(2, n - 1)
        if isStrongPrime(n, a) == "Composite":
            return "Composite"
        return "ProbablyPrime"

# print(isPrime(257))
