#!/usr/bin/env python
# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2023, Alex Taradov <alex@taradov.com>. All rights reserved.

matrix = {
  'low'                : 0,
  'io0'                : 1,
  'io1'                : 2,
  'io2'                : 3,
  'io3'                : 4,
  'io4'                : 5,
  'io5'                : 6,
  'io8'                : 7,
  'io9'                : 8,
  'io10'               : 9,
  'io11'               : 10,
  'io12'               : 11,
  'io13'               : 12,
  'io14'               : 13,
  'lut2_0'             : (14, [1232], 0),
  'dff_0'              : (14, [1232], 1),
  'lut2_1'             : (15, [1233], 0),
  'dff_1'              : (15, [1233], 1),
  'lut2_2'             : (16, [1234], 0),
  'dff_2'              : (16, [1234], 1),
  'lut2_3'             : (17, [1235], 0),
  'pgen'               : (17, [1235], 1),
  'lut3_0'             : (18, [1236], 0),
  'dff_3'              : (18, [1236], 1),
  'lut3_1'             : (19, [1238], 0),
  'dff_4'              : (19, [1238], 1),
  'lut3_2'             : (20, [1239], 0),
  'dff_5'              : (20, [1239], 1),
  'lut3_3'             : (21, [1240], 0),
  'dff_6'              : (21, [1240], 1),
  'lut3_4'             : (22, [1241], 0),
  'dff_7'              : (22, [1241], 1),
  'lut3_5'             : (23, [1242], 0),
  'dff_8'              : (23, [1242], 1),
  'lut3_6'             : (24, [1258, 1257], 0),
  'pipe_delay_0'       : (24, [1258, 1257], 1),
  'pipe_delay_1'       : (25, [1258, 1257], 1),
  'pipe_delay_1out'    : (26, [1258, 1257], 1),
  'ripple_counter_0'   : (24, [1258, 1257], 3),
  'ripple_counter_1'   : (25, [1258, 1257], 3),
  'ripple_counter_2'   : (26, [1258, 1257], 3),
  'edet_filter'        : 27,
  'prog_dly_edet'      : 28,
  'cnt_dly_1'          : 29,
  'osc1_1'             : 30,
  'osc0_1'             : 31,
  'osc2'               : 32,
  'cnt_dly_2'          : 33,
  'cnt_dly_3'          : 34,
  'cnt_dly_4'          : 35,
  'cnt_dly_5'          : 36,
  'cnt_dly_6'          : 37,
  'cnt_dly_7'          : 38,
  'lut4_0'             : (39, [1282], 0),
  'dff_9'              : (39, [1282], 1),
  'lut3_7'             : (40, [1339], 0),
  'dff_10'             : (40, [1339], 1),
  'lut3_8'             : (41, [1394], 0),
  'dff_11'             : (41, [1394], 1),
  'lut3_9'             : (42, [1411], 0),
  'dff_12'             : (42, [1411], 1),
  'lut3_10'            : (43, [1466], 0),
  'dff_13'             : (43, [1466], 1),
  'lut3_11'            : (44, [1483], 0),
  'dff_14'             : (44, [1483], 1),
  'lut3_12'            : (45, [1538], 0),
  'dff_15'             : (45, [1538], 1),
  'lut3_13'            : (46, [1556], 0),
  'dff_16'             : (46, [1556], 1),
  'cnt_dly_0'          : 47,
  'virt7'              : 48,
  'virt6'              : 49,
  'virt5'              : 50,
  'virt4'              : 51,
  'virt3'              : 52,
  'virt2'              : 53,
  'virt1'              : 54,
  'virt0'              : 55,
  'acmp0h'             : 56,
  'acmp1h'             : 57,
  'acmp2l'             : 58,
  'acmp3l'             : 59,
  'osc1_2'             : 60,
  'osc0_2'             : 61,
  'por_core'           : 62,
  'high'               : 63,
}

enable_v         = { 'disable': 0, 'enable': 1 }
disable_v        = { 'enable': 0, 'disable': 1 }
low_high_v       = { 'low': 0, 'high': 1 }

io_input_mode_d  = { 'digital': 0, 'digital_schmitt': 1, 'digital_lv': 2 }
io_input_mode_a  = { 'digital': 0, 'digital_schmitt': 1, 'digital_lv': 2, 'analog': 3 }
io_output_mode   = { 'push_pull_1x': 0, 'push_pull_2x': 1, 'open_drain': 2, 'open_drain': 3 }
io_pull_value    = { 'none': 0, '10K': 1, '100K': 2, '1M': 3 }
io_pull_mode     = { 'down': 0, 'up': 1 }
io_output_oe     = { 'disable': 0, 'enable': 1 }

osc_power        = { 'auto': 0, 'always': 1 }
osc_matrix       = { 'on': 0, 'off': 1 }
osc_pre_div      = { '1': 0, '2': 1, '4': 2, '8': 3 }
osc_div          = { '1': 0, '2': 1, '3': 3, '4': 2, '8': 4, '12': 5, '24': 6, '64': 7 }

acmp_hyst        = { '0mV': 0, '32mV': 1, '64mV': 2, '192mV': 3 }
acmp_gain        = { '1x': 0, '0.5x': 1, '0.33x': 2, '0.25x': 3 }
acmp_vref        = { 'io1': 0x3f } # other values are specified directly

lut2_fn          = { 'and': 0x8, 'nand': 0x7, 'or': 0xe, 'nor': 0x1, 'xor': 0x6, 'xnor': 0x9 }
lut3_fn          = { 'and': 0x80, 'nand': 0x7f, 'or': 0xfe, 'nor': 0x01, 'xor': 0x96, 'xnor': 0x69 }
lut4_fn          = { 'and': 0x8000, 'nand': 0x7fff, 'or': 0xfffe, 'nor': 0x0001, 'xor': 0x6996, 'xnor': 0x9669 }

