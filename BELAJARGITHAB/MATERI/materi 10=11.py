import csv

print("materi 10 - file hanling")
print("------------------------")
# buka file
file_path = r"C:\pelajaran koding\materi kelas\jajan.csv"
file_pesan = open (file_path, "r")
# baca file
isi_pesan = file_pesan.read()
# tampilkan output
print(f"ISI PESAN  => {isi_pesan}")
# tutup file
file_pesan.close()

print("-----read csv file-----")
file_path_csv = r"C:\pelajaran koding\materi kelas\jajan.csv"
file_pesan = open (file_path_csv, "r")
# baca file
isi_pesan = file_pesan.read()
# tampilkan output
print(f"ISI PESAN  => {isi_pesan}")
# tutup file
file_pesan.close()
print("======append csv file=======")
jajan_baru = [6, "zahran", "200.000.000"]
print(f"jajan baru: {jajan_baru}")
with open(file_path_csv, "a", newline="") as file_jajan:
   writer = csv.writer(file_jajan)
   writer.writerow(jajan_baru)

# materi ke sebelas (11) {bagian 1.}

print("=====UPDATE CSV=====")
# baca semua file -> ektrak data -> buat data baru
# -> tulis semua isi baris nya dengan mode "w"
file_path_csv = r"C:\pelajaran koding\materi kelas\jajan.csv"
# siap kan data jajan kosong untuk menampung data dari csv ke list
data_jajan = []
with open(file_path_csv, "r") as file_jajan:
   # csv.riader() -> membaca isi file csv
  isi_table_jajan = csv.reader(file_jajan)
   # estrak semua data dengan for loop
for item_jajan in isi_table_jajan:
      print(item_jajan)
      # tambah item ke list data jajan
      data_jajan.append(item_jajan)

# mengubah atau membuat data baru {bagian 2.}
for item in data_jajan:
   print(f"proses item no => {item[0]}")
   print(item)
   # jika kolem nama (index 1) adalah "x nama"
   if item[1] == "syahid":
      uang_jajan_baru = 754000
      item[2] = uang_jajan_baru
      print(f"data ditemukan, ganti uang jajan{uang_jajan_baru}")
   print("=====loop end=====")

# hapus data di list index 2
del data_jajan[3]
print(f"DATA JAJAN TERKINI: {data_jajan}")

# tulis uang dengan mode "w" -> writer
with open(file_path_csv, "w", newline="") as file_jajan:
   writer = csv.writer(file_jajan)
   # writerows() -> tulis sekali banyak
   writer.writerows(data_jajan)