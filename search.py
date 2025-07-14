import board
import time
import mux

if board.board_id == "metro_m4_express":
    import metro_m4_pinmapping as pin
else:
    import grand_m4_pinmapping as pin


def dac_volt_output(volts):
    return int(volts / 3.3 * 65535)


def adc_read_pin_volt(pin):
    return (pin.value * 3.3) / 65536


NUM_PINS = 16

CABLE_ASM_AMUX = [8, 9, 10, 11, 12, 13, 14, 15]
CABLE_ASM_DMUX = [0, 1, 2, 3, 4, 5, 6, 7]

DAC_DELAY = 0.1
ADC_DELAY = 0.1

count_increment = int(65536 / NUM_PINS)
deadband = int(count_increment/1.2)

while True:
    conn_found = []
    mux.en_off()
    for x in range(0, NUM_PINS):
        #counts = x * count_increment
        counts = 32768
        pin.dac.value = counts
        mux.dac_sel(x)
        time.sleep(DAC_DELAY)

        for y in range(0, NUM_PINS):
            mux.adc_sel(y)
            mux.en_on()
            time.sleep(ADC_DELAY)
            if (counts - deadband) < pin.adc.value < (counts + deadband):
                conn_found.append((x, y, counts, pin.adc.value))
                if counts!= 0:
                    print(x, y, counts, pin.adc.value, (pin.adc.value/counts))
            # mux.en_off()
    for item in conn_found:
        print(item)
