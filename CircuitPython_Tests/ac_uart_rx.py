import board
import busio
import time

# Initialize UART on the specified pins 
# Pins for Metro M4 Board D2 is RX; D3 is TX
uart = busio.UART(board.D3, board.D2, baudrate=115200, timeout=0.1)  # timeout in seconds

buf = bytearray(64)
while True:
    n = uart.readinto(buf)
    if n:
        print(bytes(memoryview(buf)[:n]).decode("utf-8"), end="")
