from typing import Optional, List, Tuple
from serial import Serial
import time


class I2cPicoDriver:
    def __init__(self, port: str):
        self.__serial: Serial = Serial(port, timeout=1.0)
        if not self.test_connection_to_driver():
            raise RuntimeError(f"i2c driver not detected at port {port}")

    def test_connection_to_driver(self, max_tries: int = 3) -> bool:
        assert max_tries > 0
        for i in range(max_tries):
            if i > 0:
                # Delay to let any pending command to timeout.
                time.sleep(0.3)
            ok: bool = True
            for b in [0x00, 0xFF, 0x5A, 0xA5]:
                if not self.__test_echo_cmd(b):
                    ok = False
                    break
            if ok:
                # We had one good pass on all patterns. We are good.
                return True
        # All tries failed.
        return False

    def __test_echo_cmd(self, b: int) -> bool:
        """Test if an echo command with given byte returns the same byte."""
        assert isinstance(b, int)
        assert 0 <= b <= 256
        payload = bytearray()
        # print(f"Type: {type(ord("e"))}")
        payload.append(ord("e"))
        payload.append(b)
        self.__serial.write(bytearray([ord("e"), b]))
        resp = self.__serial.read(1)
        assert isinstance(resp, bytes), type(resp)
        assert len(resp) == 1
        return resp[0] == b
      
    def i2c_write(self, device_address: int, data: bytearray) -> bool:
      """Write data to the I2C device, return True if ok."""
      assert isinstance(device_address, int)
      assert 0 <= device_address <= 127
      assert isinstance(data, bytearray)
      assert 0 < len(data) <= 256
      payload = bytearray()
      payload.append(ord("w"))
      payload.append(device_address)
      payload.append(len(data))
      payload.extend(data)
      n_written = self.__serial.write(payload)
      if n_written != len(payload):
        print(f"I2C write: write mismatch, expected {len(payload)}, got {n_written}")
        return False
      resp = self.__serial.read(2)
      if len(resp) != 2:
        print(f"I2C write: response mismatch, expected {2}, got {n_written}")
        return False
      if resp[0] not in (ord('E'), ord('K')):
        print(f"I2C write: unexpected status in response: {resp}")
        return False  
      if resp[0] == ord('K'):
        return True
      print(f"I2C write failed: status = {resp[1]:02x}")
      return False

      
      
