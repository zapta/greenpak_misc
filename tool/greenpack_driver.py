import i2cdriver
from typing import Optional, List, Tuple


class GreenPakDriver:
    def __init__(self, serial_port: str, control_code=0b0001):
        """Create a driver to access a GreenPAK device using I2CDriver Mini."""
        self.set_control_code(control_code)
        self.__i2c = i2cdriver.I2CDriver(serial_port, reset=False)

    def set_control_code(self, control_code: int) -> None:
        """Set the device control code to use."""
        assert 0 <= control_code <= 15
        self.__control_code = control_code

    def get_control_code(self) -> int:
        """Get current control code in the range [0,15]"""
        return self.__control_code

    def __i2c_device_addr(self, memory_space: int) -> int:
        """Constructs the I2C device address to access given memory address.
        Memory space is (1) RAM/Register (2) NVM, and (3) EEPROM."""
        assert 1 <= memory_space <= 3
        assert 0 <= self.__control_code << 15
        memory_space_table = {1: 0b000, 2: 0b010, 3: 0b011}
        device_i2c_addr = self.__control_code << 3 | memory_space_table[memory_space]
        assert 0 <= device_i2c_addr <= 127
        return device_i2c_addr

    def __read_bytes_block(
        self, memory_space: int, start_address: int, n: int
    ) -> bytearray:
        """An internal method to read a block bytes from a device memory space.
        Memory space is (1) RAM/Register (2) NVM, (3) EEPROM.
        """
        # Sanity checks
        # assert 1 <= memory_space <= 3
        assert 0 <= start_address <= 255
        assert 0 < n
        assert start_address + n <= 256

        # Construct device i2c address
        # memory_space_table = {1: 0b000, 2: 0b010, 3: 0b011}
        device_i2c_addr = self.__i2c_device_addr(memory_space)
        # assert 0 <= device_i2c_addr <= 127

        # Write the start address
        ack = self.__i2c.start(device_i2c_addr, 0)
        assert ack
        ack = self.__i2c.write([start_address])
        assert ack
        self.__i2c.stop()

        # Read the N bytes
        ack = self.__i2c.start(device_i2c_addr, 1)
        assert ack
        resp_bytes = self.__i2c.read(n)
        self.__i2c.stop()

        assert n == len(resp_bytes)
        return resp_bytes

    def read_ram_bytes_block(self, start_address: int, n: int) -> bytearray:
        """Read a block of bytes from device RAM (register) space."""
        return self.__read_bytes_block(1, start_address, n)

    def read_nvm_bytes_block(self, start_address: int, n: int) -> bytearray:
        """Read a block of bytes from device NVM space."""
        return self.__read_bytes_block(2, start_address, n)

    def read_eeprom_bytes_block(self, start_address: int, n: int) -> bytearray:
        """Read a block of bytes from device EEPROM space."""
        return self.__read_bytes_block(3, start_address, n)

    def hex_dump(self, data: bytearray, start_addr: int = 0) -> None:
        """Dump a block of bytes."""
        end_addr = start_addr + len(data)
        row_addr = (start_addr // 16) * 16
        while row_addr < end_addr:
            items = []
            for i in range(16):
                addr = row_addr + i
                col_space = " " if i % 4 == 0 else ""
                if addr >= end_addr:
                    break
                if addr < start_addr:
                    items.append(f"{col_space}  ")
                else:
                    items.append(f"{col_space}{data[addr - start_addr]:02x}")
            print(f"{row_addr:02x}: {" ".join(items)}")
            row_addr += 16

    def __write_bytes_block(
        self, memory_space: int, start_address: int, data: bytearray
    ) -> None:
        """An internal method to write a block bytes to a device memory space.
        Memory space is (1) RAM/Register (2) NVM, (3) EEPROM.
        """
        n = len(data)
        assert 0 <= start_address <= 255
        assert 0 < n
        assert start_address + n <= 256

        # Construct device i2c address
        # memory_space_table = {1: 0b000, 2: 0b010, 3: 0b011}
        device_i2c_addr = self.__i2c_device_addr(memory_space)
        print(f"device_i2c_addr: 0x{device_i2c_addr:02x}")
        # assert 0 <= device_i2c_addr <= 127

        # We write the start address followed by the data bytes
        payload = bytearray()
        payload.append(start_address)
        payload.extend(data)

        # Write the data
        ack = self.__i2c.start(device_i2c_addr, 0)
        assert ack
        ack = self.__i2c.write(bytearray(payload))
        assert ack
        self.__i2c.stop()

    def write_ram_bytes_block(self, start_address: int, data: bytearray) -> None:
        """Write a block of bytes to device RAM (register) space."""
        self.__write_bytes_block(1, start_address, data)
