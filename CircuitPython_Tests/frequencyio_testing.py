import board
import audiocore
import audioio
import array
import math
import time

# ====== CONFIGURATION ======
SAMPLE_RATE = 350_000  # Push this higher to test the limits
NUM_SAMPLES = 10       # Fewer samples = higher output frequency

# Output frequency = SAMPLE_RATE / NUM_SAMPLES
output_freq = SAMPLE_RATE / NUM_SAMPLES
print("Target output frequency: {:.1f} Hz".format(output_freq))

# ====== GENERATE SINE WAVE ======
# 16-bit unsigned values (0–65535), even though DAC is 12-bit
sine_wave = array.array("H", [0] * NUM_SAMPLES)
for i in range(NUM_SAMPLES):
    angle = 2 * math.pi * i / NUM_SAMPLES
    value = int((math.sin(angle) + 1.0) * 32767.5)
    sine_wave[i] = value

# Create RawSample with desired sample rate
sine_sample = audiocore.RawSample(sine_wave, sample_rate=SAMPLE_RATE)

# ====== OUTPUT SETUP ======
audio = audioio.AudioOut(board.A0)
audio.play(sine_sample, loop=True)

# Keep running
while True:
    pass
