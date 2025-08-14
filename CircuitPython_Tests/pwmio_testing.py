import board
import pwmio

# Set up PWM on pin D13 (you can change this to another pin)
pwm = pwmio.PWMOut(board.D13, frequency=440, duty_cycle=32768)  
# 32768 is about 50% of the max 65535

print("PWM Frequency Control")
print("Enter frequency in Hz (e.g., 1000) or 'q' to quit.")

while True:
    try:
        user_input = input("Frequency (Hz): ").strip()
        if user_input.lower() == 'q':
            print("Exiting...")
            break

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        freq = int(user_input)
        if freq <= 0:
            print("Frequency must be > 0.")
            continue

        pwm.frequency = freq
        print(f"Set frequency to {freq} Hz (50% duty cycle).")

    except Exception as e:
        print(f"Error: {e}")
