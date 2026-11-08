# Nama : Arif Syefulloh
# NIM  : 51268071

def seleksi_beasiswa(ipk, penghasilan):
    if ipk >= 3.5 and penghasilan <= 3000000:
        return "LOLOS - Beasiswa Penuh (100%)"
    elif ipk >= 3.5 and penghasilan <= 5000000:
        return "LOLOS - Beasiswa 75%"
    elif ipk >= 3.0 and penghasilan <= 3000000:
        return "LOLOS - Beasiswa 50%"
    elif ipk >= 3.0 and penghasilan <= 5000000:
        return "LOLOS - Beasiswa 25%"
    else:
        return "TIDAK LOLOS"

data = [
    ("Aditya", 3.8, 2500000),
    ("Adnan Faris", 3.6, 4500000),
    ("Angel", 3.2, 3800000),
    ("Alvio", 3.1, 4800000),
    ("Didi", 3.0, 3000000),
    ("Fatimah", 3.75, 2900000),
]

print("=== HASIL SELEKSI BEASISWA ===")
for nama, ipk, penghasilan in data:
    hasil = seleksi_beasiswa(ipk, penghasilan)
    print(f"{nama} | IPK: {ipk} | Penghasilan: Rp{penghasilan:,} | Hasil: {hasil}")
    
    