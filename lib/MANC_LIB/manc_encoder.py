import matplotlib.pyplot as plt

def ascii_to_bin(text):
    return ''.join(format(ord(c), '08b') for c in text)

def enkoder_manchester(text):
    binary = ascii_to_bin(text)
    signal = []
    for bit in binary:
        signal.extend([0, 1] if bit == '1' else [1, 0])
    return signal, binary

def sinyal_digital(binary_str, high=1, low=0, bit_width=1):
    signal = [high if bit == '1' else low for bit in binary_str]
    time, voltage = [], []
    for i, level in enumerate(signal):
        t_start, t_end = i * bit_width, (i + 1) * bit_width
        time.extend([t_start, t_end])
        voltage.extend([level, level])
    return time, voltage

def plot_encoder(input_text):
    signal_manchester, binary_input = enkoder_manchester(input_text)
    bit_width = 2
    total_bits = len(binary_input)

    time_input, volt_input = sinyal_digital(binary_input, bit_width=bit_width)

    time_manchester, volt_manchester = [], []
    for i, level in enumerate(signal_manchester):
        time_manchester.extend([i, i + 1])
        volt_manchester.extend([level, level])

    fig, axs = plt.subplots(2, 1, figsize=(16, 6), sharex=True)
    fig.suptitle("Manchester IEEE - Enkoder", fontsize=14)

    # Input
    axs[0].plot(time_input, volt_input, drawstyle='steps-post', color='green', linewidth=2)
    axs[0].set_title(f"Input Sinyal Biner:\"{input_text}\"", fontweight='bold')
    axs[0].set_ylim(-0.5, 1.5)
    axs[0].set_yticks([0, 1])
    axs[0].grid(True, axis='y')
    for i in range(total_bits + 1):
        axs[0].axvline(x=i * bit_width, linestyle='--', color='gray', linewidth=0.5)
    for i in range(total_bits):
        axs[0].text(i * bit_width + bit_width/2, 1.1, binary_input[i], ha='center', fontsize=9, fontweight='bold')

    # Manchester
    axs[1].plot(time_manchester, volt_manchester, drawstyle='steps-post', color='blue', linewidth=2)
    axs[1].set_title(f"Hasil Enkoder Manchester: \"{'-'.join(map(str, signal_manchester))}\"", fontweight='bold')
    axs[1].set_ylim(-0.5, 1.5)
    axs[1].set_yticks([0, 1])
    axs[1].grid(True, axis='y')
    for i in range(total_bits + 1):
        axs[1].axvline(x=i * 2, linestyle='--', color='gray', linewidth=0.5)
    for i in range(total_bits):
        axs[1].text(i * 2 + 1, 1.1, binary_input[i], ha='center', fontsize=9, fontweight='bold')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
