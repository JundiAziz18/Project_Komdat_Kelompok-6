from NRZL_LIB import *

text = input("Enter text to encode: ")
text = text.strip()
if not text:
    print("No input provided. Exiting.")
    exit()
signal, binary = nrzl_encode(text)
plot_nrzl(signal, binary_str=binary)
print("Decoded:", nrzl_decode(signal))
