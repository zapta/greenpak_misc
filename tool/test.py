from greenpack_i2c_driver import GreenPakI2cDriver
import time

gp = GreenPakI2cDriver(port="COM14", control_code=0b0001)


data = gp.read_eeprom_bytes(0, 256)
print(f"\nEEPROM before:")
gp.hex_dump(data)
print()


gp.program_eeprom_pages(0, bytearray([0x43] * 256))
# gp.program_eeprom_pages(0, bytearray(range(0, 256)))
# gp.program_eeprom_pages(6, bytearray([0x00 , 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99,  0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]))


data = gp.read_eeprom_bytes(0, 256)
print(f"\nEEPROM after:")
gp.hex_dump(data)
print()
