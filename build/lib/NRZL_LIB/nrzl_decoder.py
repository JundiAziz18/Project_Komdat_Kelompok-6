import matplotlib.pyplot as plt

def bin_to_ascii_nrzl(binary_string):
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    return ''.join(chr(int(b, 2)) for b in chars)

def nrzl_dekoder(signal):
    binary = ''.join('1' if level == 0 else '0' for level in signal)
    return bin_to_ascii_nrzl(binary), binary

def sinyal_digital(binary_str, high=1, low=0):
    signal = [high if bit == '1' else low for bit in binary_str]
    time, voltage = [], []
    for i, level in enumerate(signal):
        time.extend([i, i + 1])
        voltage.extend([level, level])
    return time, voltage

def plot_decoder_nrzl(nrzl_signal):
    decoded_text, biner_dekoder = nrzl_dekoder(nrzl_signal)

    time_nrzl, volt_nrzl = [], []
    for i, level in enumerate(nrzl_signal):
        time_nrzl.extend([i, i + 1])
        volt_nrzl.extend([level, level])

    time_out, volt_out = sinyal_digital(biner_dekoder, high=1, low=0)

    fig, axs = plt.subplots(2, 2, figsize=(14, 6), sharex=True)
    fig.suptitle("NRZ-L Decoder", fontsize=14, fontweight='bold')

    axs[0].plot(time_nrzl, volt_nrzl, drawstyle='steps-post', color='blue', linewidth=2)
    axs[0].set_title(f"Sinyal NRZ-L Masuk: \"{'-'.join(map(str, nrzl_signal))}\"", fontweight='bold')
    axs[0].set_ylim(-0.5, 1.5)
    axs[0].set_yticks([0, 1])
    axs[0].grid(True)
    for i in range(len(nrzl_signal) + 1):
        axs[0].axvline(i, color='gray', linestyle='--', linewidth=0.5)
    for i, bit in enumerate(biner_dekoder):
        axs[0].text(i + 0.5, 1.2, bit, ha='center', fontsize=9, fontweight='bold')

    axs[1].plot(time_out, volt_out, drawstyle='steps-post', color='orange', linewidth=2)
    axs[1].set_title(f"Hasil Dekoder: \"{decoded_text}\"", fontweight='bold')
    axs[1].set_ylim(-0.5, 1.5)
    axs[1].set_yticks([0, 1])
    axs[1].grid(True)
    for i in range(len(biner_dekoder) + 1):
        axs[1].axvline(i, color='gray', linestyle='--', linewidth=0.5)
    for i, bit in enumerate(biner_dekoder):
        axs[1].text(i + 0.5, 1.1, bit, ha='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.show()

