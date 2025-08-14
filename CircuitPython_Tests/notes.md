# Cable Tester CircuitPython Notes

## Ways to Output Sine Wave
### Audio Functions
 [Link to audio core module doc page](https://docs.circuitpython.org/en/latest/shared-bindings/audiocore/)

[Link to audioio module doc page](https://docs.circuitpython.org/en/latest/shared-bindings/audioio/)

[Link to audio mixer module doc page](https://docs.circuitpython.org/en/latest/shared-bindings/audiomixer/)

## Sine Wave Input Options

### ADC timed input
Could poll ADC value and count|time zero crossings or some threshold  
### frequencyio
 [Link to module doc page](https://docs.circuitpython.org/en/latest/shared-bindings/frequencyio/)

 [Link to github page](https://github.com/adafruit/circuitpython/tree/main/shared-bindings/frequencyio)

 [Link to github page for Atmel](https://github.com/adafruit/circuitpython/blob/main/ports/atmel-samd/common-hal/frequencyio/FrequencyIn.c#L449)

This worked well with square wae input, within 10% accuracy between 2kHz and ~5MHz detection.

