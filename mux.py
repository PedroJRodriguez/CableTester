import board

if board.board_id == "metro_m4_express":
    import metro_m4_pinmapping as pin
else:
    import grand_m4_pinmapping as pin

def bit_conversion(sel):
    return [1 if digit == "1" else 0 for digit in bin(sel)[2:]]


def adc_sel(sel):
    mux_sel_array = [int(x) for x in "{0:04b}".format(sel)]
    pin.amux0.value = mux_sel_array[3]
    pin.amux1.value = mux_sel_array[2]
    pin.amux2.value = mux_sel_array[1]
    pin.amux3.value = mux_sel_array[0]
    # print("ADC MUX", sel, mux_sel_array)
    return 0


def dac_sel(sel):
    mux_sel_array = [int(x) for x in "{0:04b}".format(sel)]
    pin.dmux0.value = mux_sel_array[3]
    pin.dmux1.value = mux_sel_array[2]
    pin.dmux2.value = mux_sel_array[1]
    pin.dmux3.value = mux_sel_array[0]
    # print("DAC MUX", sel, mux_sel_array)
    return 0


def en_on():
    pin.amux_en.value = 1
    pin.dmux_en.value = 1
    return 0


def en_off():
    pin.amux_en.value = 0
    pin.dmux_en.value = 0
    return 0

def adc_en_on():
    pin.amux_en.value = 1
    return 0


def adc_en_off():
    pin.amux_en.value = 0
    return 0

def dac_en_on():
    pin.dmux_en.value = 1
    return 0


def dac_en_off():
    pin.dmux_en.value = 0
    return 0