dff_mode         = { 'dff': 0, 'latch': 1 }
dff_output       = { 'q': 0, 'qb': 1 }
dff_init         = { 'low': 0, 'high': 1 }

cnt_init         = { 'bypass': 0, 'low': 1, 'high': 2 }
cnt_output       = { 'default': 0, 'inverted': 1 }
cnt_sync         = { 'bypass': 0, '2dff': 1 }
cnt_edet         = { 'normal': 0, 'edge': 1 }

cnt_fn_edge_v = {
  'both_delay'          : 0,
  'falling_delay'       : 1,
  'rising_delay'        : 2,

  'both_one_shot'       : 3,
  'falling_one_shot'    : 4,
  'rising_one_shot'     : 5,

  'both_freq_detect'    : 6,
  'falling_freq_detect' : 7,
  'rising_freq_detect'  : 8,

  'both_edge_detect'    : 9,
  'falling_edge_detect' : 10,
  'rising_edge_detect'  : 11,

  'both_edge_reset'     : 12,
  'falling_edge_reset'  : 13,
  'rising_edge_reset'   : 14,
  'high_level_reset'    : 15,
}

cnt_clk_src_v = {
  'osc2'        : 0,
  'osc2/4'      : 1,
  'osc1'        : 2,
  'osc1/8'      : 3,
  'osc1/64'     : 4,
  'osc1/512'    : 5,
  'osc0'        : 6,
  'osc0/8'      : 7,
  'osc0/64'     : 8,
  'osc0/512'    : 9,
  'osc0/4096'   : 10,
  'osc0/32768'  : 11,
  'osc0/262144' : 12,
  'cnt_end'     : 13,
  'external'    : 14,
  'not_used'    : 15,
}

def r(msb, lsb):
  return list(range(msb, lsb-1, -1))

def m(idx):
  return r((idx+1)*6-1, idx*6)

mf_16b_map = [
  # LUT
  ( 0x00, { 'dly_in': 'low', 'in3': 'a', 'in2': 'b', 'in1': 'c', 'in0': 'd' }), # 0000000
  # DFF
  ( 0x04, { 'dly_in': 'low', 'd': 'a', 'nset': 'b', 'nrst': 'c', 'clk': 'd' }), # 0000100
  # CNT/DLY
  ( 0x01, { 'dly_in': 'd', 'up': 'a', 'keep': 'b', 'ext_clk': 'c', 'dly_out': 'lut/dff' }), # 0000001
  # CNT/DLY -> LUT
  ( 0x02, { 'dly_in': 'a', 'in3': 'dly_out', 'in2': 'b', 'in1': 'c', 'in0': 'd' }), # 0000010
  ( 0x22, { 'dly_in': 'a', 'in3': 'dly_out', 'in2': 'low', 'in1': 'c', 'in0': 'd', 'ext_clk': 'b' }), # 0100010
  ( 0x42, { 'dly_in': 'a', 'in3': 'dly_out', 'in2': 'b', 'in1': 'low', 'in0': 'd', 'ext_clk': 'c' }), # 1000010
  ( 0x0a, { 'dly_in': 'b', 'in3': 'a', 'in2': 'dly_out', 'in1': 'c', 'in0': 'd' }), # 0001010
  ( 0x4a, { 'dly_in': 'b', 'in3': 'a', 'in2': 'dly_out', 'in1': 'low', 'in0': 'd', 'ext_clk': 'c' }), # 1001010
  ( 0x12, { 'dly_in': 'c', 'in3': 'a', 'in2': 'b', 'in1': 'dly_out', 'in0': 'd' }), # 0010010
  ( 0x32, { 'dly_in': 'c', 'in3': 'a', 'in2': 'low', 'in1': 'dly_out', 'in0': 'd', 'ext_clk': 'b' }), # 0110010
  ( 0x1a, { 'dly_in': 'd', 'in3': 'a', 'in2': 'b', 'in1': 'c', 'in0': 'dly_out' }), # 0011010
  ( 0x3a, { 'dly_in': 'd', 'in3': 'a', 'in2': 'low', 'in1': 'c', 'in0': 'dly_out', 'ext_clk': 'b' }), # 0111010
  ( 0x5a, { 'dly_in': 'd', 'in3': 'a', 'in2': 'b', 'in1': 'low', 'in0': 'dly_out', 'ext_clk': 'c' }), # 1011010
  # LUT -> CNT/DLY
  ( 0x03, { 'dly_in': 'lut_out', 'in3': 'a', 'in2': 'b', 'in1': 'c', 'in0': 'd' }), # 0000011
  ( 0x23, { 'dly_in': 'lut_out', 'in3': 'a', 'in2': 'low', 'in1': 'c', 'in0': 'd', 'ext_clk': 'b' }), # 0100011
  ( 0x43, { 'dly_in': 'lut_out', 'in3': 'a', 'in2': 'b', 'in1': 'low', 'in0': 'd', 'ext_clk': 'c' }), # 1000011
  # CNT/DLY -> DFF
  ( 0x06, { 'dly_in': 'a', 'd': 'dly_out', 'nset': 'b', 'nrst': 'c', 'clk': 'd' }), # 0000110
  ( 0x26, { 'dly_in': 'a', 'd': 'dly_out', 'nset': 'high', 'nrst': 'c', 'clk': 'd', 'ext_clk': 'b' }), # 0100110
  ( 0x46, { 'dly_in': 'a', 'd': 'dly_out', 'nset': 'b ', 'nrst': 'high', 'clk': 'd', 'ext_clk': 'c' }), # 1000110
  ( 0x0e, { 'dly_in': 'b', 'd': 'a', 'nset': 'dly_out ', 'nrst': 'c', 'clk': 'd' }), # 0001110
  ( 0x4e, { 'dly_in': 'b', 'd': 'a', 'nset': 'dly_out ', 'nrst': 'high', 'clk': 'd', 'ext_clk': 'c' }), # 1001110
  ( 0x16, { 'dly_in': 'c', 'd': 'a', 'nset': 'b ', 'nrst': 'dly_out', 'clk': 'd' }), # 0010110
  ( 0x36, { 'dly_in': 'c', 'd': 'a', 'nset': 'high', 'nrst': 'dly_out', 'clk': 'd', 'ext_clk': 'b' }), # 0110110
  ( 0x1e, { 'dly_in': 'd', 'd': 'a', 'nset': 'b', 'nrst': 'c', 'clk': 'dly_out' }), # 0011110
  ( 0x3e, { 'dly_in': 'd', 'd': 'a', 'nset': 'high', 'nrst': 'c', 'clk': 'dly_out', 'ext_clk': 'b' }), # 0111110
  ( 0x5e, { 'dly_in': 'd', 'd': 'a', 'nset': 'b', 'nrst': 'high', 'clk': 'dly_out', 'ext_clk': 'c' }), # 1011110
  # DFF -> CNT/DLY
  ( 0x07, { 'dly_in': 'dff_out', 'd': 'a', 'nset': 'b', 'nrst': 'c', 'clk': 'd' }), # 0000111
  ( 0x27, { 'dly_in': 'dff_out', 'd': 'a', 'nset': 'high', 'nrst': 'c', 'clk': 'd', 'ext_clk': 'b' }), # 0100111
  ( 0x47, { 'dly_in': 'dff_out', 'd': 'a', 'nset': 'b', 'nrst': 'high', 'clk': 'd', 'ext_clk': 'c' }), # 1000111
]

