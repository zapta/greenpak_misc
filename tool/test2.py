# A test program to exercise the RP2040 I2C driver.
import time
from i2c_pico_driver import I2cPicoDriver

driver = I2cPicoDriver(port="COM17")
assert driver.test_connection_to_driver()
print(f"Device connected.")

ok = driver.i2c_write(0x08, bytearray([0x0, 0x15, 0x34]))
print(f"Write status: {ok}")

ok = driver.i2c_write(0x08, bytearray([0x0]))
print(f"Write status: {ok}")

data = driver.i2c_read(0x08, 2)
print(f"Data: {data.hex(sep=" ")}")



