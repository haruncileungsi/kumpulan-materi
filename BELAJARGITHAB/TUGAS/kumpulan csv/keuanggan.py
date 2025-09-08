import csv
file_path = r"C:\pelajaran koding (python)\kumpulan tugas githab\BELAJARGITHAB\TUGAS\kumpulan csv\data.csv"
with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)

    print("semua data")
    print("_" * 20)
    for baris in list_read:
        tanggal = baris[0]
        keterangan = baris[1]
        kategori = baris[2]

        print(f"{tanggal} | {keterangan} | {kategori} ")
