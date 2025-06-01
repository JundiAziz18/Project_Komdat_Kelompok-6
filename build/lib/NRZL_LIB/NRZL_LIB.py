import matplotlib.pyplot as plt  # Import library matplotlib untuk plotting grafik
from matplotlib.ticker import  MultipleLocator  # Import MaxNLocator untuk mengatur jumlah tick pada sumbu

# Fungsi untuk mengubah teks ASCII menjadi representasi biner 8-bit
def ascii_to_bin_nrzl(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Fungsi untuk mengubah representasi biner kembali menjadi teks ASCII
def bin_to_ascii_nrzl(binary_string):
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]  # Pisahkan setiap 8 bit
    return ''.join(chr(int(b, 2)) for b in chars)  # Konversi ke karakter ASCII

# Fungsi untuk mengubah teks ke sinyal NRZ-L dengan dua polaritas: 1 → -1, 0 → +1
def nrzl_enkoder(text):
    binary = ascii_to_bin_nrzl(text)  # Ubah teks ke biner
    signal = [-1 if bit == '1' else 1 for bit in binary]  # NRZ-L: 1 jadi -1V, 0 jadi +1V
    return signal, binary  # Kembalikan sinyal dan representasi binernya

# Fungsi untuk mendekode sinyal NRZ-L ke teks
def nrzl_dekoder(signal):
    binary = ''.join('1' if level == -1 else '0' for level in signal)  # NRZ-L: -1V jadi '1', +1V jadi '0'
    return bin_to_ascii_nrzl(binary), binary  # Kembalikan teks hasil decoding dan binernya

# Fungsi untuk menghasilkan sinyal digital dari string biner (default: 0V untuk 0, 1V untuk 1)
def sinyal_digital(binary_str, high=1, low=0):
    signal = [high if bit == '1' else low for bit in binary_str]  # Konversi biner ke tegangan
    time = []       # List waktu (untuk step plot)
    voltage = []    # List tegangan
    for i, level in enumerate(signal):  # Buat bentuk sinyal step
        time.extend([i, i + 1])         # Tambahkan waktu awal dan akhir setiap bit
        voltage.extend([level, level])  # Pertahankan level selama 1 bit time
    return time, voltage

# Fungsi utama untuk mem-visualisasikan seluruh proses NRZ-L
def plot_hasil_nrzl(input_text):
    nrzl_signal, input_biner = nrzl_enkoder(input_text)  # Encode input teks ke NRZ-L
    decoded_text, biner_dekoder = nrzl_dekoder(nrzl_signal)  # Decode sinyal NRZ-L kembali ke teks

    # Hasilkan sinyal digital input (0 → 0V, 1 → 1V)
    time_in, volt_in = sinyal_digital(input_biner, high=1, low=0)

    # Buat sinyal NRZ-L (-1V untuk bit 1, +1V untuk bit 0)
    time_nrzl = [] # Inisialisasi list untuk waktu dan tegangan NRZ-L
    volt_nrzl = [] # Inisialisasi list untuk waktu dan tegangan NRZ-L
    for i, level in enumerate(nrzl_signal): # Iterasi setiap level sinyal NRZ-L
        time_nrzl.extend([i, i + 1]) # Tambahkan waktu untuk setiap level
        volt_nrzl.extend([level, level]) # Tambahkan level tegangan untuk setiap level sinyal NRZ-L

    # Hasilkan sinyal digital hasil decoding
    time_out, volt_out = sinyal_digital(biner_dekoder, high=1, low=0)

    # Buat plot: 3 subplot (Input, NRZ-L, dan Output)
    fig, axs = plt.subplots(3, 1, figsize=(16, 10), sharex=True)  # 3 baris subplot, satu kolom
    fig.suptitle(f"$\\bf{{Enkoder\\ dan\\ Dekoder\\ NRZ-L}}$",fontsize=14, y=0.95)  # Judul utama plot
    # Tambahkan teks deskriptif di bawah judul utama
    fig.text(0.52, 0.90, f"Input\t\t: {input_text}", ha='center', fontsize=12) # Teks input yang akan dienkode
    fig.text(0.52, 0.87, f"Input Biner\t: {input_biner}", ha='center', fontsize=12) # Teks biner input
    fig.text(0.52, 0.84, f"Hasil Dekoder\t: {decoded_text}", ha='center', fontsize=12) # Teks yang didekode dari sinyal Manchester
    
    # Plot sinyal biner input
    axs[0].plot(time_in, volt_in, drawstyle='steps-post', linewidth=2, color='green') # Sinyal biner input
    axs[0].set_title("\nInput Sinyal Biner", fontweight='bold')  # Judul subplot
    axs[0].set_ylim(-0.5, 1.5)  # Skala Y
    axs[0].set_yticks([0, 1])   # Label Y
    axs[0].grid(True)          # Tampilkan grid
    for i in range(len(input_biner) + 1):
        axs[0].axvline(i, color='gray', linestyle='--', linewidth=0.5) # Garis vertikal untuk setiap bit
    for i, bit in enumerate(input_biner):  # Tampilkan nilai bit di atas sinyal
        axs[0].text(i + 0.5, 1.1, bit, ha='center', fontsize=9, fontweight='bold')
        

    # Plot sinyal hasil encoding NRZ-L
    axs[1].plot(time_nrzl, volt_nrzl, drawstyle='steps-post', linewidth=2, color='blue') # Sinyal NRZ-L
    axs[1].set_title("\nHasil Enkoder NRZ-L", fontweight='bold') # Judul subplot
    axs[1].set_ylim(-1.5, 1.5) # Skala Y
    axs[1].set_yticks([-1, 0, 1]) # Label Y
    axs[1].grid(True) # Tampilkan grid
    for i in range(len(input_biner) + 1): # Garis vertikal untuk setiap bit
        axs[1].axvline(i, color='gray', linestyle='--', linewidth=0.5) # Garis vertikal untuk setiap bit
    for i, bit in enumerate(input_biner):  # Tampilkan nilai bit di atas sinyal
        axs[1].text(i + 0.5, 1.2, bit, ha='center', fontsize=9, fontweight='bold')

    # Plot sinyal hasil decoding
    axs[2].plot(time_out, volt_out, drawstyle='steps-post', linewidth=2, color='orange') # Sinyal hasil decoding
    axs[2].set_title("\nHasil Dekoder", fontweight='bold') # Judul subplot
    axs[2].set_ylim(-0.5, 1.5) # Skala Y
    axs[2].set_yticks([0, 1]) # Label Y
    axs[2].grid(True) # Tampilkan grid
    for i in range(len(input_biner) + 1): # Garis vertikal untuk setiap bit
        axs[2].axvline(i, color='gray', linestyle='--', linewidth=0.5) # Garis vertikal untuk setiap bit
    for i, bit in enumerate(biner_dekoder):  # Tampilkan nilai bit
        axs[2].text(i + 0.5, 1.1, bit, ha='center', fontsize=9, fontweight='bold') # Tampilkan nilai bit di atas sinyal

    # Atur layout agar tidak tumpang tindih
    plt.tight_layout(rect=[0, 0.03, 1, 0.84]) # Atur margin bawah untuk teks deskriptif 
    plt.show()  # Tampilkan semua plot
