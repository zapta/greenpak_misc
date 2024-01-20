#!python

from greenpak import driver, i2c, utils
import time
import sys

#port = "COM20"
port = "COM17"
file_name = "./addressable_oled.hex"
#device_code = 15 

i2c_driver = i2c.GreenPakI2cAdapter(port = port)
gp_driver = driver.GreenpakDriver(i2c_driver, "SLG46826", 0)

device_codes = gp_driver.scan_greenpak_devices()
print(f"Greenpak device control codes found: {device_codes}", flush=True)
assert device_codes
assert len(device_codes) == 1
#assert device_code in device_codes
gp_driver.set_device_control_code(device_codes[0])

print(f"Loading file {file_name}")
data = utils.read_hex_config_file(file_name)
print(f"\nProgram loaded from file:")
utils.hex_dump(data)
print()


# Program the new program into the device.
gp_driver.program_nvm_pages(0, data)
time.sleep(0.1)

gp_driver.reset_device()
time.sleep(0.1)

control_codes = gp_driver.scan_greenpak_devices()
print(f"Greenpak device control codes found: {control_codes}", flush=True)

