from NRZL_LIB import plot_hasil_nrzl
from MANC_LIB import plot_manchester

# Contoh penggunaan

def main():
    input_char = input("Masukkan teks/ karakter untuk NRZ-L: ")  # Input teks dari pengguna
    plot_hasil_nrzl(input_char)  # Panggil fungsi untuk memplot hasil NRZ-L

    input_text = input("Masukkan teks/ karakter untuk Manchester: ")  # Input teks dari pengguna
    plot_manchester(input_text)  # Panggil fungsi untuk memplot hasil Manchester

main()  # Panggil fungsi utama