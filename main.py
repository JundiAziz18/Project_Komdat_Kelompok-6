from NRZL_LIB import plot_hasil_nrzl
from MANC_LIB import plot_manchester

# Program utama untuk memilih jenis enkoder dan menjalankan fungsinya
while True:
    print("\n=== Menu Encoder ===") # Menampilkan menu utama
    print("1. NRZ-L Encoder and Decoder") # Pilihan untuk NRZ-L Encoder dan Decoder
    print("2. Manchester Encoder and Decoder")   # Pilihan untuk Manchester Encoder dan Decoder
    print("3. Keluar") # Pilihan untuk keluar dari program
    pilihan = input("Pilih jenis encoder (1/2/3): ")    # Input pilihan dari pengguna

    if pilihan == "1": # Jika pilihan adalah 1
        print("=== NRZ-L Encoder and Decoder ===") # Menampilkan judul NRZ-L Encoder dan Decoder
        input_nrzl = input("Masukkan teks/ karakter untuk NRZ-L: ") # Input teks/karakter untuk NRZ-L
        plot_hasil_nrzl(input_nrzl) # Memanggil fungsi untuk memplot hasil NRZ-L
    elif pilihan == "2": # Jika pilihan adalah 2
        print("=== Manchester Encoder and Decoder ===") # Menampilkan judul Manchester Encoder dan Decoder
        input_manchester = input("Masukkan teks/ karakter untuk Manchester: ") # Input teks/karakter untuk Manchester
        plot_manchester(input_manchester) # Memanggil fungsi untuk memplot hasil Manchester
    elif pilihan == "3": # Jika pilihan adalah 3
        print("Terima kasih telah menggunakan program ini.") # Menampilkan pesan terima kasih
        break # Keluar dari loop dan program
    else: # Jika pilihan tidak valid
        print("Pilihan tidak valid. Silakan coba lagi.") # Menampilkan pesan kesalahan

