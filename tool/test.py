from greenpack_driver import GreenPakDriver

gp = GreenPakDriver("COM14", 0b0001)

data = gp.read_ram_bytes_block(0, 256)
print(f"\nRAM:")
gp.hex_dump(data)
print()

print()

print(f"Writing...")
gp.write_ram_bytes_block(0, bytearray([0x12, 0x34, 0x56]))

data = gp.read_ram_bytes_block(0, 256)
print(f"\nRAM:")
gp.hex_dump(data)
print()
