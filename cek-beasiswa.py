ipk = float(input("Enter your IPK: "))
penghasilan = float(input("Enter your Penghasilan orang tua : "))
if ipk >= 3.0 and penghasilan < 4000000:
    print("kamu lulus mendapatkan beasiswa")
else:
    if (ipk < 3.00 ):
        print("IPK kamu kurang dari 3.0.")
    if (penghasilan >= 4000000):  
        print("Penghasilan orang tua kamu terlalu tinggi.")
    print("Kamu tidak memenuhi syarat untuk mendapatkan beasiswa.") 