import board, busio

uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=0.01)

buf = bytearray(64)
while True:
    n = uart.readinto(buf)
    if n:
        print(bytes(memoryview(buf)[:n]).decode(errors="ignore"), end="")
