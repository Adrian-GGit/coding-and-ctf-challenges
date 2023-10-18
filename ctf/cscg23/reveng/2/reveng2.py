
hexes = ['02','EA','02','e8','fc','fd','bd','fd','f2','ec','e8','fd','fb','ea','f7','fc','ef','b9','fb','f6','ea','fd','f2','f8','f7'] #,'00']
converted_hexes = [int(h, 16) if int(h, 16) < 128 else int(h, 16) - 256 for h in hexes]
passwd = "".join([chr(h + int('77', 16)) for h in converted_hexes])
print(passwd)