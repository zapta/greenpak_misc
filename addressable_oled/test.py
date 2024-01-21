
#import sys
#sys.path.insert(0, '../src/')

import time
from spi_adapter import SpiAdapter, AuxPinMode

port = "COM18"

print(f"Connecting to port {port}...", flush=True)
spi =  SpiAdapter(port = port)
print(f"Connected.", flush=True)


i = 0
while True:
  i += 1
  print(f"\nLoop {i:04d}", flush=True)

  rst_bit = bool(i & 4)
  dc_bit = bool(i & 2)

  rst_mask = 0b10000 if rst_bit else 0
  dc_mask  = 0b01000 if dc_bit else 0

  for addr in [0, 1, 2, 4, 3, 5, 6, 7] :
    assert isinstance(addr, int)
    assert 0 <= addr <= 7
    ctrl_byte = rst_mask | dc_mask | addr 
    data = bytearray([ctrl_byte, 1, 2, 3])
    result = spi.send(data, mode=0, read=True)
    print(f"{i:04d} Result: {result.hex(' ')}", flush=True)
  time.sleep(0.01)
  


