#!python

from greenpak import driver, i2c
from io_extender import IoExtender, DigitalInType, PullType, ResistorValue, IoPin
import time

# port = "COM20"
port = "/dev/tty.usbmodem1101"
# device_code = 7

# Create drivers
i2c_driver = i2c.GreenPakI2cAdapter(port=port)
gp_driver = driver.GreenpakDriver(i2c_driver, "SLG46826", 0)
io_extender = IoExtender(gp_driver)

# Scan the I2C bus, to verify that the device exists.
device_codes = gp_driver.scan_greenpak_devices()
print(f"Greenpak device control code found: {device_codes}", flush=True)
assert device_codes
assert len(device_codes) == 1

gp_driver.set_device_control_code(device_codes[0])
gp_driver.reset_device()

pin0 = IoPin(0, gp_driver)
pin0.set_input(DigitalInType.WITH_SCHMITT_TRIGER, PullType.PULLUP, ResistorValue.RES_10K)

# Start the test
# count = 0
# while True:
#     count = (count + 1) % 256
#     # The mask causes only the least three output pins to get updated.
#     mask = 0b00000111
#     io_extender.write_output(count, mask)
#     in_value = io_extender.read_input()
#     out_value = io_extender.read_output()
#     print(
#         f"Input: {in_value:04b}, output: {out_value:08b}, count: {count:08b}",
#         flush=True,
#     )
#     assert out_value == (count & mask)
#     time.sleep(0.1)
