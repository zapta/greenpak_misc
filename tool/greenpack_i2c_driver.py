# A library to manage and program GreenPAK devices using a I2CDriver or I2CDriver Mini adapters.

# Docs
# https://www.renesas.com/us/en/document/mat/system-programming-guide-slg468246?r=1572991
# https://www.renesas.com/us/en/document/mat/slg47004-system-programming-guide?r=1572991

import i2cdriver
from enum import Enum
from typing import Optional, List, Tuple
import time

# TODO: Erase only if not already erased.
# TODO: Handle and verify device ids.
# TODO: Add prevention of bricking or locking.
# TODO: Add high level operation such as setting the I2C address.
# TODO: Convert the print messages to log messages.
# TODO: Add a more graceful handling of errors.
# TODO: in __program_page(), use polling of write completion instead of a blind wait.
# TODO: Add a file with the main() of the command line tool.


class MemorySpace(Enum):
    """The three memory spaces of GreenPAKS."""

    REGISTER = 1
    NVM = 2
    EEPROM = 3


class GreenPakI2cDriver:
    """Each instance controls an I2C bus with one or more GreenPAK devices."""

    def __init__(self, port: str, control_code=0b0001):
        """Initialize using a I2CDrivcer serial port and GreenPAK device control code.."""
        self.set_control_code(control_code)
        self.__i2c = i2cdriver.I2CDriver(port, reset=False)

    def set_control_code(self, control_code: int) -> None:
        """Set the GreenPAK device control code to use. Should be in [0, 15]"""
        assert 0 <= control_code <= 15
        self.__control_code = control_code

    def get_control_code(self) -> int:
        """Get the current GreenPAK device control code in use."""
        return self.__control_code

    def __i2c_device_addr(self, memory_space: MemorySpace) -> int:
        """Constructs the I2C device address for the given memory space."""
        assert memory_space in (
            MemorySpace.REGISTER,
            MemorySpace.NVM,
            MemorySpace.EEPROM,
        )
        assert 0 <= self.__control_code << 15
        memory_space_table = {
            MemorySpace.REGISTER: 0b000,
            MemorySpace.NVM: 0b010,
            MemorySpace.EEPROM: 0b011,
        }
        device_i2c_addr = self.__control_code << 3 | memory_space_table[memory_space]
        assert 0 <= device_i2c_addr <= 127
        return device_i2c_addr

    def __read_bytes(
        self, memory_space: MemorySpace, start_address: int, n: int
    ) -> bytearray:
        """An internal method to read a arbitrary block of bytes from a device's memory space."""
        # Sanity checks
        assert memory_space in (
            MemorySpace.REGISTER,
            MemorySpace.NVM,
            MemorySpace.EEPROM,
        )
        assert 0 <= start_address <= 255
        assert 0 < n
        assert start_address + n <= 256

        # Construct the i2c address.
        device_i2c_addr = self.__i2c_device_addr(memory_space)

        # Write the start address to read.
        ack = self.__i2c.start(device_i2c_addr, 0)
        assert ack
        ack = self.__i2c.write([start_address])
        assert ack
        # self.__i2c.stop()

        # Start again (with no stop) to read the N bytes
        ack = self.__i2c.start(device_i2c_addr, 1)
        assert ack
        resp_bytes = self.__i2c.read(n)
        self.__i2c.stop()

        assert n == len(resp_bytes)
        return resp_bytes

    def read_register_bytes(self, start_address: int, n: int) -> bytearray:
        """Read an arbitrary block of bytes from device's REGISTER memory space."""
        return self.__read_bytes(MemorySpace.REGISTER, start_address, n)

    def read_nvm_bytes(self, start_address: int, n: int) -> bytearray:
        """Read an arbitrary block of bytes from device's NVM memory space."""
        return self.__read_bytes(MemorySpace.NVM, start_address, n)

    def read_eeprom_bytes(self, start_address: int, n: int) -> bytearray:
        """Read an arbitrary block of bytes from device's EEPROM memory space."""
        return self.__read_bytes(MemorySpace.EEPROM, start_address, n)

    def hex_dump(self, data: bytearray, start_addr: int = 0) -> None:
        """Dump a block of bytes in hex format."""
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
            print(f"{row_addr:02x}: {" ".join(items)}", flush=True)
            row_addr += 16

    def __write_bytes(
        self, memory_space: MemorySpace, start_address: int, data: bytearray
    ) -> None:
        """An low level method to write a block of bytes to a device memory space.
        For NVM and EEPROM spaces, the block must exactly one page, the
        page must be erased, and user must wait for the operation to complete.
        """
        assert memory_space in (
            MemorySpace.REGISTER,
            MemorySpace.NVM,
            MemorySpace.EEPROM,
        )
        n = len(data)
        assert 0 <= start_address <= 255
        assert 0 < n
        assert start_address + n <= 256

        # For NVM and EEPROM it must be exactly one page.
        if memory_space in (MemorySpace.NVM, MemorySpace.EEPROM):
            assert start_address % 16 == 0
            assert n == 16

        # Construct the device i2c address
        device_i2c_addr = self.__i2c_device_addr(memory_space)
        # print(f"device_i2c_addr: 0x{device_i2c_addr:02x}", flush=True)

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

    def __read_page(self, memory_space: MemorySpace, page_id: int) -> bool:
        """Read a 16 bytes page of a NVM or EEPROM memory spaces."""
        assert memory_space in (MemorySpace.NVM, MemorySpace.EEPROM)
        assert 0 <= page_id <= 15
        device_i2c_addr = self.__i2c_device_addr(memory_space)
        data = self.__read_bytes(memory_space, page_id << 4, 16)
        assert len(data) == 16
        return data

    def __erase_page(self, memory_space: MemorySpace, page_id: int) -> None:
        """Erase a 16 bytes page of NVM or EEPROM spaces to all zeros"""
        assert memory_space in (MemorySpace.NVM, MemorySpace.EEPROM)
        assert 0 <= page_id <= 15

        # Erase only if needed
        if self.__is_page_erased(memory_space, page_id):
            print(f"Page {memory_space.name}/{page_id:02d} already erased.", flush=True)
            return

        # Erase.
        print(f"Erasing page {memory_space.name}/{page_id:02d}.", flush=True)
        # We erase by writing to the register ERSR byte, and waiting.
        msb = {MemorySpace.NVM: 0x80, MemorySpace.EEPROM: 0x90}[memory_space]
        ersr_byte = msb | page_id
        # print(f"ersr byte: {ersr_byte:02x}", flush=True)
        device_i2c_addr = self.__i2c_device_addr(MemorySpace.REGISTER)
        self.write_register_bytes(0xE3, bytearray([ersr_byte]))
        time.sleep(0.025)

        # Verify that the page is all zeros.
        assert self.__is_page_erased(memory_space, page_id)
        # print(f"Page {memory_space}/{page_id} erased OK.", flush=True)

    def __is_page_erased(self, memory_space: MemorySpace, page_id: int) -> bool:
        """Returns true if all 16 bytes of given MVM or EEPROM page are zero."""
        data = self.__read_page(memory_space, page_id)
        # print(f"\nVerifying erased.", flush=True)
        # self.hex_dump(data)
        return all(val == 0 for val in data)

    def __program_page(
        self, memory_space: MemorySpace, page_id: int, page_data: bytearray
    ) -> None:
        """Program a NVM or EEPROM 16 bytes page."""
        assert memory_space in (MemorySpace.NVM, MemorySpace.EEPROM)
        assert 0 <= page_id <= 15
        assert len(page_data) == 16

        # Do nothing if already has the desired value.
        old_data = self.__read_page(memory_space, page_id)
        if old_data == page_data:
            print(f"Page {memory_space.name}/{page_id:02d} no change.", flush=True)
            return

        # Erase the page to all zeros.
        self.__erase_page(memory_space, page_id)

        # Write the new page data.
        print(f"Writing page {memory_space.name}/{page_id:02d}.")
        self.__write_bytes(memory_space, page_id << 4, page_data)
        time.sleep(0.025)

        # Wait for completion. This is faster than a 20ms blind wait.
        # device_i2c_addr = self.__i2c_device_addr(memory_space)
        # start_time = time.time()
        # while True:
        #     ack: bool = self.__i2c.start(device_i2c_addr, 1)
        #     self.__i2c.stop()
        #     elapsed_secs = time.time() - start_time
        #     if ack:
        #         print(f"{memory_space}/{page_id} write completed in {elapsed_secs*1000:.0f}ms")
        #         break
        #     assert elapsed_secs < 0.05

        # Read and verify the page's content.
        actual_page_data = self.__read_page(memory_space, page_id)
        assert actual_page_data == page_data

    def __program_pages(
        self, memory_space: MemorySpace, start_page_id: int, pages_data: bytearray
    ) -> None:
        """Program one or mage 16 bytes pages of the NVM or EEPROM spaces."""
        assert memory_space in (MemorySpace.NVM, MemorySpace.EEPROM)
        assert 0 <= start_page_id <= 15
        assert 1 < len(pages_data)
        assert (len(pages_data) % 16) == 0
        assert (start_page_id << 4) + len(pages_data) <= 256

        num_pages = len(pages_data) // 16
        assert 0 < num_pages
        assert start_page_id + num_pages <= 16
        for i in range(0, num_pages):
            self.__program_page(
                memory_space, start_page_id + i, pages_data[i << 4 : (i + 1) << 4]
            )

        # Verify all the pages at once, just in case.
        actual_pages_data = self.__read_bytes(
            memory_space, start_page_id << 4, len(pages_data)
        )
        assert actual_pages_data == pages_data

    def write_register_bytes(self, start_address: int, data: bytearray) -> None:
        """Write a block of bytes to device's Register (RAM) space."""
        self.__write_bytes(MemorySpace.REGISTER, start_address, data)

    def program_nvm_pages(self, start_page_id: int, pages_data: bytearray) -> None:
        """Program one or mage 16 bytes pages of the NVM space."""
        self.__program_pages(MemorySpace.NVM, start_page_id, pages_data)

    def program_eeprom_pages(self, start_page_id: int, pages_data: bytearray) -> None:
        """Program one or mage 16 bytes pages of the EEPROM space."""
        self.__program_pages(MemorySpace.EEPROM, start_page_id, pages_data)