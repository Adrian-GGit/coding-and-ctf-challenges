FILE_NAME = "intro-forensics-3-original.png"
FILE_NAME_MODIFIED = "intro-forensics-3-fixed-crc.png"

png_read = open(FILE_NAME, "rb")
bytes_ = png_read.read().hex()
png_read.close()

chunks = []
next_chunk = 8*2
png_header = bytes_[:next_chunk]
while next_chunk < len(bytes_):
	chunk_len = int(bytes_[next_chunk:next_chunk + 4*2], 16)
	current_chunk_end = next_chunk + 4*2*3 + chunk_len*2
	current_chunk = bytes_[next_chunk:current_chunk_end]
	next_chunk = current_chunk_end
	chunks.append(current_chunk)

chunks = sorted(chunks, key=lambda chunk: int(chunk[len(chunk) - 4 * 2:], 16))

png_write = open(FILE_NAME_MODIFIED, "wb")
png_write.write(bytes.fromhex(png_header))
for chunk in chunks:
	png_write.write(bytes.fromhex(chunk))
png_write.close()
