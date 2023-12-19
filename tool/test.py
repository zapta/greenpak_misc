from greenpack_i2c_driver import (
    GreenPakI2cDriver,
    hex_dump,
    read_bits_file,
    write_bits_file,
)
import time

gp = GreenPakI2cDriver(port="COM14", control_code=0b0001)

# Scan and print available greenpack devices.
control_codes = gp.scan_devices()
if control_codes:
  print(f"Devices found control codes:")
  for control_code in control_codes:
      print(f"  {control_code:02d}")
else:
  print(f"No devices found")

# Dump device content before programming.
data = gp.read_nvm_bytes(0, 256)
print(f"\nNVM before:")
hex_dump(data)
print()


# Load the new program from disk. 
file_name = "test_data/blinky_nvm_fast.txt"
# file_name = "test_data/blinky_nvm_slow.txt"
print(f"Loading file {file_name}")
data = read_bits_file(file_name)
print(f"\nProgram loaded from file:")
hex_dump(data)
print()


# Program the new program into the device.
gp.program_nvm_pages(0, data)

# Dump device content after programming.
data = gp.read_nvm_bytes(0, 256)
print(f"\nNVM after:")
hex_dump(data)
# print()

write_bits_file("_nvm_output.txt", data)

gp.reset_device()
