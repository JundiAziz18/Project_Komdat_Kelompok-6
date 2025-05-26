# Import library numpy untuk array dan matplotlib untuk plotting grafik
import numpy as np # Import library numpy untuk array
import matplotlib.pyplot as plt # Import library matplotlib untuk plotting grafik

# Fungsi untuk mengubah biner menjadi sinyal Manchester
def manchester_encode(bits): 
    signal = []  # List kosong untuk menyimpan sinyal
    for bit in bits:  # Loop setiap bit dalam string biner
        if bit == '1':
            # Jika bit 1, transisi dari rendah ke tinggi (-0.5 ke 0.5)
            signal.extend([-0.5, 0.5])
        else:
            # Jika bit 0, transisi dari tinggi ke rendah (0.5 ke -0.5)
            signal.extend([0.5, -0.5])
    return signal  # Kembalikan sinyal hasil encoding

# Fungsi untuk decoding sinyal Manchester menjadi biner
def manchester_decode(signal):
    bits = ''  # String kosong untuk menyimpan bit hasil decoding
    # Loop setiap dua nilai (karena 1 bit terdiri dari 2 bagian sinyal)
    for i in range(0, len(signal), 2):
        first_half = signal[i]      # Bagian pertama sinyal
        second_half = signal[i + 1] # Bagian kedua sinyal
        if first_half == 0.5 and second_half == -0.5:
            bits += '0'  # Ini berarti bit aslinya adalah 0
        elif first_half == -0.5 and second_half == 0.5:
            bits += '1'  # Ini berarti bit aslinya adalah 1
        else:
            bits += '?'  # Jika tidak cocok, berarti ada kesalahan
    return bits  # Kembalikan hasil decoding

# Input dari user berupa 1 karakter
character = input("Input satu karakter: ")

# Ubah karakter ke nilai ASCII, lalu ke bentuk biner, dan pastikan 8 bit
binary_representation = bin(ord(character))[2:].zfill(8)

# Tampilkan representasi biner ke layar
print("Representasi biner:", binary_representation)

# Panggil fungsi encode untuk mendapatkan sinyal Manchester
encoded_signal = manchester_encode(binary_representation)

# Buat array waktu untuk sumbu X grafik
time = np.arange(len(encoded_signal))

# Mulai menggambar grafik sinyal Manchester
plt.step(time, encoded_signal, where='mid', linewidth=2, color='blue')  # Jenis grafik "step"
plt.ylim(-1, 1.5)  # Batas bawah dan atas sumbu Y
plt.yticks([-1, 1], ["-1", "1"])  # Label sumbu Y
plt.xlabel("Waktu")  # Label sumbu X
plt.ylabel("Level Sinyal")  # Label sumbu Y
plt.title("Sinyal Manchester Encoding")  # Judul grafik
plt.grid()  # Tambahkan grid

# Tambahkan teks bit di atas sinyal
for i, bit in enumerate(binary_representation):
    # Letakkan bit di atas titik tengah tiap pasangan sinyal
    plt.text(i * 2 + 0.5, 1.2, bit, fontsize=12, ha='center', color='red', fontweight='bold') # Teks bit berwarna merah, tebal, dan ukuran 12, ha='center' untuk rata tengah

# Tampilkan grafik ke layar
plt.show()

# Panggil fungsi decode untuk mengubah sinyal ke biner
decoded_binary = manchester_decode(encoded_signal)

# Ubah biner hasil decoding ke karakter asli
decoded_char = chr(int(decoded_binary, 2))

# Tampilkan hasil decoding
print("Hasil decoding biner:", decoded_binary)
print("Karakter hasil decoding:", decoded_char)