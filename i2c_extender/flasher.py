

from greenpak import driver, i2c, utils
import time
import sys

port = "COM20"
device_code = 7

i2c_driver = i2c.GreenPakI2cAdapter(port = port)
gp_driver = driver.GreenpakDriver(i2c_driver, "SLG46826", device_code)

device_codes = gp_driver.scan_greenpak_devices()
print(f"Greenpak device control code found: {device_codes}", flush=True)
assert device_codes
assert device_code in device_codes

#file_name = "./i2c_extender.txt"
file_name = "./i2c_extender.hex"
print(f"Loading file {file_name}")
data = utils.read_hex_config_file(file_name)
#data = utils.read_bits_config_file(file_name)
print(f"\nProgram loaded from file:")
utils.hex_dump(data)
print()


# Program the new program into the device.
gp_driver.program_nvm_pages(0, data)
time.sleep(0.1)

gp_driver.reset_device()
time.sleep(0.1)

control_codes = gp_driver.scan_greenpak_devices()
print(f"Greenpak device control code found: {control_codes}", flush=True)

