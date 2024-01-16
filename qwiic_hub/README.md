#SMD to DIP Adapters for GreenPAK SPLDs.

These PCBs designs be ordered from PCB houses such as JLCPCB and are useful for prototyping with GreenPAK devices using solderless or other breadboards. They can be programmed or accessed via a QWIIC (I2C)  connector using boards such as Raspberry PI Pico which are supported
by the [greenpak](https://pypi.org/project/greenpak/) Python package. The recomanded PCB thickness is 0.8mm or 1.0mm for easy breakaway though standard 1.6mm thickness should be just fine.


Item | Value | Comments
---|---|---
R1 | 2K - 5K | SCL pullup resistor.
R2 | 2K - 5K | SDA pullup resistor.
C1 | 0.1uf | VDD bypass capacitor.
C2 | 0.1uf | VDD2 bypass capacitor.
J1 | JST SH 1.0mm right angle SMD | QWIIC and STEMMA QT compatible connector.

R1, R2, C1, C2, can be of 0402, 0603, or 0805 footptints.


## Front side
<img  src="https://raw.githubusercontent.com/zapta/greenpak_misc/main/smd_adapters/smd_adapters.png"
      style="display: block;margin-left: auto;margin-right: auto;width: 80%;" />

## Back side
<img  src="https://raw.githubusercontent.com/zapta/greenpak_misc/main/smd_adapters/smd_adapters_rear.png"
      style="display: block;margin-left: auto;margin-right: auto;width: 80%;" />
