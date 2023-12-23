from greenpack_i2c_driver import (
    GreenPakI2cDriver,
    hex_dump,
    read_bits_file,
    write_bits_file,
)
import time
import random

gp = GreenPakI2cDriver(port="COM17", control_code=0b0001)

data = bytearray(random.randbytes(16))
print(f"Random bytes: {data.hex(sep=" ")}")
gp.program_eeprom_pages(10, bytearray(random.randbytes(16)))

# data = bytearray(random.randbytes(16))
# print(f"Random bytes: {data.hex(sep=" ")}")
# gp.program_nvm_pages(10, bytearray(random.randbytes(16)))

