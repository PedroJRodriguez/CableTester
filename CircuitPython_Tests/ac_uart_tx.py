import board, busio, time

# Pick a hardware UART-capable TX pin (example: TX on Serial1)
uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=0.01)

while True:
    uart.write(b"Hello over AC-coupled UART!\r\n")
    time.sleep(1)
