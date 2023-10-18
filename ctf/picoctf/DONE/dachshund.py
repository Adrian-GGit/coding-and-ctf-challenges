from pwn import *
from usefulstuff import conversions
from Crypto.Util.number import long_to_bytes
import rsa

def get_enc(conn):
    e = conversions.b_to_string(conn.recvline())[3:-1]
    N = conversions.b_to_string(conn.recvline())[3:-1]
    c = conversions.b_to_string(conn.recvline())[3:-1]
    return e, N, c

def euclidean_step(a, b):
    convergent = int(a / b)
    remainder = a % b
    return convergent, remainder

def continued_fraction(n, d):
    e = []
    while True:
        convergent, remainder = euclidean_step(n, d)
        e.append(convergent)
        n, d = d, remainder
        if remainder == 0:
            break
    return e

def convergents_from_contfrac(frac):
    '''
    computes the list of convergents
    using the list of partial quotients
    '''
    convs = [];
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i]))
    return convs

def contfrac_to_rational (frac):
    '''Converts a finite continued fraction [a0, ..., an]
     to an x/y rational.
     '''
    if len(frac) == 0:
        return (0,1)
    num = frac[-1]
    denom = 1
    for _ in range(-2,-len(frac)-1,-1):
        num, denom = frac[_]*num+denom, num
    return (num,denom)

def bitlength(x):
    '''
    Calculates the bitlength of x
    '''
    assert x >= 0
    n = 0
    while x > 0:
        n = n+1
        x = x>>1
    return n


def isqrt(n):
    '''
    Calculates the integer square root
    for arbitrary large nonnegative integers
    '''
    if n < 0:
        raise ValueError('square root not defined for negative numbers')
    
    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def is_perfect_square(n):
    '''
    If n is a perfect square it returns sqrt(n),
    
    otherwise returns -1
    '''
    h = n & 0xF; #last hexadecimal "digit"
    
    if h > 9:
        return -1 # return immediately in 6 cases out of 16.

    # Take advantage of Boolean short-circuit evaluation
    if ( h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8 ):
        # take square root if you must
        t = isqrt(n)
        if t*t == n:
            return t
        else:
            return -1
    
    return -1

server = "mercury.picoctf.net"
port = 58978
conn = remote(server, port)
conn.recvline()
for i in range(1):
    e, N, c = get_enc(conn)
    e, N, c = int(e), int(N), int(c)
    cf = continued_fraction(e, N)
    convergents = convergents_from_contfrac(cf)
    for (k, d) in convergents:
        if k != 0 and ((e*d) - 1) % k == 0 and d % 2 != 0:
            phi = (e*d - 1) // k
            s = N - phi + 1
            discr = s*s - 4*N
            if (discr >= 0):
                t = is_perfect_square(discr)
                if t != -1 and (s+t) % 2 == 0:
                    print(f'Found private key: {d}')
                    print(f'Processing to decode encrypted message {c}')
                    print(long_to_bytes(int(pow(c, d, N))).decode())
                    # priv_key = rsa.PrivateKey(N, e, d)
                    # M = rsa.decrypt(c, priv_key).decode('ascii')
                    # print(f'The decrypted message is {M}')