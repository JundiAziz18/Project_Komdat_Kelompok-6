# nrzl_LIB/nrzl_LIB.py

import matplotlib.pyplot as plt

def ascii_to_binary(text):
    """Konversi string ke representasi biner ASCII."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_ascii(binary_string):
    """Konversi biner ke string ASCII."""
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    return ''.join(chr(int(b, 2)) for b in chars)

def nrzl_encode(text):
    """
    Enkode teks ke sinyal NRZ-L.
    NRZ-L Mapping:
        '1' → -5V
        '0' → +5V
    """
    binary = ascii_to_binary(text)
    nrzl_signal = [-5 if bit == '1' else 5 for bit in binary]
    return nrzl_signal, binary  # Kembalikan biner juga untuk referensi

def nrzl_decode(nrzl_signal):
    """
    Dekode sinyal NRZ-L ke teks.
    -5 → '1', +5 → '0'
    """
    binary = ''.join('1' if level == -5 else '0' for level in nrzl_signal)
    return binary_to_ascii(binary)

def plot_nrzl(signal, title="NRZ-L Signal", binary_str=None):
    """
    Menampilkan grafik gelombang NRZ-L.
    """
    time = []
    voltage = []
    for i, level in enumerate(signal):
        time.extend([i, i + 1])
        voltage.extend([level, level])

    plt.figure(figsize=(12, 4))
    plt.title(title)
    plt.xlabel("Bit Time")
    plt.ylabel("Voltage (V)")
    plt.grid(True)
    plt.ylim(-6, 6)
    plt.yticks([-5, 0, 5])
    plt.plot(time, voltage, drawstyle='steps-post', linewidth=2)

    if binary_str:
        for i, bit in enumerate(binary_str):
            plt.text(i + 0.4, 5.5, bit, fontsize=12, ha='center')

    plt.show()
