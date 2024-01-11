

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


# data = gp_driver.read_register_bytes(0x74, 1)
# assert len(data) == 1
# b = data[0]
# result = ((b & 0b00000110) >> 1) | ((b & 0b01100000) >> 3)
# print(f"Value = {result:04b}")

class I2cExtender:
  def __init__(self, gp_driver: driver.GreenPakI2cInterface):
    self.__gp_driver = gp_driver
    
  def read_input(self) -> int:
    """Read the 4 input pins and return their value as a 4 bits int."""
    data = self.__gp_driver.read_register_bytes(0x74, 1)
    assert len(data) == 1
    b = data[0]
    return ((b & 0b00000110) >> 1) | ((b & 0b01100000) >> 3)
  

extender = I2cExtender(gp_driver)

while True:
  v = extender.read_input()
  print(f"Input: {v:04b}", flush=True)
  time.sleep(1.0)
  

