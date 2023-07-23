import re

text = "Nama Mahasiswa: John Doe, Email: john.doe@example.com, Nama Mahasiswa: Jane Smith, Email: jane.smith@example.com"

# Pola regex untuk nama mahasiswa
nama_mahasiswa_pattern = r"[A-Za-z]+(?: [A-Za-z]+)*"
# Pola regex untuk email
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Mencari semua kombinasi nama_mahasiswa dan email dalam teks
nama_mahasiswa_list = re.findall(nama_mahasiswa_pattern, text)
email_list = re.findall(email_pattern, text)

# Menggabungkan hasil
for nama_mahasiswa, email in zip(nama_mahasiswa_list, email_list):
    print(f"Nama Mahasiswa: {nama_mahasiswa}, Email: {email}")
