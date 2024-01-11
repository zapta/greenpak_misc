

from greenpak import driver, i2c, utils
import time
import sys

device_code = 7
port = "COM20"

i2c_driver = i2c.GreenPakI2cAdapter(port = port)
gp_driver = driver.GreenpakDriver(i2c_driver, "SLG46826", device_code)

# Scan and print available greenpack devices.
# for i in range(1000):
for i in range(1):
  control_codes = gp_driver.scan_greenpak_devices()
  if control_codes:
    print(f"Devices found control codes:", flush=True)
    for control_code in control_codes:
        print(f"  {control_code:02d}", flush=True)
  else:
    print(f"No devices found", flush=True)
  time.sleep(0.5)
  
# sys.exit()

# Dump device content before programming.
#data = driver.read_nvm_bytes(0, 256)
#print(f"\nNVM before:")
#gp.hex_dump(data)
#print()

assert len(control_codes) == 1, len(control_codes)
print(f"Setting control code to {control_codes[0]}", flush=True)
gp_driver.set_device_control_code(control_codes[0])

# Load the new program from disk. 
# file_name = "./i2c_extender.hex"
file_name = "./i2c_extender.txt"
print(f"Loading file {file_name}")
# data = utils.read_hex_config_file(file_name)
data = utils.read_bits_config_file(file_name)
print(f"\nProgram loaded from file:")
utils.hex_dump(data)
print()


# Program the new program into the device.
gp_driver.program_nvm_pages(0, data)

time.sleep(0.1)

gp_driver.reset_device()

time.sleep(0.1)

# Dump device content after programming.
data = gp_driver.read_register_bytes(0, 256)
print(f"\nRegister after:")
utils.hex_dump(data)
# print()

utils.write_bits_config_file("_register_output.txt", data)

