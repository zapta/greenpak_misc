"""Driver for the io_extender GreenPAK design."""

from greenpak import driver


class IoExtender:
    """Driver for the io_extender design. Allow to read/write I/O pins via I2C.

    :param gp_driver: The underlying GreenPAK driver to use to access the IO extender.
       The gp_driver should have the control code of the IO extender set correctly.
    :type gp_driver: GreenPakI2cInterface

    """

    def __init__(self, gp_driver: driver.GreenPakI2cInterface):
        self.__gp_driver = gp_driver

    def read_input(self) -> int:
        """Reads the 4 input pins of the i2C extender.

        :returns: the value of the four input bits as an integer value.
        :rtype: int
        """
        data = self.__gp_driver.read_register_bytes(0x74, 1)
        assert len(data) == 1
        b = data[0]
        return ((b & 0b00000110) >> 1) | ((b & 0b01100000) >> 3)

    def write_output(self, value: int, mask: int = 0b11111111) -> None:
        """Write the the i2c extender output bits.

        :param value: An 8 bit value to write to the  8 output pins.
        :type value: int

        :param mask: An 8 bit value that indicates which bits of ``value`` should actually
           be written to the output pins. Only the output pins whose mask bit is 1 are
           updated while the reset maintain their value. The default value of ``mask`` causes
           all 8 bits to be updated.
        :type mask: int

        :returns: None.
        """
        assert isinstance(value, int)
        assert 0 <= value <= 255
        assert isinstance(mask, int)
        assert 0 <= mask <= 255
        if mask != 0b11111111:
            # The hardware expect inverted mask.
            self.__gp_driver.write_register_bytes(0xC9, bytearray([255 - mask]))
        self.__gp_driver.write_register_bytes(0x7A, bytearray([value]))

    def read_output(self) -> int:
        """Read the the current value of the i2c extender output bits.

        :returns: The current value of the 8 pins as an 8 bits integer value.
        :rtype: int
        """
        data = self.__gp_driver.read_register_bytes(0x7A, 1)
        assert len(data) == 1
        return data[0]