slg46826 = {
  'io0': {
    'input_mode' : ([777, 776], io_input_mode_d),
    'output_mode': ([779, 778], io_output_mode),
    'pull_value' : ([781, 780], io_pull_value),
    'pull_mode'  : ([782], io_pull_mode),
    'output'     : (m(67), matrix),
    'output_oe'  : ([783], io_output_oe),
  },

  'io1': {
    'input_mode' : ([785, 784], io_input_mode_a),
    'output_mode': ([787, 786], io_output_mode),
    'pull_value' : ([789, 788], io_pull_value),
    'pull_mode'  : ([790], io_pull_mode),
    'output'     : (m(68), matrix),
    'output_oe'  : (m(69), matrix),
  },

  'io2': {
    'input_mode' : ([801, 800], io_input_mode_d),
    'output_mode': ([803, 802], io_output_mode),
    'pull_value' : ([805, 804], io_pull_value),
    'pull_mode'  : ([806], io_pull_mode),
    'output'     : (m(70), matrix),
    'output_oe'  : ([807], io_output_oe),
  },

  'io3': {
    'input_mode' : ([809, 808], io_input_mode_d),
    'output_mode': ([811, 810], io_output_mode),
    'pull_value' : ([813, 812], io_pull_value),
    'pull_mode'  : ([814], io_pull_mode),
    'output'     : (m(71), matrix),
    'output_oe'  : ([815], io_output_oe),
  },

  'io4': {
    'input_mode' : ([817, 816], io_input_mode_d),
    'output_mode': ([819, 818], io_output_mode),
    'pull_value' : ([821, 820], io_pull_value),
    'pull_mode'  : ([822], io_pull_mode),
    'output'     : (m(72), matrix),
    'output_oe'  : (m(73), matrix),
  },

  'io5': {
    'input_mode' : ([825, 824], io_input_mode_d),
    'output_mode': ([827, 826], io_output_mode),
    'pull_value' : ([829, 828], io_pull_value),
    'pull_mode'  : ([830], io_pull_mode),
    'output'     : (m(74), matrix),
    'output_oe'  : (m(75), matrix),
  },

  'io6': {
    'output_mode': ([851, 850], io_output_mode),
    'pull_value' : ([853, 852], io_pull_value),
    'pull_mode'  : ([854], io_pull_mode),
    'output'     : (m(76), matrix),
    'output_oe'  : ([855], io_output_oe),
  },

  'io7': {
    'output_mode': ([859, 858], io_output_mode),
    'pull_value' : ([861, 860], io_pull_value),
    'pull_mode'  : ([862], io_pull_mode),
    'output'     : (m(77), matrix),
    'output_oe'  : ([863], io_output_oe),
  },

  'io8': {
    'input_mode' : ([865, 864], io_input_mode_d),
    'output_mode': ([867, 866], io_output_mode),
    'pull_value' : ([869, 868], io_pull_value),
    'pull_mode'  : ([870], io_pull_mode),
    'output'     : (m(78), matrix),
    'output_oe'  : (m(79), matrix),
  },

  'io9': {
    'input_mode' : ([881, 880], io_input_mode_a),
    'output_mode': ([883, 882], io_output_mode),
    'pull_value' : ([885, 884], io_pull_value),
    'pull_mode'  : ([886], io_pull_mode),
    'output'     : (m(80), matrix),
    'output_oe'  : (m(81), matrix),
  },

  'io10': {
    'input_mode' : ([889, 888], io_input_mode_a),
    'output_mode': ([891, 890], io_output_mode),
    'pull_value' : ([893, 892], io_pull_value),
    'pull_mode'  : ([894], io_pull_mode),
    'output'     : (m(82), matrix),
    'output_oe'  : (m(83), matrix),
  },

  'io11': {
    'input_mode' : ([897, 896], io_input_mode_a),
    'output_mode': ([899, 898], io_output_mode),
    'pull_value' : ([901, 900], io_pull_value),
    'pull_mode'  : ([902], io_pull_mode),
    'output'     : (m(84), matrix),
    'output_oe'  : (m(85), matrix),
  },

  'io12': {
    'input_mode' : ([905, 904], io_input_mode_a),
    'output_mode': ([907, 906], io_output_mode),
    'pull_value' : ([909, 908], io_pull_value),
    'pull_mode'  : ([910], io_pull_mode),
    'output'     : (m(86), matrix),
    'output_oe'  : (m(87), matrix),
  },

  'io13': {
    'input_mode' : ([913, 912], io_input_mode_a),
    'output_mode': ([915, 914], io_output_mode),
    'pull_value' : ([917, 916], io_pull_value),
    'pull_mode'  : ([918], io_pull_mode),
    'output'     : (m(88), matrix),
    'output_oe'  : (m(89), matrix),
  },

  'io14': {
    'input_mode' : ([921, 920], io_input_mode_a),
    'output_mode': ([923, 922], io_output_mode),
    'pull_value' : ([925, 924], io_pull_value),
    'pull_mode'  : ([926], io_pull_mode),
    'output'     : (m(90), matrix),
    'output_oe'  : (m(91), matrix),
  },

  'scl': {
    'input_mode' : ([834, 833], io_input_mode_d),
  },

  'sda': {
    'input_mode' : ([842, 841], io_input_mode_d),
  },

  'io_common': {
    'fast_pull': ([768], enable_v),
  },

  'osc0': {
    'power'   : ([1040], osc_power),
    'matrix'  : ([1041], osc_matrix),
    'source'  : ([1042], { 'internal': 0, 'io0': 1 }),
    'pre_div' : ([1044, 1043], osc_pre_div),
    'div1'    : (r(1047, 1045), osc_div),
    'out1'    : ([1049], enable_v),
    'div2'    : (r(1061, 1059), osc_div),
    'out2'    : ([1053], enable_v),
    'enable'  : (m(58), matrix),
  },

  'osc1': {
    'power'   : ([1024], osc_power),
    'matrix'  : ([1025], osc_matrix),
    'source'  : ([1026], { 'internal': 0, 'io10': 1 }),
    'pre_div' : ([1028, 1027], osc_pre_div),
    'div1'    : (r(1031, 1029), osc_div),
    'out1'    : ([1050], enable_v),
    'div2'    : (r(1058, 1056), osc_div),
    'out2'    : ([1054], enable_v),
    'enable'  : (m(59), matrix),
  },

  'osc2': {
    'power'   : ([1032], osc_power),
    'matrix'  : ([1033], osc_matrix),
    'source'  : ([1034], { 'internal': 0, 'io8': 1 }),
    'pre_div' : ([1036, 1035], osc_pre_div),
    'div'     : (r(1039, 1037), osc_div),
    'out'     : ([1051], enable_v),
    'delay'   : ([1052], disable_v),
    'enable'  : (m(57), matrix),
  },

  'acmp0h': {
    'hyst'     : (r(1065, 1064), acmp_hyst),
    'gain'     : (r(1097, 1096), acmp_gain),
    'vref'     : (r(1103, 1098), acmp_vref),
    'input'    : ([1069, 1067], { 'io14': 0, 'io14_buf': 1, 'VDD': 2}), # TODO: verify, does not match Figure 57
    'ws'       : ([1070], enable_v),
    'current_source': ([1071], enable_v),
    'power_up' : (m(62), matrix),
  },

  'acmp1h': {
    'hyst'     : (r(1075, 1074), acmp_hyst),
    'gain'     : (r(1105, 1104), acmp_gain),
    'vref'     : (r(1111, 1106), acmp_vref),
    'input'    : ([1072, 1076], { 'io13': 0, 'io13_buf': 1, 'acmp0h': 2}), # TODO: verify, does not match Figure 58
    'ws'       : ([1078], enable_v),
    'power_up' : (m(63), matrix),
  },

  'acmp2l': {
    'hyst'     : (r(1083, 1082), acmp_hyst),
    'gain'     : (r(1113, 1112), acmp_gain),
    'vref'     : (r(1119, 1114), acmp_vref),
    'input'    : ([1081, 1080], { 'io12': 0, 'acmp0h': 1, 'acmp1h': 2}),
    'power_up' : (m(64), matrix),
  },

  'acmp3l': {
    'hyst'     : (r(1089, 1088), acmp_hyst),
    'gain'     : (r(1121, 1120), acmp_gain),
    'vref'     : (r(1127, 1122), acmp_vref),
    'input'    : ([1087, 1092], { 'io11': 0, 'acmp2l': 1, 'temp_sensor': 2}), # TODO: verify, TS does not match the description of 1087
    'power_up' : (m(65), matrix),
  },

  'acmp': {
    'ws_time'  : ([1079], { 'short': 0, 'normal': 1 }),
  },

  'temp_sensor': {
    'range'   : ([1095], { '0.62V-0.99V': 0, '0.75V-1.2V': 1 }),
    'pd_sel'  : ([1094], { 'register': 0, 'matrix': 1 }),
    'pd_ctrl' : ([1093], enable_v),
    'pd'      : (m(60), matrix),
    'bg_power_down': (m(61), matrix),
    'acmp3l_out': ([1135], enable_v),
  },

  'vref_0': {
    'output'  : ([1128], enable_v),
    'input'   : ([1130, 1129], { 'acmp0h': 1, 'acmp1h': 2, 'temp_sensor': 3 }),
    'pd_sel'  : ([1138], { 'register': 0, 'matrix': 1 }),
    'pd_ctrl' : ([1137], enable_v),
  },

  'vref_1': {
    'output'  : ([1131], enable_v),
    'input'   : ([1133, 1132], { 'acmp2l': 1, 'acmp3l': 2 }),
    'pd_sel'  : ([1140], { 'register': 0, 'matrix': 1 }),
    'pd_ctrl' : ([1139], enable_v),
  },

  'vref': {
    'pd' : (m(60), matrix),
  },

  'edet_filter': {
    'input'    : (m(55), matrix),
    'op_mode'  : ([1243], { 'filter': 0, 'edge': 1 }),
    'edge_mode': ([1246, 1245], { 'rising': 0, 'falling': 1, 'both': 2, 'both_delay': 3 }),
    'out_pol'  : ([1244], { 'normal': 0, 'inverted': 1 }),
  },

  'prog_dly_edet': {
    'input'    : (m(56), matrix),
    'mode'     : ([1260, 1259], { 'rising': 0, 'falling': 1, 'both': 2, 'both_delay': 3 }),
    'value'    : ([1262, 1261], { '125ns': 0, '250ns': 1, '375ns': 2, '500ns': 3 }),
  },

  'lut2_0': {
    'in0'    : (m(0), matrix),
    'in1'    : (m(1), matrix),
    'lut'    : (r(1155, 1152), lut2_fn),
    '#check' : ([1232], 0),
  },

  'dff_0': {
    'clk'    : (m(0), matrix),
    'd'      : (m(1), matrix),
    'mode'   : ([1155], dff_mode),
    'output' : ([1154], dff_output),
    'init'   : ([1153], dff_init),
    '#check' : ([1232], 1),
  },

  'lut2_1': {
    'in0'    : (m(4), matrix),
    'in1'    : (m(5), matrix),
    'lut'    : (r(1159, 1156), lut2_fn),
    '#check' : ([1233], 0),
  },

  'dff_1': {
    'clk'    : (m(4), matrix),
    'd'      : (m(5), matrix),
    'mode'   : ([1159], dff_mode),
    'output' : ([1158], dff_output),
    'init'   : ([1157], dff_init),
    '#check' : ([1233], 1),
  },

  'lut2_2': {
    'in0'    : (m(6), matrix),
    'in1'    : (m(7), matrix),
    'lut'    : (r(1163, 1160), lut2_fn),
    '#check' : ([1234], 0),
  },

  'dff_2': {
    'clk'    : (m(6), matrix),
    'd'      : (m(7), matrix),
    'mode'   : ([1163], dff_mode),
    'output' : ([1162], dff_output),
    'init'   : ([1161], dff_init),
    '#check' : ([1234], 1),
  },

  'lut2_3': {
    'in0'    : (m(2), matrix),
    'in1'    : (m(3), matrix),
    'lut'    : (r(1167, 1164), lut2_fn),
    '#check' : ([1235], 0),
  },

  'pgen': {
    'clk'    : (m(2), matrix),
    'nrst'   : (m(3), matrix),
    'data'   : (r(1183, 1168), {}),
    '#check' : ([1235], 1),
  },

  'lut3_0': {
    'in0'    : (m(8), matrix),
    'in1'    : (m(9), matrix),
    'in2'    : (m(10), matrix),
    'lut'    : (r(1191, 1184), lut3_fn),
    '#check' : ([1236], 0),
  },

  'dff_3': {
    'clk'    : (m(8), matrix),
    'd'      : (m(9), matrix),
    'nrst'   : (m(10), matrix, [1189], 0),
    'nset'   : (m(10), matrix, [1189], 1),
    'mode'   : ([1191], dff_mode),
    'output' : ([1190], dff_output),
    'init'   : ([1188], dff_init),
    'qmode'  : ([1237], { 'first': 0, 'second': 1 }),
    '#check' : ([1236], 1),
  },

  'lut3_1': {
    'in0'    : (m(11), matrix),
    'in1'    : (m(12), matrix),
    'in2'    : (m(13), matrix),
    'lut'    : (r(1199, 1192), lut3_fn),
    '#check' : ([1238], 0),
  },

  'dff_4': {
    'clk'    : (m(11), matrix),
    'd'      : (m(12), matrix),
    'nrst'   : (m(13), matrix, [1197], 0),
    'nset'   : (m(13), matrix, [1197], 1),
    'mode'   : ([1199], dff_mode),
    'output' : ([1198], dff_output),
    'init'   : ([1196], dff_init),
    '#check' : ([1238], 1),
  },

  'lut3_2': {
    'in0'    : (m(14), matrix),
    'in1'    : (m(15), matrix),
    'in2'    : (m(16), matrix),
    'lut'    : (r(1207, 1200), lut3_fn),
    '#check' : ([1239], 0),
  },

  'dff_5': {
    'clk'    : (m(14), matrix),
    'd'      : (m(15), matrix),
    'nrst'   : (m(16), matrix, [1205], 0),
    'nset'   : (m(16), matrix, [1205], 1),
    'mode'   : ([1207], dff_mode),
    'output' : ([1206], dff_output),
    'init'   : ([1204], dff_init),
    '#check' : ([1239], 1),
  },

  'lut3_3': {
    'in0'    : (m(17), matrix),
    'in1'    : (m(18), matrix),
    'in2'    : (m(19), matrix),
    'lut'    : (r(1215, 1208), lut3_fn),
    '#check' : ([1240], 0),
  },

  'dff_6': {
    'clk'    : (m(17), matrix),
    'd'      : (m(18), matrix),
    'nrst'   : (m(19), matrix, [1213], 0),
    'nset'   : (m(19), matrix, [1213], 1),
    'mode'   : ([1215], dff_mode),
    'output' : ([1214], dff_output),
    'init'   : ([1212], dff_init),
    '#check' : ([1240], 1),
  },

  'lut3_4': {
    'in0'    : (m(20), matrix),
    'in1'    : (m(21), matrix),
    'in2'    : (m(22), matrix),
    'lut'    : (r(1223, 1216), lut3_fn),
    '#check' : ([1241], 0),
  },

  'dff_7': {
    'clk'    : (m(20), matrix),
    'd'      : (m(21), matrix),
    'nrst'   : (m(22), matrix, [1221], 0),
    'nset'   : (m(22), matrix, [1221], 1),
    'mode'   : ([1223], dff_mode),
    'output' : ([1222], dff_output),
    'init'   : ([1220], dff_init),
    '#check' : ([1241], 1),
  },

  'lut3_5': {
    'in0'    : (m(23), matrix),
    'in1'    : (m(24), matrix),
    'in2'    : (m(25), matrix),
    'lut'    : (r(1231, 1224), lut3_fn),
    '#check' : ([1242], 0),
  },

  'dff_8': {
    'clk'    : (m(23), matrix),
    'd'      : (m(24), matrix),
    'nrst'   : (m(25), matrix, [1229], 0),
    'nset'   : (m(25), matrix, [1229], 1),
    'mode'   : ([1231], dff_mode),
    'output' : ([1230], dff_output),
    'init'   : ([1228], dff_init),
    '#check' : ([1242], 1),
  },

  'lut3_6': {
    'in0'    : (m(26), matrix),
    'in1'    : (m(27), matrix),
    'in2'    : (m(28), matrix),
    'lut'    : (r(1255, 1248), lut3_fn),
    '#check' : ([1258, 1257], 0),
  },

  'pipe_delay': {
    'in'       : (m(26), matrix),
    'nrst'     : (m(27), matrix),
    'clk'      : (m(28), matrix),
    's0'       : (r(1251, 1248), {}),
    's1'       : (r(1255, 1252), {}),
    'out1_pol' : ([1256], { 'non_inverted': 0, 'inverted': 1 }),
    '#check'   : ([1258, 1257], 1),
  },

  'ripple_counter': {
    'up'       : (m(26), matrix),
    'nset'     : (m(27), matrix),
    'clk'      : (m(28), matrix),
    'nset_value': (r(1250, 1248), {}),
    'end_value' : (r(1253, 1251), {}),
    'cycle'    : ([1254], { 'full': 0, 'ranged': 1 }),
    '#check'   : ([1258, 1257], 3),
  },

  '#mf_16b': { 'd': m(30), 'c': m(31), 'b': m(32), 'a': m(33), 'map': mf_16b_map, 'select': r(1286, 1280) },

  'lut4_0': {
    'in0'      : (None, None),
    'in1'      : (None, None),
    'in2'      : (None, None),
    'in3'      : (None, None),
    'lut'      : (r(1303, 1288), lut4_fn),
    '#check'   : ([1282], 0),
    '#block'   : '#mf_16b',
  },

  'dff_9': {
    'clk'      : (None, None),
    'd'        : (None, None),
    'nrst'     : (None, None),
    'nset'     : (None, None),
    'mode'     : ([1303], dff_mode),
    'output'   : ([1302], dff_output),
    'init'     : ([1301], dff_init),
    '#check'   : ([1282], 1),
    '#block'   : '#mf_16b',
  },

  'cnt_dly_0': {
    'dly_in'   : (None, None),
    'ext_clk'  : (None, None),
    'mode'     : (r(1305, 1304), { 'delay': 0, 'one_shot': 1, 'freq_detect': 2, 'counter': 3}),
    'edge_mode': (r(1307, 1306), { 'both': 0, 'falling': 1, 'rising': 2, 'high_level_reset': 3 }),
    'clk_src'  : (r(1311, 1308), cnt_clk_src_v),
    'data'     : (r(1335, 1320), {}),
    'init'     : (r(1314, 1313), cnt_init),
    'output'   : ([1312], cnt_output),
    'sync'     : ([1336], cnt_sync),
    'edet'     : ([1319], cnt_edet),
    '#block'   : '#mf_16b',
  },

  'fsm': {
    'ws_power_down_state'  : ([1315], { 'low': 0, 'high': 1 }),
    'ws_mode'  : ([1316], enable_v),
    'keep_sync': ([1317], cnt_sync),
    'up_sync'  : ([1318], cnt_sync),
    'set_rst'  : ([1287], { 'reset_to_0': 0, 'set_to_data': 1 }),
    '#block'   : '#mf_16b',
  },

  'i2c_expander': {
    'io0_data'  : ([1592], low_high_v),
    'io0_select': ([1593], { 'matrix': 0, 'register': 1 }),
    'io5_data'  : ([1594], low_high_v),
    'io5_select': ([1595], { 'matrix': 0, 'register': 1 }),
    'io6_data'  : ([1596], low_high_v),
    'io6_select': ([1597], { 'matrix': 0, 'register': 1 }),
    'io9_data'  : ([1598], low_high_v),
    'io9_select': ([1599], { 'matrix': 0, 'register': 1 }),
  },

  'i2c': {
    'addr'     : (r(1619, 1616), {}),
    'sa4_sel'  : ([1620], { 'register': 0, 'io2': 1 }),
    'sa5_sel'  : ([1621], { 'register': 0, 'io3': 1 }),
    'sa6_sel'  : ([1622], { 'register': 0, 'io4': 1 }),
    'sa7_sel'  : ([1623], { 'register': 0, 'io5': 1 }),
    'mode'     : ([769], { 'standard': 0, 'fast': 1 }),
    'latch'    : ([1602], disable_v),
  },

  'nvm': {
    'rpr_read' : (r(1793, 1792), { 'unprotected': 0, 'part': 1, 'full': 2 }),
    'rpr_write': (r(1795, 1794), { 'unprotected': 0, 'part': 1, 'full': 2 }),
    'npr'      : (r(1801, 1800), { 'unprotected': 0, 'read': 1, 'write/erase': 2, 'read/write/erase': 3 }),
    'wpr'      : (r(1809 , 1808), { '1/4': 0, '1/2': 1, '3/4': 2, 'full': 3 }),
    'wpre'     : ([1810], enable_v),
    'prl'      : ([1824], { 'unlocked': 0, 'locked': 1 }),
    'pattern'  : (r(1631, 1624), {}),
  }
}

