import board
import time
import mux

if board.board_id == "metro_m4_express":
    import metro_m4_pinmapping as pin
else:
    import grand_m4_pinmapping as pin

def conn_sweep(diag_print):
    conn_found = []
    print_header = 0
    mux.en_on()
    for x in range(0, NUM_PINS):
        # counts = x * count_increment
        counts = 32768
        cal = (-2626)
        pin.dac.value = counts
        mux.dac_sel(x)
        time.sleep(DAC_DELAY)

        for y in range(0, NUM_PINS):
            mux.adc_sel(y)
            time.sleep(ADC_DELAY)
            if ((counts + cal) - dband) < pin.adc.value < ((counts + cal) + dband):
                conn_found.append((x, y))
                if (diag_print == 1):
                    if (print_header == 0):
                        print("DAC.sel, ADC.sel, DAC.val, ADC.val")
                        print_header += 1
                    print(x, ',', y, ',', counts, ',', pin.adc.value)
    mux.en_off()
    return conn_found

def cal_board(mux_delay, sample_delay, num_samples, steps):
    print("Attach all pins straight-through")
    print("Press ENTER to Continue")
    input()
   
    counts_step = int(65536 / steps)
   
    for x in range(0, steps+1):
        counts = x * counts_step
        if (counts > 65535):  # clamp dac to upper bound
            counts = 65535
        pin.dac.value = counts
        counts_avg_list = []
        for y in range(0, (NUM_PINS)):
            adc_samples = []
            mux.dac_sel(y)
            mux.adc_sel(y)
            time.sleep(mux_delay)
            mux.en_on()
           
            for z in range(0, num_samples):
                time.sleep(sample_delay)
                adc_samples.append(pin.adc.value)
           
            average = sum(adc_samples) / len(adc_samples)
            mux.en_off()
            counts_avg_list.append(average)
       
        counts_avg_list.insert(0, counts)  # prepend the counts to the average list
        # counts_avg_list.append("END")      # append 'END' to simplify formatted printing
       
        # print (counts_avg_list)
        for item in counts_avg_list:
            if (item != "END"):
                print(item, end=', ')
        print(';')
    return 0

NUM_PINS = 16

DAC_DELAY = 0.01
ADC_DELAY = 0.01

count_increment = int(65536 / NUM_PINS)
dband = int(count_increment)

cable_asm_dict = {}

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
    print("")  # add a newline after input

    if user_input == "1":
        print("Scanning Current Connections")
        conn_sweep(1)  # print diag print statements

    elif user_input == "2":
        print("Storing new Cable Assembly")
        print("Name of Cable Assembly >>> ", end="")
        user_input = input()  # type and press enter
        print("")  # add a newline after input

        conn_found = conn_sweep(0)

        for item in conn_found:
            print(item)
        cable_asm_dict.update({user_input: conn_found})

    elif user_input == "3":
        print("Checking Cable Assembly")
        print("Name of Cable Assembly to check >>> ", end="")
        user_input = input()  # type and press enter
        print("")  # add a newline after input

        stored_cable_conn = cable_asm_dict.get(user_input)
        if stored_cable_conn is None:
            print(" !Cable Assembly Not Found", end="\n\n")
        else:
            conn_found = conn_sweep(0)

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
   
    elif user_input == "cal_board":
        cal_board(0.01, 0.001, 1000, 64)
    else:
        print("Not a valid input")
