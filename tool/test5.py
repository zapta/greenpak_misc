import greenpak as gp

print("Connecting.")
driver = gp.GreenpakDriver(port="COM17", device="SLG46826", control_code=0b0001)

print("Loading configuration.")
data = gp.read_bits_file("test_data/blinky_nvm_slow.txt")
gp.hex_dump(data)

print("Programming NVM.")
driver.program_nvm_pages(0, data)

print ("Reading NVM.")
data = driver.read_nvm_bytes(0, 256)
gp.hex_dump(data)

print("Reseting the device.")
driver.reset_device()
