import matplotlib.pyplot as plt # Library untuk plotting

def ascii_ke_biner(text): # Fungsi untuk mengonversi teks ke biner
    return ''.join(format(ord(c), '08b') for c in text) # Fungsi ini mengonversi setiap karakter ke representasi biner 8-bit

def biner_ke_ascii(binary_str):
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)] # Memecah string biner menjadi karakter 8-bit
    return ''.join(chr(int(c, 2)) for c in chars) # Mengonversi setiap karakter biner ke karakter ASCII

def enkoder_manchester(text):
    binary = ascii_ke_biner(text) # Mengonversi teks ke biner
    signal = [] # Inisialisasi sinyal kosong
    for bit in binary: # Iterasi setiap bit dalam string biner
        if bit == '1': # Jika bit adalah '1'
            signal.extend([1, -1])  # Tambahkan level sinyal untuk '1'
        else: # Jika bit adalah '0'
            signal.extend([-1, 1]) # Tambahkan level sinyal untuk '0'
    return signal, binary # Mengembalikan sinyal Manchester dan string biner

def dekoder_manchester(signal): # Fungsi untuk mendekode sinyal Manchester
    binary = '' # Inisialisasi string biner kosong
    for i in range(0, len(signal), 2):  # Iterasi setiap dua level sinyal
        pair = signal[i:i+2] # Mengambil sepasang level sinyal
        if pair == [-1, 1]: # Jika pasangan adalah [-1, 1]
            binary += '0' # Tambahkan '0' ke string biner
        elif pair == [1, -1]: # Jika pasangan adalah [1, -1]
            binary += '1' # Tambahkan '1' ke string biner
        else: # Jika pasangan tidak valid
            raise ValueError(f"Invalid Manchester signal at position {i}: {pair}") # Tampilkan pesan kesalahan
    return biner_ke_ascii(binary), binary # Mengonversi biner ke teks ASCII

# Fungsi sinyal digital dengan skala waktu tetap
def sinyal_digital(binary_str, high=1, low=0, bit_width=2): 
    signal = [high if bit == '1' else low for bit in binary_str] # Membuat sinyal berdasarkan nilai biner
    time = [] # Inisialisasi daftar waktu
    voltage = [] # Inisialisasi daftar tegangan
    for i, level in enumerate(signal): # Iterasi setiap level sinyal
        t_start = i * bit_width # Menghitung waktu mulai untuk level sinyal
        t_end = t_start + bit_width # Menghitung waktu akhir untuk level sinyal
        time.extend([t_start, t_end]) # Menambahkan waktu mulai dan akhir ke daftar waktu
        voltage.extend([level, level]) # Menambahkan level tegangan ke daftar tegangan
    return time, voltage # Mengembalikan daftar waktu dan tegangan   

