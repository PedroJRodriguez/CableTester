import board
import mux
import cable_test
import sd_card

if board.board_id == "metro_m4_express":
    import metro_m4_pinmapping as pin
else:
    import grand_m4_pinmapping as pin

sd_card.mount_filesystem()
cable_asm_dict = sd_card.load_dict("cable.json")

mux.en_off()

while True:
    print("****************************************************")
    print("************ ALSU Controls Cable Tester ************")
    print("****************************************************")
    print("1) Scan & Print Current Connections")
    print("2) Store new Cable Assembly")
    print("3) Check Cable Assembly", end="\n\n")
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

        conn_found = cable_test.scan

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
            conn_found = cable_test.scan

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

    elif user_input == "cal_board":  #Hidden function call
        cable_test.cal_board()
    
    elif user_input == "":  #Handles case of pressing enter after loading terminal
        print("")
    
    else:
        print("Not a valid input")
