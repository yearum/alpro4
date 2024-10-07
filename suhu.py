suhuCelcius = float(input("Masukkan suhu Celcius: "))
suhuReamur = float(input("Masukkan suhu Reamur: "))
suhuKelvin = float(input("Masukkan suhu Kelvin: "))

# Konversi antar suhu
reamur_ke_celcius = suhuReamur * 5 / 4
kelvin_ke_celcius = suhuKelvin - 273.15

if suhuCelcius == reamur_ke_celcius and suhuCelcius == kelvin_ke_celcius:
    print("Semua Sama")
elif suhuCelcius == reamur_ke_celcius:
    print("Celcius = Reamur")
elif suhuCelcius == kelvin_ke_celcius:
    print("Celcius = Kelvin")
elif reamur_ke_celcius == kelvin_ke_celcius:
    print("Reamur = Kelvin")
else:
    print("Tidak ada yang sama")
