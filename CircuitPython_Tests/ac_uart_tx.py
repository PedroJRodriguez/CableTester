import board
import busio
import time

#Hardware UART-Capable pin for grand central m4
#board.D16 is board.TX2 ; board.D17 is board.RX2
uart = busio.UART(board.TX2, board.RX2, baudrate=115200, timeout=0.01)

while True:
    uart.write(b"Hello over AC-coupled UART!\r\n")
    time.sleep(0.25)