mf_8b_map = [
  # LUT
  ( 0x00, { 'in2': 'a', 'in1': 'b', 'in0': 'c' }), # 00000
  # DFF
  ( 0x04, { 'd': 'a', 'nset': 'b', 'nrst': 'b', 'clk': 'c' }), # 00100
  # CNT/DLY
  ( 0x01, { 'dly_in': 'a', 'ext_clk': 'b' }), # 00001
  # CNT/DLY -> LUT
  ( 0x02, { 'in2': 'dly_out', 'in1': 'b', 'in0': 'c', 'dly_in': 'a' }), # 00010
  ( 0x0a, { 'in2': 'a', 'in1': 'dly_out', 'in0': 'c', 'dly_in': 'b' }), # 01010
  ( 0x12, { 'in2': 'a', 'in1': 'b', 'in0': 'dly_out', 'dly_in': 'c' }), # 10010
  # CNT/DLY -> DFF
  ( 0x06, { 'd': 'dly_out', 'nset': 'b', 'nrst': 'b', 'clk': 'c', 'dly_in': 'a' }), # 00110
  ( 0x0e, { 'd': 'a', 'nset': 'dly_out', 'nrst': 'dly_out', 'clk': 'c', 'dly_in': 'b' }), # 01110
  ( 0x16, { 'd': 'a', 'nset': 'b', 'nrst': 'b', 'clk': 'dly_out', 'dly_in': 'c' }), # 10110
  # LUT -> CNT/DLY
  ( 0x03, { 'in2': 'a', 'in1': 'b', 'in0': 'c', 'dly_in': 'lut_out' }), # 00011
  # DFF -> CNT/DLY
  ( 0x07, { 'd': 'a', 'nset': 'b', 'nrst': 'b', 'clk': 'c', 'dly_in': 'dff_out' }), # 00111
]

