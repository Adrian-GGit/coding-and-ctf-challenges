FILE_NAME = "intro-forensics-3-original.png"
FILE_NAME_MODIFIED = "intro-forensics-3-fixed.png"

png_read = open(FILE_NAME, "rb")
bytes_ = png_read.read().hex()
png_read.close()

chunks = []
NEXT_CHUNK = 8*2
PNG_HEADER = bytes_[:NEXT_CHUNK]
while NEXT_CHUNK < len(bytes_):
	CHUNK_LENGTH = int(bytes_[NEXT_CHUNK:NEXT_CHUNK + 4*2], 16)
	NEXT_NEXT_CHUNK = NEXT_CHUNK + 4*2*3 + CHUNK_LENGTH*2
	CHUNK = bytes_[NEXT_CHUNK:NEXT_NEXT_CHUNK]
	# print(CHUNK[len(CHUNK) - 4*2:])
	# print(int(CHUNK[len(CHUNK) - 4*2:], 16))
	NEXT_CHUNK = NEXT_NEXT_CHUNK
	chunks.append(CHUNK)

chunks = sorted(chunks, key=lambda chunk: int(chunk[len(chunk) - 4 * 2:], 16))

png_write = open(FILE_NAME_MODIFIED, "wb")
png_write.write(bytes.fromhex(PNG_HEADER))
for chunk in chunks:
	png_write.write(bytes.fromhex(chunk))
png_write.close()
