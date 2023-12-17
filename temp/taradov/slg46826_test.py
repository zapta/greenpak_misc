#!/usr/bin/env python
# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2023, Alex Taradov <alex@taradov.com>. All rights reserved.
import os
import sys
import time
import serial
import slg46826

#------------------------------------------------------------------------------
i2c_addr = 0x10 # SRAM
#i2c_addr = 0x14 # NVM
#i2c_addr = 0x16 # EEPROM

#------------------------------------------------------------------------------
def print_array(arr):
  for i in range(16):
    print('%02x: %s' % (i*16, ' '.join(['%02x' % v for v in arr[i*16:i*16+16]])))

#------------------------------------------------------------------------------
def i2c_response(port):
  s = ''
  while not s.endswith('#'):
    s += port.read(port.inWaiting()).decode()
  assert s != '>@#'
  assert s[0] == '>' and s[-1] == '#' and len(s) % 2 == 0, s
  return [int(v, 16) for v in list(map(''.join, zip(*[iter(s[1:-1])]*2)))]

#------------------------------------------------------------------------------
def i2c_write(port, addr, data):
  s = '>%02x%02x%02x%s#' % (i2c_addr, len(data), addr, ''.join(['%02x' % d for d in data]))
  port.write(s.encode())
  assert i2c_response(port) == []

#------------------------------------------------------------------------------
def i2c_read(port, addr, size):
  i2c_write(port, addr, [])
  s = '<%02x%02x#' % (i2c_addr | 1, size-1)
  port.write(s.encode())
  return i2c_response(port)

#------------------------------------------------------------------------------
def write_virt(port, value):
  v = 0
  for i in range(8):
    v |= (((value >> i) & 1) << (7-i))
  i2c_write(port, 0x7a, [v])

#------------------------------------------------------------------------------
def read_out(port, index):
  value = i2c_read(port, 0x74 + index // 8, 1)
  return (value[0] >> (index % 8)) & 1

#------------------------------------------------------------------------------
config = """
i2c.addr = 1 # default

osc0.power   = always
osc0.matrix  = off
osc0.pre_div = 8
osc0.div1    = 1
osc0.out1    = enable

cnt_dly_1.clk_src = osc0
cnt_dly_1.dly_in  = low
cnt_dly_1.data    = 128
cnt_dly_1.fn_edge = rising_edge_reset
cnt_dly_1.sync    = 2dff

lut2_0.in0 = dff_1
lut2_0.in1 = dff_1
lut2_0.lut = nand

dff_1.clk = cnt_dly_1
dff_1.d   = lut2_0

io14.input_mode = digital_schmitt
io14.pull_value = 10K
io14.pull_mode  = up

lut2_3.in0 = dff_1
lut2_3.in1 = io14
lut2_3.lut = and

io6.output_mode = push_pull_2x
io6.output      = lut2_3
io6.output_oe   = enable

io3.output_mode = push_pull_2x
io3.output      = osc0_1
io3.output_oe   = enable
"""

code = slg46826.generate(config)

print('--------------------------')
print_array(code)

#------------------------------------------------------------------------------
port = serial.Serial('/dev/ttyACM0', 115200, timeout=0.5)
#port = serial.Serial('COM27', 115200, timeout=0.5)

vs = i2c_read(port, 0, 256)
#print_array(vs)

VIRT = 0x7a

i2c_write(port, VIRT, [0x11])
print(hex(i2c_read(port, VIRT, 1)[0]))

i2c_write(port, VIRT, [0x22])
print(hex(i2c_read(port, VIRT, 1)[0]))

i2c_write(port, VIRT, [0x33])
print(hex(i2c_read(port, VIRT, 1)[0]))

i2c_write(port, 0, code[0:0xf1])

port.close()


