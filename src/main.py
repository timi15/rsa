from core.rsa_core import key_generation, encrypt, decrypt
from signature.digital_signature import sign, verify


def main():
    (e, n), d ,(p, q) = key_generation()

    print(f"public key: {e, n}, \t secret key: {d}")
    print(f"e: {e} \t n:{n} \t d: {d}")
    print(f"p: {p} \t q:{q}")

    message = int(input("Give me a message: "))

    c = encrypt(message, e, n)
    m = decrypt(c, d, p, q)

    print(f"c: {c} \t m: {m}")

    signature = sign(message, d, p, q)
    print(f"Signature: {signature}")

    print(f"The signature is valid: {"Yes" if verify(m, signature, e, n) else "No"}")


if __name__ == "__main__":
    main()
