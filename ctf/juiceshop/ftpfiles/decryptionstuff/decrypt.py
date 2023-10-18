import functools
import math
import fractions


def egcd(a, b):
    """Extended gcd of a and b. Returns (d, x, y) such that
    d = a*x + b*y where d is the greatest common divisor of a and b."""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def inverse(a, n):
    """Returns the inverse x of a mod n, i.e. x*a = 1 mod n. Raises a
    ZeroDivisionError if gcd(a,n) != 1."""
    d, a_inv, n_inv = egcd(a, n)
    if d != 1:
        raise ZeroDivisionError('{} is not coprime to {}'.format(a, n))
    else:
        return a_inv % n


def lcm(*x):
    """
    Returns the least common multiple of its arguments. At least two arguments must be
    supplied.
    :param x:
    :return:
    """
    if not x or len(x) < 2:
        raise ValueError("at least two arguments must be supplied to lcm")
    lcm_of_2 = lambda x, y: (x * y) // fractions.gcd(x, y)
    return functools.reduce(lcm_of_2, x)


def carmichael_pp(p, e):
    phi = pow(p, e - 1) * (p - 1)
    if (p % 2 == 1) or (e >= 2):
        return phi
    else:
        return phi // 2


def carmichael_lambda(pp):
    """
    pp is a sequence representing the unique prime-power factorization of the
    integer whose Carmichael function is to be computed.
    :param pp: the prime-power factorization, a sequence of pairs (p,e) where p is prime and e>=1.
    :return: Carmichael's function result
    """
    return lcm(*[carmichael_pp(p, e) for p, e in pp])

def decrypt(msg):
    # key_len = 256
    # lam = carmichael_lambda([(2,8), (N / key_len, 1)])
    # z = inverse(e, lam)
    # x = pow(int(msg), z, N)
    # return x
    return pow(int(msg), e, N)

def encrypt(basic, e, N):
    # ord(char)
    return pow(basic, e, N)

encrypted_document = open('announcement_encrypted.md')
lines = encrypted_document.read().splitlines()
confidential_document = open('announcement.md', 'w')
e = 65537
N = 0xCFC733D3D62AF11A935CBBA777E3BF08262629284D84095AECF7DFC63EFE38DD0680A6972D677FF04CC3D2E7C84CB4463C528EBC87680623DB37792F0315447B2A5DA8D229AFA229AF95B5249EBA3C4B3EA726F54989B76CCA9002EE10A383DE28EFE84EBC6F5B74E9F201FD1B9543679E4EF022BF728270B9687BEB10599D55

firstline = lines[0]
basic = decrypt(firstline)
print("calced encrypted: ", encrypt(basic, e, N))
print("vs")
print("real encrypted: ", firstline)

encrypted_document.close()
confidential_document.close()