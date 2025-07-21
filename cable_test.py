import board
import time
import mux

if board.board_id == "metro_m4_express":
    import metro_m4_pinmapping as pin
else:
    import grand_m4_pinmapping as pin

NUM_PINS = 16

DAC_DELAY = 0.01
ADC_DELAY = 0.01

count_increment = int(65536 / NUM_PINS)
dband = int(count_increment)

def dac_volt_output(volts):
    return int(volts / 3.3 * 65535)


def adc_read_pin_volt(pin):
    return (pin.value * 3.3) / 65536


def scan(diag_print = 0):
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

def cal_board(steps = 64, num_samples = 1000, mux_delay = 0.01, sample_delay=0.001):
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
