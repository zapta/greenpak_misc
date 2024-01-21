#!python

# This program demonstrates how to use the SpiAdapter to allow the luma.oled
# package to draw on an SPI Oled display. In this example we use a 128x64
# SH1106 display.

import time
import datetime

# import sys
# sys.path.insert(0, '../src/')

from spi_adapter import SpiAdapter, AuxPinMode
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont, ImageColor


# Related readings
# - https://buildmedia.readthedocs.org/media/pdf/luma-oled/rtd-update/luma-oled.pdf
# - https://github.com/rm-hull/luma.core/blob/master/luma/core/interface/serial.py#L260
# - https://github.com/rm-hull/luma.examples/blob/master/examples/sys_info.py
# - https://github.com/rm-hull/luma.examples/tree/master/examples
# - https://luma-oled.readthedocs.io/en/latest/
# - https://stackoverflow.com/questions/64189757/add-element-to-oled-display-via-pil-python-without-erasing-rest


# Customize for your system.
my_port = "COM18"
addr = 2
# speed = 1000000
# mode = 0
# dc_aux_pin = 0
# nrst_aux_pin = 1

# my_oled_addr = 0x3C


class MyLumaSerial:
    """Implementation of the luma.core.interface.serial interface using an SPI Adapter.
    See luma.core.interface.serial.spi for an example.
    """

    def __init__(self, port: str, addr: int):
        """Open the SPI Adapter and initialize this Luma serial instance."""
        assert isinstance(port, str)
        assert isinstance(addr, int)
        assert 0 <= addr <= 7
        self.__spi = SpiAdapter(port)
        self.__addr = addr
        # Reset the OLED.
        self.__send(bytearray(), dc=0, rst=0)
        time.sleep(0.001)
        self.__send(bytearray(), dc=0, rst=1)

    def __send(self, data: bytearray, dc: int, rst: int = 1) -> None:
        """Send data to self.__addr, with given dc and rst output values."""
        assert isinstance(data, bytearray)
        assert isinstance(dc, int)
        assert 0 <= dc <= 1
        assert isinstance(rst, int)
        assert 0 <= rst <= 1
        rst_mask = 0b10000 if rst else 0
        dc_mask = 0b01000 if dc else 0
        control_byte = rst_mask | dc_mask | self.__addr
        payload = bytearray()
        payload.append(control_byte)
        payload.extend(data)
        resp = self.__spi.send(payload, cs=0, mode=0, speed=1000000, read=False)
        assert resp is not None

    def command(self, *cmd) -> None:
        """Send to the SPI display a command with given bytes."""
        data = bytearray()
        self.__send(bytearray(list(cmd)), dc=0)
        # # Reset high, D/C low.
        # data.append(self.__control_byte(1, 0))
        # data.extend(bytearray(list(cmd)))
        # assert self.__spi.send(data, read=False, speed=speed) is not None

    def data(self, data):
        """Send to the SPI display data with given bytes."""
        # print(f"Data type: {type(data)}", flush=True)
        # data = 
        # self.__spi.write_aux_pins(1 << dc_aux_pin, 1 << dc_aux_pin)
        i = 0
        n = len(data)
        while i < n:
            # SPI Adapter limits to 256 bytes and we need one extra control byte
            # so we limit the chunks to 255 bytes.
            chunk_size = min(255, n - i)
            # print(f"Chunk size: {chunk_size}", flush=True)
            payload = bytearray(data[i : i + chunk_size])
            self.__send(payload, dc=1)
            i += chunk_size


luma_serial = MyLumaSerial(my_port, 2)
luma_device = ssd1306(luma_serial, width=128, height=64, rotate=0)
# luma_device.persist = True  # Do not clear display on exit


font1 = ImageFont.truetype("./fonts/FreePixel.ttf", 16)
font2 = ImageFont.truetype("./fonts/OLED.otf", 12)
white = ImageColor.getcolor("white", "1")
black = ImageColor.getcolor("black", "1")

while True:
    time_str = "{0:%H:%M:%S}".format(datetime.datetime.now())
    print(f"Drawing {time_str}", flush=True)
    # The canvas is drawn from scratch and is sent in its entirety to the display
    # upon exiting the 'with' clause.
    with canvas(luma_device) as draw:
        draw.rectangle(luma_device.bounding_box, outline=white, fill=black)
        draw.text((43, 14), f"OLED {2}", fill=white, font=font1)
        draw.text((33, 40), f"{time_str}", fill=white, font=font2)
        # Uncomment to save screenshot.
        # draw._image.save("oled_demo_screenshot.png")
    time.sleep(1.0)
