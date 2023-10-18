from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# confidential_document = open('announcement.md', 'r')
encrypted_document = open('announcement_encrypted.md', 'r')
N = 0xCFC733D3D62AF11A935CBBA777E3BF08262629284D84095AECF7DFC63EFE38DD0680A6972D677FF04CC3D2E7C84CB4463C528EBC87680623DB37792F0315447B2A5DA8D229AFA229AF95B5249EBA3C4B3EA726F54989B76CCA9002EE10A383DE28EFE84EBC6F5B74E9F201FD1B9543679E4EF022BF728270B9687BEB10599D55
e = 65537
msg = encrypted_document.readlines()
msg = " ".join(msg)

def decrypt(self, c):
    # compute c**e (mod n)
    if (hasattr(self,'p') and hasattr(self,'q') and hasattr(self,'u')):
        m1 = pow(c, e % (self.p-1), self.p)
        m2 = pow(c, e % (self.q-1), self.q)
        h = m2 - m1
        if (h<0):
            h = h + self.q
        h = h*self.u % self.q
        return h*self.p+m1
    return pow(c, self.d, self.n)

def encrypt(self, m):
    # compute m**e (mod n)
    return pow(m, e, N)