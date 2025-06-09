from lib.nrzl_lib.nrzl_encoder import * 
from lib.nrzl_lib.nrzl_decoder import * 
from lib.manc_lib.manc_encoder import * 
from lib.manc_lib.manc_decoder import * 

if __name__ == "__main__":
    while True:
        print("\nPilih Tipe Enkoder :")
        print("1. NRZ-L")
        print("2. Manchester")
        print("3. Exit")
        choice = input("Masukan pilihan anda (1/2/3): ")

        if choice == "1":
            text = input("Masukan input teks untuk dienkoding dengan NRZ-L: ")            
            plot_encoder_nrzl(text)

            signal, _ = nrzl_enkoder(text)
            print("Sinyal NRZ-L yang akan didekode:", f"\"{'-'.join(map(str, signal))}\"")
            decoded_text, binary_output = nrzl_dekoder(signal)
            print(f"Hasil Dekode: \"{decoded_text}\"")
            print(f"Output Biner Dekode: \"{binary_output}\"")
            plot_decoder_nrzl(signal)

        elif choice == "2":
            text = input("Masukan input teks untuk dienkoding dengan Manchester: ")
            plot_encoder(text)

            signal_manchester, _ = enkoder_manchester(text)
            print(f"Sinyal Manchester yang akan didekode: \"{'-'.join(map(str, signal_manchester))}\"")
            decoded_text, binary_output = dekoder_manchester(signal_manchester)
            print(f"Hasil Dekode: \"{decoded_text}\"")
            print(f"Output Biner Dekode: \"{binary_output}\"")
            plot_decoder(signal_manchester)

        elif choice == "3":
            print("Exit program.")
            break

        else:
            print(" Pilihan Invalid\n Coba Lagi!!!.")