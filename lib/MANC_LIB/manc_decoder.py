import matplotlib.pyplot as plt # menambahkan import matplotlib untuk plotting
# manc_decoder.py - Modul untuk dekoder sinyal Manchester
def bin_to_ascii(binary_str): # Mengonversi string biner ke karakter ASCII
    return ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)) # Mengonversi biner ke ASCII

def dekoder_manchester(signal): # Fungsi untuk mendekode sinyal Manchester
    binary = '' # Inisialisasi string biner kosong
    for i in range(0, len(signal), 2): # Iterasi setiap dua bit dalam sinyal
        pair = signal[i:i+2] # Mengambil pasangan bit
        if pair == [0, 1]: # Jika pasangan adalah 0,1
            binary += '1' # Tambahkan '1' ke string biner
        elif pair == [1, 0]:
            binary += '0'
        else:
            raise ValueError(f"Invalid Manchester signal at position {i}: {pair}")
    return bin_to_ascii(binary), binary

def sinyal_digital(binary_str, high=1, low=0, bit_width=1):
    signal = [high if bit == '1' else low for bit in binary_str]
    time, voltage = [], []
    for i, level in enumerate(signal):
        t_start, t_end = i * bit_width, (i + 1) * bit_width
        time.extend([t_start, t_end])
        voltage.extend([level, level])
    return time, voltage

def plot_decoder(signal_manchester):
    decoded_text, binary_output = dekoder_manchester(signal_manchester)
    total_bits = len(binary_output)
    bit_width = 2

    time_manchester, volt_manchester = [], []
    for i, level in enumerate(signal_manchester):
        time_manchester.extend([i, i + 1])
        volt_manchester.extend([level, level])

    time_output, volt_output = sinyal_digital(binary_output, bit_width=bit_width)

    fig, axs = plt.subplots(2, 1, figsize=(16, 6), sharex=True)
    fig.suptitle("Manchester IEEE - Dekoder", fontsize=14)
    # Manchester input
    axs[0].plot(time_manchester, volt_manchester, drawstyle='steps-post', color='blue', linewidth=2)
    axs[0].set_title(f"Sinyal Manchester:\"{'-'.join(map(str, signal_manchester))}\"", fontweight='bold')
    axs[0].set_ylim(-0.5, 1.5)
    axs[0].set_yticks([0, 1])
    axs[0].grid(True, axis='y')
    for i in range(total_bits + 1):
        axs[0].axvline(x=i * 2, linestyle='--', color='gray', linewidth=0.5)
    for i in range(total_bits):
        axs[0].text(i * 2 + 1, 1.1, binary_output[i], ha='center', fontsize=9, fontweight='bold')
    # Decoded binary output
    axs[1].plot(time_output, volt_output, drawstyle='steps-post', color='orange', linewidth=2)
    axs[1].set_title(f"Hasil Dekoder: \"{decoded_text}\"", fontweight='bold')
    axs[1].set_ylim(-0.5, 1.5)
    axs[1].set_yticks([0, 1])
    axs[1].grid(True, axis='y')
    for i in range(total_bits + 1):
        axs[1].axvline(x=i * bit_width, linestyle='--', color='gray', linewidth=0.5)
    for i in range(total_bits):
        axs[1].text(i * bit_width + bit_width/2, 1.1, binary_output[i], ha='center', fontsize=9, fontweight='bold')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

