print("materi 6 - python data struktur")
print("------------------")

# list[] (berurutan bisa diubah, boleh di boleh di duplikat )
daftar_belanja = [
    "teh desa", # index 0
    "nasi padang", # index 1
    "pisang kembung", # index 2
]

print("isi tas belanja:",daftar_belanja)
print("item ke-1:", daftar_belanja[0])
print("item ke-2:", daftar_belanja[1])
# menambah item batru ke akhir list
daftar_belanja.append("olive chiken")
daftar_belanja.append("gabin")
print ("isi tas belanja skrg:", daftar_belanja)
print ("item ke-4:", daftar_belanja[3])
# remove() menghapus item dari list
daftar_belanja.remove("pisang kembung")
print("isi tas belanja akhir:",daftar_belanja)

# tuple (berurutan, bedanya tidak bisa diubah, boleh di duplikat) 
# penulisan nya menggunakan ()
ttl = (21, "april", 2003)
print("tgl lahi umair harun:", ttl)
# [no_index] akses data tuple
print("tgl:", ttl[0])
print("bulan:",ttl[1])
print("tahun:", ttl[2])
# akses bulan (posisi index) lalu batas akhir item nya
print("bulan tahun:", ttl[4:2])
# unpeking tuple ke variable baru
# mengikuti urutan itemnya

# manipulasi list lanjutan
jajan_umer = ("pentol", "cireng")
jajan_harun = ("olive", "gorengan")

print("jajan_ujang_dan_asep")

# list minuman
list_minuman = [
    ["kopi", "susu", "teh"], #baris 0
     ["jus apel", "jus melon", "jus semangka" ], # baris 1
    ["es kepala", "es bir", "es ciu"], # baris 2
]

print(list_minuman[0][2])


# materi pengulangan

buah = ["jagung", "tomat", "jambu", "kelapa", ]

# 1. mengubah elemen [index]

print(buah[1])

# 2.mengubah nilai nya
buah[1] = "aprikot"
print(buah)

# 3. menambah elemen
# di akhir
buah.append("pir")
print("buah")

buah.insert(1, "semangka")
print(buah)

# 4. menghapus elemen
# menghapus berdararkan isi
buah.remove("jagung")
print(buah)

# menghapus berdasarkan index
buah.pop(2)
print(buah)

# 5. panjang list
print(len(buah))

# 6. mencetak seluruh isi list menggunakan looping

for item in buah:
    print(buah)

# tugas malam ini

listbuah = []
print("coba pilh 5 nama dari nama nama buah buah an")
buah1=input("buah pertama: ")
#buah3=input("buah ke tiga: ")
listbuah.append(buah3)
listbuah.append(buah4)
buah5=input("buah ke lima: ")

print("buah yg kamu pilih adalah: ")
print(h)