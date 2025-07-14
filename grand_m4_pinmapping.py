# ********************************
# Pin Mapping for Grand Central M4
# ********************************

import board
import digitalio
import analogio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

dac = analogio.AnalogOut(board.A0)  # output on pin A0
adc = analogio.AnalogIn(board.A5)  # input on pin A5

amux_en = digitalio.DigitalInOut(board.D31)
amux0 = digitalio.DigitalInOut(board.D33)
amux1 = digitalio.DigitalInOut(board.D35)
amux2 = digitalio.DigitalInOut(board.D37)
amux3 = digitalio.DigitalInOut(board.D39)

amux_en.direction = digitalio.Direction.OUTPUT
amux0.direction = digitalio.Direction.OUTPUT
amux1.direction = digitalio.Direction.OUTPUT
amux2.direction = digitalio.Direction.OUTPUT
amux3.direction = digitalio.Direction.OUTPUT

dmux_en = digitalio.DigitalInOut(board.D30)
dmux0 = digitalio.DigitalInOut(board.D32)
dmux1 = digitalio.DigitalInOut(board.D34)
dmux2 = digitalio.DigitalInOut(board.D36)
dmux3 = digitalio.DigitalInOut(board.D38)


dmux_en.direction = digitalio.Direction.OUTPUT
dmux0.direction = digitalio.Direction.OUTPUT
dmux1.direction = digitalio.Direction.OUTPUT
dmux2.direction = digitalio.Direction.OUTPUT
dmux3.direction = digitalio.Direction.OUTPUT

print('Grand Central M4 Loaded')
