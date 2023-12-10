# import i2cdriver
# import time
# from typing import Optional, List, Tuple


# class GreenPakDriver:
#     def __init__(self, serial_port: str, control_code=0b0001):
#         self.set_control_code(control_code)
#         self.__i2c = i2cdriver.I2CDriver(serial_port, reset=False)

#     def set_control_code(self, control_code: int) -> None:
#         assert 0 <= control_code <= 15
#         self.__control_code = control_code

#     def __read_block(self, memory_space: int, start_address: int, n: int) -> bytearray:
#         # Sanity checks
#         assert 1 <= memory_space <= 3
#         assert 0 <= start_address <= 255
#         assert 0 < n
#         assert start_address + n <= 256

#         # Construct device i2c address
#         memory_space_table = {1: 0b000, 2: 0b010, 3: 0b011}
#         device_i2c_addr = self.__control_code << 3 | memory_space_table[memory_space]
#         assert 0 <= device_i2c_addr <= 127

#         # Write the start address
#         ack = self.__i2c.start(device_i2c_addr, 0)
#         assert ack
#         ack = self.__i2c.write([start_address])
#         assert ack
#         self.__i2c.stop()

#         # Read the N bytes
#         ack = self.__i2c.start(device_i2c_addr, 1)
#         assert ack
#         resp_bytes = self.__i2c.read(n)
#         self.__i2c.stop()

#         assert n == len(resp_bytes)
#         return resp_bytes

#     def read_ram_block(self, start_address: int, n: int) -> bytearray:
#         return self.__read_block(1, start_address, n)

#     def read_nvm_block(self, start_address: int, n: int) -> bytearray:
#         return self.__read_block(2, start_address, n)

#     def read_eeprom_block(self, start_address: int, n: int) -> bytearray:
#         return self.__read_block(3, start_address, n)

#     def hex_dump(self, start: int, data: bytearray):
#         end_addr = start + len(data)
#         row_addr = (start // 16) * 16
#         while row_addr < end_addr:
#             items = []
#             for i in range(16):
#                 addr = row_addr + i
#                 if addr < start:
#                     items.append("  ")
#                     continue
#                 if addr >= end_addr:
#                     break
#                 items.append(f"{data[addr - start]:02x}")
#             print(f"{row_addr:02x}: {" ".join(items)}")
#             row_addr += 16


from greenpack_driver import GreenPakDriver

gp = GreenPakDriver("COM14", 0b0001)

data = gp.read_ram_block(0, 256)
print(f"\nRAM:")
gp.hex_dump(0, data)
print()

data = gp.read_nvm_block(0, 256)
print(f"\nNVM:")
gp.hex_dump(0, data)
print()

data = gp.read_eeprom_block(0, 256)
print(f"\nEEPROM:")
gp.hex_dump(0, data)
print()




