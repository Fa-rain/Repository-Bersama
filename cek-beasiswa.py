try:
    ipk = float(input("Masukkan IPK: "))
    penghasilan = float(input("Masukkan penghasilan orang tua: "))
    kategori = input("Pilih kategori beasiswa (penuh/parsial): ").lower()

    if not (0.0 <= ipk <= 4.0):
        print("Input tidak valid: IPK harus berada dalam rentang 0.0 sampai 4.0.")
    elif penghasilan < 0:
        print("Input tidak valid: Penghasilan orang tua tidak boleh negatif.")
    elif kategori not in ["penuh", "parsial"]:
        print("Kategori beasiswa tidak valid.")
    elif kategori == "penuh":
        if ipk >= 3.5 and penghasilan < 4000000:
            print("Kamu mendapatkan beasiswa penuh.")
        else:
            print("Kamu tidak memenuhi syarat beasiswa penuh.")
    elif kategori == "parsial":
        if ipk >= 3.0 and penghasilan < 4000000:
            print("Kamu mendapatkan beasiswa parsial.")
        else:
            print("Kamu tidak memenuhi syarat beasiswa parsial.")

except ValueError:
    print("Input tidak valid: Harap masukkan nilai berupa angka untuk IPK dan penghasilan.")
