grKarbohidrat = float(input("Masukkan berat karbohidrat (gr): "))
grProtein = float(input("Masukkan berat protein (gr): "))
grLemak = float(input("Masukkan berat lemak (gr): "))
grVitMin = float(input("Masukkan berat vitamin dan mineral (gr): "))

totalBerat = grKarbohidrat + grProtein + grLemak + grVitMin

persenKarbohidrat = (grKarbohidrat / totalBerat) * 100
persenProtein = (grProtein / totalBerat) * 100
persenLemak = (grLemak / totalBerat) * 100
persenVitMin = (grVitMin / totalBerat) * 100

if 55 <= persenKarbohidrat <= 60 and \
   10 <= persenProtein <= 20 and \
   7 <= persenLemak <= 10 and \
   10 <= persenVitMin <= 15:
    print("Sehat")
else:
    print("Tidak Sehat")
