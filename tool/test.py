
import i2cdriver

# See product manual at https://i2cdriver.com/i2cdriver.pdf

i2c = i2cdriver.I2CDriver("COM14")
i2c.setspeed(400)
# 2.2K pullups SDA and CLK.
i2c.setpullups(0b001001)
i2c.scan()
ack = i2c.start(0x48, 1)
print(f"Start ack: {ack}")
resp = i2c.read(2)
i2c.stop()
print(f"resp: {resp}")


