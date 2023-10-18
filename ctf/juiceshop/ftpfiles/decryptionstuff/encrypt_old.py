# Source Generated with Decompyle++
# File: encrypt.pyc (Python 2.7)

confidential_document = open('announcement.md', 'r')
N = 0xCFC733D3D62AF11A935CBBA777E3BF08262629284D84095AECF7DFC63EFE38DD0680A6972D677FF04CC3D2E7C84CB4463C528EBC87680623DB37792F0315447B2A5DA8D229AFA229AF95B5249EBA3C4B3EA726F54989B76CCA9002EE10A383DE28EFE84EBC6F5B74E9F201FD1B9543679E4EF022BF728270B9687BEB10599D55L
e = 65537
encrypted_document = open('announcement_encrypted.md', 'w')
for char in confidential_document.read():
    encrypted_document.write(str(pow(ord(char), e, N)) + '\n')

encrypted_document.close()
