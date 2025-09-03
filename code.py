import board
import busio
import time
import mux
import cable_test
import sd_card

if board.board_id == "metro_m4_express":
    import metro_m4_pinmapping as pin
elif board.board_id == "grandcentral_m4_express":
    import grand_m4_pinmapping as pin
else:
    print("Board not supported")

sd_card.mount_filesystem()
cable_asm_dict = sd_card.load_dict("cable.json")

mux.en_off()

while True:
    print("****************************************************")
    print("************ ALSU Controls Cable Tester ************")
    print("****************************************************")
    print("1) Scan & Print Current Connections")
    print("2) Store new Cable Assembly")
    print("3) Check Cable Assembly")
    print("x1) Manually set RX Mux")
    print("x2) Manually set TX Mux")
    print("rx) Set board to RX test") 
    print("tx) Set board to TX test", end="\n\n" )

    print("Select Option >>> ", end="")

    user_input = input()  # type and press enter
    print("")

    if user_input == "1":
        print("Scanning Current Connections")
        cable_test.scan(diag_print=1)  # print diag print statements

    elif user_input == "2":
        print("Storing new Cable Assembly")
        print("Name of Cable Assembly >>> ", end="")
        user_input = input()  # type and press enter
        print("")

        conn_found = cable_test.scan()

        for item in conn_found:
            print(item)
        cable_asm_dict.update({user_input: conn_found})
        print("Save to SD? [y]/n >>> ", end="")
        user_input = input()  # type and press enter
        print("")
        if (input == "y"):
            sd_card.save_dict(cable_asm_dict, "cable.json")

    elif user_input == "3":
        print("Checking Cable Assembly")
        print("Name of Cable Assembly to check >>> ", end="")
        user_input = input()  # type and press enter
        print("")

        stored_cable_conn = cable_asm_dict.get(user_input)
        if stored_cable_conn is None:
            print(" !Cable Assembly Not Found", end="\n\n")
        else:
            conn_found = cable_test.scan()

            print("Tested Cable Assembly Connections")
            for item in conn_found:
                print(item)

            print("Stored Cable Assembly Connections")
            for item in stored_cable_conn:
                print(item)

            if sorted(conn_found) == sorted(stored_cable_conn):
                print("Cable Assembly Tests GOOD")
            else:
                print("Cable Assembly Test FAILURE")
    elif user_input == "x1":
        print("Setting RX Mux to (1-16) >>> ", end="")
        user_input = input()  # type and press enter
        print("")
        if (1<user_input<17):
            print("Setting RX Mux to %i", user_input)
            mux.dac_sel(user_input)
        else:
            print("User Input - Out of Range")
            
    elif user_input == "x2":
        print("Setting RX Mux to (1-16) >>> ", end="")
        user_input = input()  # type and press enter
        print("")
        if (1<user_input<17):
            print("Setting RX Mux to %i", user_input)
            mux.adc_sel(user_input)
        else:
            print("User Input - Out of Range")

    elif user_input == "rx":
        print("Starting in RX Test mode - will require restart to exit")
        # Pins for Metro M4 Board D2 is RX; D3 is TX
        # Pins for Grand Central M4 Board D17 is RX; D16 is TX
        uart = busio.UART(pin.tx, pin.rx, baudrate=115200, timeout=0.1)  # timeout in seconds
        buf = bytearray(64)
        while True:
            n = uart.readinto(buf)
            if n:
                print(bytes(memoryview(buf)[:n]).decode("utf-8"), end="")
    
    elif user_input == "tx":
        print("Starting in TX Test mode - will require restart to exit")
        # Pins for Metro M4 Board D2 is RX; D3 is TX
        # Pins for Grand Central M4 Board D17 is RX; D16 is TX
        uart = busio.UART(pin.tx, pin.rx, baudrate=115200, timeout=0.1)  # timeout in seconds
        while True:
            uart.write(b"Hello over AC-coupled UART!\r\n")
            time.sleep(0.25)
            
    elif user_input == "cal_board":  #Hidden function call
        cable_test.cal_board()
    
    elif user_input == "":  #Handles case of pressing enter after loading terminal
        print("")
    
    else:
        print("Not a valid input")
