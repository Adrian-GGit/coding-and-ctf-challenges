hex_numbers = [
    "6f636970",
	"7b465443",
	"306c5f49",
	"345f7435",
	"6d5f6c6c",
	"306d5f79",
	"5f79336e",
	"32666331",
	"30613130",
	"fff2007d"
]

flag = b""
for hex_num in hex_numbers:
    from_hex = bytes.fromhex(hex_num)
    flag += bytes(reversed(from_hex))

print(flag)