def mf_8b(names, block, lut_dff, lut, fn_edge, clk_src, cnt_data, init, output, sync, edet):
  return {
    names[0]: block,

    names[1]: { # LUT
      'in0'    : (None, None),
      'in1'    : (None, None),
      'in2'    : (None, None),
      'lut'    : (lut, lut3_fn),
      '#check' : ([lut_dff], 0),
      '#block' : names[0],
    },

    names[2]: { # DFF
      'clk'    : (None, None),
      'd'      : (None, None),
      'nrst'   : (None, None, [lut[5]], 0),
      'nset'   : (None, None, [lut[5]], 1),
      'mode'   : ([lut[7]], dff_mode),
      'output' : ([lut[6]], dff_output),
      'init'   : ([lut[4]], dff_init),
      '#check' : ([lut_dff], 1),
      '#block' : names[0],
    },

    names[3]: { # CNT/DLY
      'dly_in' : (None, None),
      'ext_clk': (None, None),
      'fn_edge': (fn_edge, cnt_fn_edge_v),
      'clk_src': (clk_src, cnt_clk_src_v),
      'data'   : (cnt_data, {}),
      'init'   : (init, cnt_init),
      'output' : (output, cnt_output),
      'sync'   : (sync, cnt_sync),
      'edet'   : (edet, cnt_edet),
      '#block' : names[0],
    },
  }

