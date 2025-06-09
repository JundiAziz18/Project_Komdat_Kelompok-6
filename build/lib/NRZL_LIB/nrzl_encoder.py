import matplotlib.pyplot as plt

def ascii_to_bin_nrzl(text):
    return ''.join(format(ord(char), '08b') for char in text)

def nrzl_enkoder(text):
    binary = ascii_to_bin_nrzl(text)
    signal = [0 if bit == '1' else 1 for bit in binary]
    return signal, binary

def sinyal_digital(binary_str, high=1, low=0):
    signal = [high if bit == '1' else low for bit in binary_str]
    time, voltage = [], []
    for i, level in enumerate(signal):
        time.extend([i, i + 1])
        voltage.extend([level, level])
    return time, voltage

def plot_encoder_nrzl(input_text):
    nrzl_signal, input_biner = nrzl_enkoder(input_text)
    time_in, volt_in = sinyal_digital(input_biner, high=1, low=0)

    time_nrzl, volt_nrzl = [], []
    for i, level in enumerate(nrzl_signal):
        time_nrzl.extend([i, i + 1])
        volt_nrzl.extend([level, level])

    fig, axs = plt.subplots(2, 1, figsize=(14, 6), sharex=True)
    fig.suptitle("NRZ-L Encoder", fontsize=14, fontweight='bold')

    axs[0].plot(time_in, volt_in, drawstyle='steps-post', color='green', linewidth=2)
    axs[0].set_title(f"Input Sinyal Biner:\"{input_text}\"", fontweight='bold')
    axs[0].set_ylim(-0.5, 1.5)
    axs[0].set_yticks([0, 1])
    axs[0].grid(True)
    for i in range(len(input_biner) + 1):
        axs[0].axvline(i, color='gray', linestyle='--', linewidth=0.5)
    for i, bit in enumerate(input_biner):
        axs[0].text(i + 0.5, 1.1, bit, ha='center', fontsize=9, fontweight='bold')

    axs[1].plot(time_nrzl, volt_nrzl, drawstyle='steps-post', color='blue', linewidth=2)
    axs[1].set_title(f"Output Enkoder NRZ-L: \"{'-'.join(map(str, nrzl_signal))}\"", fontweight='bold')
    axs[1].set_ylim(-0.5, 1.5)
    axs[1].set_yticks([0, 1])
    axs[1].grid(True)
    for i in range(len(input_biner) + 1):
        axs[1].axvline(i, color='gray', linestyle='--', linewidth=0.5)
    for i, bit in enumerate(input_biner):
        axs[1].text(i + 0.5, 1.2, bit, ha='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.show()

