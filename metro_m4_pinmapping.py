# *********************
# Pin Mapping Metro M4
# *********************

import board
import digitalio
import analogio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

dac = analogio.AnalogOut(board.A0)  # output on pin A0
adc = analogio.AnalogIn(board.A5)  # input on pin A5

rx = board.D2
tx = board.D3

amux_en = digitalio.DigitalInOut(board.D3)
amux0 = digitalio.DigitalInOut(board.D4)
amux1 = digitalio.DigitalInOut(board.D5)
amux2 = digitalio.DigitalInOut(board.D6)
amux3 = digitalio.DigitalInOut(board.D7)

amux_en.direction = digitalio.Direction.OUTPUT
amux0.direction = digitalio.Direction.OUTPUT
amux1.direction = digitalio.Direction.OUTPUT
amux2.direction = digitalio.Direction.OUTPUT
amux3.direction = digitalio.Direction.OUTPUT

dmux_en = digitalio.DigitalInOut(board.D8)
dmux0 = digitalio.DigitalInOut(board.D9)
dmux1 = digitalio.DigitalInOut(board.D10)
dmux2 = digitalio.DigitalInOut(board.D11)
dmux3 = digitalio.DigitalInOut(board.D12)


dmux_en.direction = digitalio.Direction.OUTPUT
dmux0.direction = digitalio.Direction.OUTPUT
dmux1.direction = digitalio.Direction.OUTPUT
dmux2.direction = digitalio.Direction.OUTPUT
dmux3.direction = digitalio.Direction.OUTPUT

print('Metro M4 Express Loaded')
