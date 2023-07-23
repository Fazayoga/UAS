import re

# Teks yang akan diuji (gantilah ini dengan teks yang sesuai)
text = "Hello bro, how are you doing? Bro, let's grab a coffee later."

# Definisikan pola regex untuk mencocokkan kata "bro" di mana saja dalam teks (tidak case-sensitive)
pattern = r'\bbr[o]+\b'

# Gunakan fungsi findall untuk menemukan semua kemunculan kata "bro" dalam teks
matches = re.findall(pattern, text, re.IGNORECASE)

# Cetak hasilnya
if matches:
    print("Kata 'bro' ditemukan dalam teks:")
    for match in matches:
        print(match)
else:
    print("Kata 'bro' tidak ditemukan dalam teks.")
