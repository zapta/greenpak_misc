"""Driver for the io_extender GreenPAK design."""

from greenpak import driver
from enum import Enum


class IoSelection(Enum):
    UNUSED = 0
    DIGITAL_INPUT = 1
    DIGITAL_OUTPUT = 2


class DigitalInType(Enum):
    WITHOUT_SCHMITT_TRIGER = 0
    WITH_SCHMITT_TRIGER = 1
    LOW_LEVEL = 2


digital_in_type_dict = {
    DigitalInType.WITHOUT_SCHMITT_TRIGER: 0b00000000,
    DigitalInType.WITH_SCHMITT_TRIGER: 0b00000001,
    DigitalInType.LOW_LEVEL: 0b00000010,
}


class PullType(Enum):
    PULLDOWN = 0
    PULLUP = 1
    FLOAT = 2


pull_type_dict = {
    PullType.PULLDOWN: 0b00000000,
    PullType.PULLUP: 0b01000000,
    PullType.FLOAT: 0b00000000,
}


class ResistorValue(Enum):
    RES_10K = 0
    RES_100K = 1
    RES_1M = 2


resistor_value_dict = {
    ResistorValue.RES_10K: 0b00010000,
    ResistorValue.RES_100K: 0b00100000,
    ResistorValue.RES_1M: 0b00110000,
}


# class PinMode(Enum):
#     OUTPUT_0 = 0
#     OUTPUT_1 = (1,)
#     INPUT_FLOATING = 2
#     INPUT_PULLDOWN10K = 3
#     INPUT_PULLDOWN_100K = 4
#     INPUT_PULLDOWN_1M = 5
#     INPUT_PULLUP_10K = 6
#     INPUT_PULLUP_100K = 7
#     INPUT_PULLUP_1M = 8


class IoPin:
    def __init__(self, io_num: int, gp_driver: driver.GreenpakDriver):
        assert gp_driver.get_device_type() == "SLG46826", print(
            f"[{gp_driver.get_device_type()}]", flush=True
        )
        assert isinstance(io_num, int)
        self.__io_num = io_num
        self.__gp_driver = gp_driver

    def set_unused(self):
        ctrl_byte = 0b00000000
        print(f"Control byte: {ctrl_byte:08b}", flush=True)
        self.__gp_driver.write_register_bytes(0x61, bytearray([ctrl_byte]))

    def set_input(
        self, in_type: DigitalInType, pull_type: PullType, resistor_value: ResistorValue
    ):
        assert (pull_type == PullType.FLOAT) == (resistor_value is None)
        ctrl_byte = 0b00000000
        ctrl_byte |= digital_in_type_dict[in_type]
        ctrl_byte |= pull_type_dict[pull_type]
        if resistor_value is not None:
            ctrl_byte |= resistor_value_dict[resistor_value]
        print(f"Control byte: {ctrl_byte:08b}", flush=True)
        self.__gp_driver.write_register_bytes(0x61, bytearray([ctrl_byte]))

    def set_output(self):
        pass


class IoExtender:
    """Driver for the io_extender design. Allow to read/write I/O pins via I2C.

    :param gp_driver: The underlying GreenPAK driver to use to access the IO extender.
       The gp_driver should have the control code of the IO extender set correctly.
    :type gp_driver: GreenPakI2cInterface

    """

    def __init__(self, gp_driver: driver.GreenpakDriver):
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
