import csv
file_path = r"C:\pelajaran koding (python)\kumpulan kumpulan tugas pekanan\tugas_keuangan.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)
    print("semua keuangan")
    print("_" * 50)
    print("Tanggal | keterangan | kategoro | jumlah")
    for baris in list_read:
        tanggal = baris[0]
        keterangan = baris[1]
        kategori = baris[2]
        print(f"{tanggal} | {keterangan} | {kategori} ")

#   TAMBAH DATA
with open(file_path, "a", newline="") as file_baru:
    write = csv.writer(file_baru)
    write.writerow(["5", "faiz", "18"])