import pwn
from sympy import legendre_symbol

prime = int("""
FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1
29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD
EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245
E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED
EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D
C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F
83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D
670C354E 4ABC9804 F1746C08 CA18217C 32905E46 2E36CE3B
E39E772C 180E8603 9B2783A2 EC07A28F B5C55DF0 6F4C52C9
DE2BCBF6 95581718 3995497C EA956AE5 15D22618 98FA0510
15728E5A 8AACAA68 FFFFFFFF FFFFFFFF""".replace('\n', '').replace(' ', ''), 
16)

generator = 11
won_200 = False

# ncat --ssl 372bb762b2102b0b2ad07172-casino.challenge.master.cscg.live 31337
io = pwn.remote("372bb762b2102b0b2ad07172-casino.challenge.master.cscg.live", 31337, ssl=True)

while True:
    io.recvuntil('Commitment: ')
    s = io.recvline()
    numbers = s.split(b", ")
    A, B, mystery = int(numbers[0]), int(numbers[1]), int(numbers[2].decode('utf-8').replace("\n", ""))

    a_even = legendre_symbol(A, prime) == 1
    b_even = legendre_symbol(B, prime) == 1
    mystery_even = legendre_symbol(mystery, prime) == 1

    input_ = 1 if (a_even or b_even) == mystery_even else 0    
    io.sendlineafter("> ", str(input_))

    result = io.recvline()
    try:
        io.recvuntil("Your current balance is ")
        balance_or_flag = io.recvline().decode('utf-8')
        print(f"Current balance: {balance_or_flag}")
    except EOFError:
        io.recvline().decode('utf-8')
        print(f"Flag: {io.recvline().decode('utf-8')}")
        break