slg46826.update(mf_8b(
  names    = ['#mf_8b_1', 'lut3_7', 'dff_10', 'cnt_dly_1'],
  block    = { 'c': m(34), 'b': m(35), 'a': m(36), 'map': mf_8b_map, 'select': r(1341, 1337) },
  lut_dff  = 1339,
  lut      = r(1351, 1344),
  fn_edge  = r(1359, 1356),
  clk_src  = r(1355, 1352),
  cnt_data = r(1367, 1360),
  init     = r(1343, 1342),
  output   = [1368],
  sync     = [1370],
  edet     = [1371],
))

slg46826.update(mf_8b(
  names    = ['#mf_8b_2', 'lut3_8', 'dff_11', 'cnt_dly_2'],
  block    = { 'c': m(37), 'b': m(38), 'a': m(39), 'map': mf_8b_map, 'select': [1375, 1374, 1394, 1373, 1372] },
  lut_dff  = 1394,
  lut      = r(1383, 1376),
  fn_edge  = r(1391, 1388),
  clk_src  = r(1387, 1384),
  cnt_data = r(1407, 1400),
  init     = r(1393, 1392),
  output   = [1395],
  sync     = [1397],
  edet     = [1398],
))

slg46826.update(mf_8b(
  names    = ['#mf_8b_3', 'lut3_9', 'dff_12', 'cnt_dly_3'],
  block    = { 'c': m(40), 'b': m(41), 'a': m(42), 'map': mf_8b_map, 'select': r(1413, 1409) },
  lut_dff  = 1411,
  lut      = r(1423, 1416),
  fn_edge  = r(1431, 1428),
  clk_src  = r(1427, 1424),
  cnt_data = r(1439, 1432),
  init     = r(1415, 1414),
  output   = [1440],
  sync     = [1442],
  edet     = [1443],
))

