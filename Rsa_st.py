import random

def lnko(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def kibovitett_euklideszi(a, m):
    m0, y, x = m, 0, 1
    if m == 1: return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0: x = x + m0
    return x

def gyorshatvanyozas(alap, kitevo, modulus):
    eredmeny = 1
    alap = alap % modulus
    while kitevo > 0:
        if kitevo % 2 == 1:
            eredmeny = (eredmeny * alap) % modulus
        alap = (alap * alap) % modulus
        kitevo //= 2
    return eredmeny

def miller_rabin(n, k=5):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    s, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        if lnko(a, n) > 1:
            return False
        x = gyorshatvanyozas(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = gyorshatvanyozas(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def prim_gen(bitek):
    while True:
        p = random.randrange(2**(bitek - 1), 2**bitek)
        if miller_rabin(p):
            return p

def kulcs_gen(bit_hossz):
    p = prim_gen(bit_hossz // 2)
    q = prim_gen(bit_hossz // 2)
    n = p * q
    fi = (p - 1) * (q - 1)

    e = 65537
    while lnko(e, fi) != 1:
        e = random.randrange(3, fi, 2)

    d = kibovitett_euklideszi(e, fi)

    return (e, n), (d, n, p, q)

def titkositas(publikus_kulcs, nyilt_uzenet):
    e, n = publikus_kulcs
    return [gyorshatvanyozas(ord(char), e, n) for char in nyilt_uzenet]

def kinai_maradek(c, d, p, q):
    m1 = gyorshatvanyozas(c, d, p)
    m2 = gyorshatvanyozas(c, d, q)
    M = p * q
    M1 = M // p
    M2 = M // q
    c1 = kibovitett_euklideszi(q, p)
    c2 = kibovitett_euklideszi(p, q)
    return (M1 * c1 * m1 + M2 * c2 * m2) % M

def rsa_visszafejtes(privat_kulcs, titkositott_uzenet):
    d, n, p, q = privat_kulcs
    return "".join([chr(kinai_maradek(c, d, p, q)) for c in titkositott_uzenet])

def digitalis_alairas(privat_kulcs, uzenet):
    d, n, p, q = privat_kulcs
    return [kinai_maradek(ord(char), d, p, q) for char in uzenet]

def digitalis_alairas_ervenyesseg(publikus_kulcs, uzenet, alairas):
    e, n = publikus_kulcs
    return "".join([chr(gyorshatvanyozas(s, e, n)) for s in alairas]) == uzenet

def main():
    bit_hossz = 1024
    print(f"RSA Kulcs Generálás ({bit_hossz} bit)\n")
    pub, priv = kulcs_gen(bit_hossz)

    uzenet = "titkos uzenet"
    print(f"Eredeti üzenet: {uzenet}")

    titkositott = titkositas(pub, uzenet)
    visszafejtett = rsa_visszafejtes(priv, titkositott)
    print(f"Visszafejtve: {visszafejtett}")

    alairas = digitalis_alairas(priv, uzenet)
    alairas_ervenyesseg = digitalis_alairas_ervenyesseg(pub, uzenet, alairas)
    print(f"Aláírás érvényes: {alairas_ervenyesseg}")

if __name__ == "__main__":
    main()
