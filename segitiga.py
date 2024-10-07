Sisi1 = float(input("Masukkan panjang sisi pertama: "))
Sisi2 = float(input("Masukkan panjang sisi kedua: "))
Sisi3 = float(input("Masukkan panjang sisi ketiga: "))

if Sisi1 == Sisi2 == Sisi3:
    print("Sama Sisi")
elif Sisi1 == Sisi2 or Sisi1 == Sisi3 or Sisi2 == Sisi3:
    print("Sama Kaki")
elif (Sisi1**2 + Sisi2**2 == Sisi3**2) or (Sisi1**2 + Sisi3**2 == Sisi2**2) or (Sisi2**2 + Sisi3**2 == Sisi1**2):
    print("Siku-siku")
else:
    print("Lainnya")
