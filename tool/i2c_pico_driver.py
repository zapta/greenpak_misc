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
      n = self.__serial.write(payload)
      if n != len(payload):
        print(f"I2C write: write mismatch, expected {len(payload)}, got {n}")
        return False
      resp = self.__serial.read(2)
      assert isinstance(data, bytearray), type(data)
      if len(resp) != 2:
        print(f"I2C write: response mismatch, expected {2}, got {len(resp)}")
        return False
      if resp[0] not in (ord('E'), ord('K')):
        print(f"I2C write: unexpected status in response: {resp}")
        return False  
      if resp[0] == ord('K'):
        return True
      print(f"I2C write: failed with status = {resp[1]:02x}")
      return False
    
    def i2c_read(self, device_address: int, byte_count: int) -> Optional[bytearray]:
      """Read a given number of bytes from the device. Returns the bytes or None if error."""
      assert isinstance(device_address, int)
      assert 0 <= device_address <= 127
      assert isinstance(byte_count, int)
      assert 0 < byte_count <= 256
      payload = bytearray()
      payload.append(ord("r"))
      payload.append(device_address)
      payload.append(byte_count)
      n = self.__serial.write(payload)
      if n != len(payload):
        print(f"I2C read: write mismatch, expected {len(payload)}, got {n}")
        return None
      resp = self.__serial.read(2)
      assert isinstance(resp, bytes), type(resp)
      if len(resp) != 2:
        print(f"I2C read: response mismatch, expected {2}, got {len(resp)}")
        return None
      if resp[0] not in (ord('E'), ord('K')):
        print(f"I2C read: unexpected status in response: {resp}")
        return None  
      if resp[0] == ord('E'):
        print(f"I2C read: failed with status = {resp[1]:02x}")
        return None
      actual_count = resp[1]
      assert actual_count == byte_count
      data = self.__serial.read(actual_count)
      assert isinstance(data, bytes), type(data)
      if len(data) != byte_count:
        print(f"I2C read: expected to read{byte_count} data byte, found {len(data)}")
        return None  
      return bytearray(data)
        
      
      
    
    

      
      
