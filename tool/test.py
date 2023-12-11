from greenpack_i2c_driver import (
    GreenPakI2cDriver,
    hex_dump,
    read_bits_file,
    write_bits_file,
)
import time

gp = GreenPakI2cDriver(port="COM14", control_code=0b0001)

control_codes = gp.scan_devices()
print(f"Control codes: {control_codes}")


# Dump the eeprom before.
data = gp.read_nvm_bytes(0, 256)
print(f"\nNVM before:")
hex_dump(data)
print()


# Get the new program
file_name = "test_data/blinky_nvm_fast.txt"
# file_name = "test_data/blinky_nvm_slow.txt"

print(f"Loading file {file_name}")
data = read_bits_file(file_name)
print(f"\nProgram file:")
hex_dump(data)
print()


gp.program_nvm_pages(0, data)

# Dump the eeprom after.
data = gp.read_nvm_bytes(0, 256)
print(f"\nNVM after:")
hex_dump(data)
# print()

write_bits_file("_nvm_output.txt", data)

gp.reset_device()
