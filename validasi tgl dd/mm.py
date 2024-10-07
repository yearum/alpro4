dd = int(input("Masukan hari(dd): "))
mm = int(input("Masukan bulan(mm): "))

if (mm == 2 and 1 <= dd <= 28) or \
   (mm in [4, 6, 9, 11] and 1 <= dd <= 30) or \
   (mm in [1, 3, 5, 7, 8, 10, 12] and 1 <= dd <= 31):
    print("Valid")
else:
    print("Tidak Valid")
