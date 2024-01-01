import string

def calculation(index, original_char_ascii_num):
	calc = reduce_to_char(index + 10)
	calc_xor = reduce_to_char(calc ^ original_char_ascii_num)
	return reduce_to_char(calc_xor - 2)

def calculation_rev(index, calc_xor):
	calc_xor = reduce_to_char(calc_xor + 2)
	inv_index = reduce_to_char(10 + index)
	return reduce_to_char(calc_xor ^ inv_index)

def reduce_to_char(calc):
	if calc < 128:
		if calc < -129:
			return reduce_to_char(calc + 256)
		else:
			return calc
	else:
		return reduce_to_char(calc - 256)

original = "b9yPw:MwqcoHuFz^r-o*{>I\x10Y"
print(f'Length original: {len(original)}')
original_ascii = [ord(c) for c in original]
rev_original = ""
for index, ascii_num in enumerate(original_ascii):
	rev_original += chr(calculation_rev(index, ascii_num))
print(f'Calced from original {original}: {rev_original}')
print(f'Length rev_original: {len(rev_original)}')

brute_forced = ""
for index, c in enumerate(original):
	for printable in (string.ascii_letters + string.digits + string.punctuation):
		reved = calculation(index, ord(printable))
		if reved >= 0:
			calced = chr(reved)
			if calced == c:
				brute_forced += printable
print(f'Brute force approach: {brute_forced}')
