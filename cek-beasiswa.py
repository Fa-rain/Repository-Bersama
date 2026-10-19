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
            if ipk >= 3.0 and penghasilan < 4000000:
                print("\n[SELAMAT] Kamu lulus dan memenuhi syarat mendapatkan beasiswa.")
            elif ipk < 3.0 and penghasilan >= 4000000:
                print("\n[INFO] Maaf, kamu tidak memenuhi syarat karena IPK di bawah 3.0 dan penghasilan terlalu tinggi.")
            elif ipk < 3.0:
                print("\n[INFO] Maaf, kamu tidak memenuhi syarat karena IPK kurang dari 3.0.")
            else:
                print("\n[INFO] Maaf, kamu tidak memenuhi syarat karena penghasilan orang tua terlalu tinggi.")

            if ipk >= 3.25 and penghasilan < 5000000:
                print("\n[SELAMAT] Anda lolos seleksi beasiswa dengan kriteria terbaru.")
            elif ipk < 3.25 and penghasilan >= 5000000:
                print("\n[INFO] Maaf, Anda belum memenuhi kriteria IPK dan batas penghasilan.")
            elif ipk < 3.25:
                print("\n[INFO] Maaf, IPK Anda kurang dari standar minimal 3.25.")
            else:
                print("\n[INFO] Maaf, penghasilan orang tua melebihi batas ketentuan baru.")

except ValueError:
    print("Input tidak valid: Harap masukkan nilai berupa angka.")