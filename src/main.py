from core.rsa_core import key_generation, encrypt, decrypt
from signature.digital_signature import sign, verify


def main():
    p = 257
    q = 631
    pk, sk = key_generation(p, q)
    e, n = pk
    d, _ = sk

    print(f"public key: {pk}, \t secret key: {sk}")
    print(f"e: {e} \t n:{n}")
    print(f"d: {d}")

    c = encrypt(20, e, n)
    m = decrypt(c, d, p, q)

    print(f"c: {c}")
    print(f"m: {m}")

    signature = sign(m, d, p, q)
    print(f"Signature: {signature}")

    #Valid
    print(f"The signature is valid: {"Yes" if verify(m, signature, e, n) else "No"}")

    #Invalid
    print(f"The signature is valid: {"Yes" if verify(m, signature+1, e, n) else "No"}")


if __name__ == "__main__":
    main()
