# Smart-LED-Dimmer-using-PWM
# Smart LED Dimmer using PWM
# PWM = switching LED ON/OFF very fast.
# Duty cycle % = how long it stays ON in each cycle.

duty = int(input("Enter brightness (0-100%): "))

if duty == 0:
    print("LED is OFF")
elif duty >= 100:
    print("LED is FULL brightness")
else:
    print(f"LED glowing at {duty}% brightness (PWM duty cycle = {duty}%)")