slg46826.update(mf_8b(
  names    = ['#mf_8b_4', 'lut3_10', 'dff_13', 'cnt_dly_4'],
  block    = { 'c': m(43), 'b': m(44), 'a': m(45), 'map': mf_8b_map, 'select': [1447, 1446, 1466, 1445, 1444] },
  lut_dff  = 1466,
  lut      = r(1455, 1448),
  fn_edge  = r(1463, 1460),
  clk_src  = r(1459, 1456),
  cnt_data = r(1479, 1472),
  init     = r(1465, 1464),
  output   = [1467],
  sync     = [1469],
  edet     = [1470],
))

slg46826.update(mf_8b(
  names    = ['#mf_8b_5', 'lut3_11', 'dff_14', 'cnt_dly_5'],
  block    = { 'c': m(46), 'b': m(47), 'a': m(48), 'map': mf_8b_map, 'select': r(1485, 1481) },
  lut_dff  = 1483,
  lut      = r(1495, 1488),
  fn_edge  = r(1503, 1500),
  clk_src  = r(1499, 1496),
  cnt_data = r(1511, 1504),
  init     = r(1487, 1486),
  output   = [1512],
  sync     = [1514],
  edet     = [1515],
))

slg46826.update(mf_8b(
  names    = ['#mf_8b_6', 'lut3_12', 'dff_15', 'cnt_dly_6'],
  block    = { 'c': m(49), 'b': m(50), 'a': m(51), 'map': mf_8b_map, 'select': [ 1519, 1518, 1538, 1517, 1516] },
  lut_dff  = 1538,
  lut      = r(1527, 1520),
  fn_edge  = r(1535, 1532),
  clk_src  = r(1531, 1528),
  cnt_data = r(1551, 1544),
  init     = r(1537, 1536),
  output   = [1539],
  sync     = [1541],
  edet     = [1542],
))

