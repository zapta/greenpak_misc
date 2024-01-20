
#import sys
#sys.path.insert(0, '../src/')

import time
from spi_adapter import SpiAdapter, AuxPinMode

port = "COM18"

print(f"Connecting to port {port}...", flush=True)
spi =  SpiAdapter(port = port)
print(f"Connected.", flush=True)

spi.set_aux_pin_mode(0, AuxPinMode.OUTPUT)


i = 0
while True:
  i += 1
  print(f"\n{i:04d} Sending...", flush=True)

  rst_mask = 0b00010000 if (i & 4) else 0
  dc_mask  = 0b00001000 if (i & 2) else 0 
  adr = 0b010

  ctrl_byte = rst_mask | dc_mask | adr 

  data = bytearray([ctrl_byte, 1, 2, 3])
  result = spi.send(data, mode=0, read=True)
  print(f"{i:04d} Result: {result.hex(' ')}", flush=True)
  time.sleep(0.01)
  


