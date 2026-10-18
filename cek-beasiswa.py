def Cek_beasiswa():
    print("Masukan data Mahasiswa untuk Pengecekan Beasiswa")
    data = int(input())

    for i in range (1,data + 1):
        try:
            ipk = float(input("Enter your IPK: "))
            penghasilan = float(input("Enter your Penghasilan orang tua: "))

            if not (0.0 <= ipk <= 4.0):
                print("Input tidak valid: IPK harus berada dalam rentang 0.0 sampai 4.0.")
            elif penghasilan < 0:
                print("Input tidak valid: Penghasilan orang tua tidak boleh bernilai negatif.")    
            else:
                if ipk >= 3.0 and penghasilan < 4000000:
                    print("Kamu lulus mendapatkan beasiswa.")
                else:
                    if ipk < 3.0:
                        print("IPK kamu kurang dari 3.0.")
                    if penghasilan >= 4000000:
                        print("Penghasilan orang tua kamu terlalu tinggi.")
                    print("Kamu tidak memenuhi syarat untuk mendapatkan beasiswa.")

        except ValueError:
            print("Input tidak valid: Harap masukkan nilai berupa angka.")
Cek_beasiswa()
        
        
    

status =str(input("apakah ingin pengecekan ulang ? (y/n)"))
if status == "y":
    Cek_beasiswa()
else: print("Terima kasih")