# Fungsi utama plotting
def plot_manchester(input_text): # Fungsi untuk memplot sinyal Manchester
    signal_manchester, binary_input = enkoder_manchester(input_text) # Enkode teks input menjadi sinyal Manchester
    decoded_text, binary_decoded = dekoder_manchester(signal_manchester) # Dekode sinyal Manchester menjadi teks

    bit_width = 2 # Lebar bit untuk visualisasi
    total_bits = len(binary_input) # Total bit dalam input biner

    time_input, volt_input = sinyal_digital(binary_input, bit_width=bit_width)  # Membuat sinyal digital untuk input biner
    time_output, volt_output = sinyal_digital(binary_decoded, bit_width=bit_width) # Membuat sinyal digital untuk output biner yang didekode

    time_manchester, volt_manchester = [], [] # Inisialisasi daftar waktu dan tegangan untuk sinyal Manchester
    for i, level in enumerate(signal_manchester): # Iterasi setiap level sinyal Manchester
        t = i  # Menghitung waktu untuk level sinyal
        time_manchester.extend([t, t + 1]) # Menambahkan waktu untuk level sinyal
        volt_manchester.extend([level, level]) # Menambahkan level tegangan untuk level sinyal

    fig, axs = plt.subplots(3, 1, figsize=(16, 10), sharex=True) # Membuat subplots untuk tiga grafik
    fig.suptitle("Manchester IEEE Encoding & Decoding", fontsize=16, y=0.95)    # Judul utama grafik

    # Tambahkan teks deskriptif di bawah judul utama
    fig.text(0.5, 0.91, f"Input Text: {input_text}", ha='center', fontsize=12) # Teks input yang akan dienkode
    fig.text(0.5, 0.88, f"Input Binary: {binary_input}", ha='center', fontsize=10) # Teks biner input
    fig.text(0.5, 0.85, f"Decoded Text: {decoded_text}", ha='center', fontsize=12) # Teks yang didekode dari sinyal Manchester

    # Plot input binary
    axs[0].plot(time_input, volt_input, drawstyle='steps-post', color='green', linewidth=2) # Plot sinyal biner input
    axs[0].set_title("Input Binary Signal (0=0V, 1=1V)") # Judul grafik input biner
    axs[0].set_ylim(-0.5, 1.5) # Set batas y untuk grafik input biner
    axs[0].set_yticks([0, 1]) # Set tick y untuk grafik input biner
    axs[0].grid(True, which='major', axis='y') # Tambahkan grid pada grafik input biner
    for i in range(total_bits + 1): # Tambahkan garis vertikal untuk setiap bit
        axs[0].axvline(x=i * bit_width, color='gray', linestyle='--', linewidth=0.5) # Garis vertikal untuk setiap bit
    for i in range(total_bits): # Tambahkan teks untuk setiap bit pada grafik input biner
        axs[0].text(i * bit_width + bit_width / 2, 1.1, binary_input[i], ha='center', fontsize=9) # Teks untuk setiap bit input biner

    # Plot Manchester
    axs[1].plot(time_manchester, volt_manchester, drawstyle='steps-post', color='blue', linewidth=2) # Plot sinyal Manchester
    axs[1].set_ylim(-2, 2) # Set batas y untuk grafik Manchester
    axs[1].set_title("Manchester Encoded Signal") # Judul grafik sinyal Manchester
    axs[1].set_yticks([-1, 0, 1]) # Set tick y untuk grafik sinyal Manchester
    axs[1].set_ylabel("Voltage Level") # Label sumbu y untuk grafik sinyal Manchester
    axs[1].grid(True, which='major', axis='y') # Tambahkan grid pada grafik sinyal Manchester
    for i in range(total_bits + 1): # Tambahkan garis vertikal untuk setiap bit pada grafik sinyal Manchester
        axs[1].axvline(x=i * 2, color='gray', linestyle='--', linewidth=0.5) # Garis vertikal untuk setiap bit pada grafik sinyal Manchester
    for i in range(total_bits): # Tambahkan teks untuk setiap bit pada grafik sinyal Manchester
        axs[1].text(i * 2 + 1, 1.5, binary_input[i], ha='center', fontsize=9) # Teks untuk setiap bit pada grafik sinyal Manchester

    # Plot decoded output
    axs[2].plot(time_output, volt_output, drawstyle='steps-post', color='red', linewidth=2) # Plot sinyal biner yang didekode
    axs[2].set_title("Decoded Binary Signal (0=0V, 1=1V)") # Judul grafik sinyal biner yang didekode
    axs[2].set_ylim(-0.5, 1.5) # Set batas y untuk grafik sinyal biner yang didekode
    axs[2].set_yticks([0, 1]) # Set tick y untuk grafik sinyal biner yang didekode
    axs[2].grid(True, which='major', axis='y') # Tambahkan grid pada grafik sinyal biner yang didekode
    for i in range(total_bits + 1): # Tambahkan garis vertikal untuk setiap bit pada grafik sinyal biner yang didekode
        axs[2].axvline(x=i * bit_width, color='gray', linestyle='--', linewidth=0.5) # Garis vertikal untuk setiap bit pada grafik sinyal biner yang didekode
    for i in range(len(binary_decoded)):   # Tambahkan teks untuk setiap bit pada grafik sinyal biner yang didekode
        axs[2].text(i * bit_width + bit_width / 2, 1.1, binary_decoded[i], ha='center', fontsize=9) # Teks untuk setiap bit pada grafik sinyal biner yang didekode

    plt.tight_layout(rect=[0, 0, 1, 0.83]) # Mengatur tata letak agar tidak ada tumpang tindih
    plt.show() # Menampilkan grafik
