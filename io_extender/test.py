from greenpak import driver, i2c
from io_extender import IoExtender
import time

port = "COM20"
device_code = 7

# Create drivers
i2c_driver = i2c.GreenPakI2cAdapter(port=port)
gp_driver = driver.GreenpakDriver(i2c_driver, "SLG46826", device_code)
io_extender = IoExtender(gp_driver)

# Scan the I2C bus, to verify that the device exists.
device_codes = gp_driver.scan_greenpak_devices()
print(f"Greenpak device control code found: {device_codes}", flush=True)
assert device_codes
assert device_code in device_codes
gp_driver.reset_device()


# Start the test
count = 0
while True:
    count = (count + 1) % 256
    # The mask causes only the least three output pins to get updated.
    mask = 0b00000111
    io_extender.write_output(count, mask)
    in_value = io_extender.read_input()
    out_value = io_extender.read_output()
    print(
        f"Input: {in_value:04b}, output: {out_value:08b}, count: {count:08b}",
        flush=True,
    )
    assert out_value == (count & mask)
    time.sleep(0.1)
