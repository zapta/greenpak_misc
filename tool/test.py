
import greenpak as gp

driver = gp.GreenpakDriver(port="COM17", control_code=0b0001)

# Scan and print available greenpack devices.
control_codes = driver.scan_devices()
if control_codes:
  print(f"Devices found control codes:")
  for control_code in control_codes:
      print(f"  {control_code:02d}")
else:
  print(f"No devices found")

# Dump device content before programming.
data = driver.read_nvm_bytes(0, 256)
print(f"\nNVM before:")
gp.hex_dump(data)
print()


# Load the new program from disk. 
#file_name = "test_data/blinky_nvm_fast.txt"
file_name = "test_data/blinky_nvm_slow.txt"
print(f"Loading file {file_name}")
data = gp.read_bits_file(file_name)
print(f"\nProgram loaded from file:")
gp.hex_dump(data)
print()


# Program the new program into the device.
driver.program_nvm_pages(0, data)

# Dump device content after programming.
data = driver.read_nvm_bytes(0, 256)
print(f"\nNVM after:")
gp.hex_dump(data)
# print()

gp.write_bits_file("_nvm_output.txt", data)

driver.reset_device()
