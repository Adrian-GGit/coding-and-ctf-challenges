ports = [17235, 17223, 31595, 28208, 25451, 24427, 28208, 25451, 24427, 28208, 25451, 12654, 26463, 12398, 24424, 13108, 30259, 28213, 24432, 12402, 29749, 8573]
bin_data = [bin(i)[2:].zfill(8) for i in ports]

str_data = ""
for b in bin_data:
	missing_leading_zeros = 16 - len(b)
	if missing_leading_zeros > 0:
		part = missing_leading_zeros * "0" + b
	else:
		part = b
	first_part = part[:8]
	second_part = part[8:]
	decimal_first_part = int(first_part, 2)
	decimal_second_part = int(second_part, 2)
	str_data += chr(decimal_first_part) + chr(decimal_second_part)

print(str_data)