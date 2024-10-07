dd = int(input("Masukkan hari (dd): "))
mm = int(input("Masukkan bulan (mm): "))
yyyy = int(input("Masukkan tahun (yyyy): "))


def is_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

if (mm == 2 and ((is_kabisat(yyyy) and 1 <= dd <= 29) or (not is_kabisat(yyyy) and 1 <= dd <= 28))) or \
   (mm in [4, 6, 9, 11] and 1 <= dd <= 30) or \
   (mm in [1, 3, 5, 7, 8, 10, 12] and 1 <= dd <= 31):
    print("Valid")
else:
    print("Tidak Valid")