slg46826.update(mf_8b(
  names    = ['#mf_8b_7', 'lut3_13', 'dff_16', 'cnt_dly_7'],
  block    = { 'c': m(52), 'b': m(53), 'a': m(54), 'map': mf_8b_map, 'select': r(1556, 1552) },
  lut_dff  = 1556,
  lut      = r(1567, 1560),
  fn_edge  = r(1575, 1572),
  clk_src  = r(1571, 1568),
  cnt_data = r(1591, 1584),
  init     = r(1577, 1576),
  output   = [1557],
  sync     = [1559],
  edet     = [1578],
))

config_bits = {}

def update_bits(bits, value):
  global config_bits
  for i, b in enumerate(bits):
    v = (value >> (len(bits)-i-1)) & 1
    if b in config_bits:
      assert config_bits[b] == v, 'conflicting values for bit %d' % b
    config_bits[b] = v

def generate(config):
  global config_bits
  cfg = {}
  config_bits = {}
  lines = config.split('\n')
  for ln, line in enumerate(lines):
    line = line.split('#')
    line = line[0].strip()

    if line == '':
      continue

    line = line.split('=')
    assert len(line) == 2, '%d: not an assignment line' % ln

    param = line[0].split('.')
    assert len(param) == 2, '%d: not a valid LHS' % ln

    block = param[0].strip()
    reg   = param[1].strip()
    value = line[1].strip()

    assert block in slg46826, '%d: unknown block: %s' % (ln, block)
    assert reg in slg46826[block], '%d: unknown register: %s' % (ln, reg)

    if block not in cfg:
      cfg[block] = {}

    assert reg not in cfg[block], 'register "%s.%s" already defined' % (block, reg)

    cfg[block][reg] = value

  mapped = {}

  for block, regs in cfg.items():
    db = slg46826[block]

    for r, v in regs.items():
      try:
        vv = int(v, 0)
      except ValueError:
        vv = None

      if len(db[r]) == 2:
        bits, values = db[r]
        check_bits, check_value = [], 0
      elif len(db[r]) == 4:
        bits, values, check_bits, check_value = db[r]
      else:
        assert False

      if bits is None:
        if db['#block'] not in mapped:
          mapped[db['#block']] = []
        mapped[db['#block']] += [(r, v)]
        update_bits(check_bits, check_value)
        continue

      if v in values:
        vv = values[v]

      assert vv is not None, '"%s" is not a valid value for "%s"' % (v, r)

      if isinstance(vv, tuple):
        vv, set_bits, set_value = vv
      else:
        set_bits, set_value = [], 0

      update_bits(bits, vv)
      update_bits(set_bits, set_value)
      update_bits(check_bits, check_value)

      if '#check' in db:
        update_bits(db['#check'][0], db['#check'][1])

  for block, values in mapped.items():
    db = slg46826[block]['map']

    for sel_value, sel_set in db:
      for inp, val in values:
        if inp in sel_set and ((sel_set[inp] in ['a', 'b', 'c', 'd'] and val in matrix) or (sel_set[inp] == val)):
          match_set = sel_set
        else:
          match_set = None
          break

      if not match_set:
        continue

      for inp, val in values:
        if val in matrix:
          port = match_set[inp]
          port_bits = slg46826[block][port]

          vv = matrix[val]

          if isinstance(vv, tuple):
            vv, set_bits, set_value = vv
          else:
            set_bits, set_value = [], 0

          update_bits(port_bits, vv)
          update_bits(set_bits, set_value)

      update_bits(slg46826[block]['select'], sel_value)
      break
    else:
      assert False, 'no valid configuration found for "%s"' % block

  # print(config_bits)

  code = [0] * 256
  for index in config_bits:
    code[index // 8] |= (config_bits[index] << (index % 8))

  return code


