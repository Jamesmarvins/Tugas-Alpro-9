bilangan = []

while True:
    masukan_pengguna = input("Masukkan sebuah bilangan (atau 'selesai' untuk mengakhiri): ")
    
    if masukan_pengguna.lower() == 'selesai':
        break
        
    try:
        bilangan.append(float(masukan_pengguna))
    except ValueError:
        print("Masukan tidak valid. Silakan masukkan sebuah bilangan.")

if bilangan:
    print("Bilangan maksimum:", max(bilangan))
    print("Bilangan minimum:", min(bilangan))
else:
    print("Tidak ada bilangan yang dimasukkan.")