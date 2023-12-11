from greenpack_i2c_driver import GreenPakI2cDriver, hex_dump, read_bits_file, write_bits_file
import time


data = read_bits_file("data/blinky.txt")
hex_dump(data)
write_bits_file("_kaka.txt", data)




# gp = GreenPakI2cDriver(port="COM14", control_code=0b0001)


# # Dump the eeprom before.
# data = gp.read_eeprom_bytes(0, 256)
# print(f"\nEEPROM before:")
# hex_dump(data)
# print()

# # Fill the eeprom with a new value.
# gp.program_eeprom_pages(0, bytearray([0x43] * 256))
# # gp.program_eeprom_pages(0, bytearray(range(0, 256)))
# # gp.program_eeprom_pages(6, bytearray([0x00 , 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99,  0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]))

# # Dump the eeprom after.
# data = gp.read_eeprom_bytes(0, 256)
# print(f"\nEEPROM after:")
# hex_dump(data)
# print()
