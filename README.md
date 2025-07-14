# Cable Tester
This is a [Circuit Python](https://circuitpython.org/) project tageting the following boards:
Adafruit Grand Central M4 Express
Adafruit Metro M4 Express

## Function
This code generates a test signal using the on board DAC of the of the target boards
This signal is switched though a series of MUXs/DeMUXs [1:16 Mux Dev Board](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/dg120xevkit.html)
This signal is then read back using the on board ADC of the of the target boards

