print("materi 7 - python STRUCTURES")
print("----------------------------")
# set -> {} -> tidak berurutan, tidak busa diubah, tidak boleh duplikat
game_azka={"valoran", "pudg", "free fire"}
game_azka.add("mobil lageds")
print("Game azka", game_azka)


game_zaky={"pudg", "free fire", "call of duthy"}
game_zaky.add("valorant")

print("game zaky", game_zaky)
game_gabungan = game_azka | game_zaky # (bisa pakai | atau or)
print("daftar game gabungan:", game_gabungan)
# fo (loop) untuk mengeluarkan isi item set
for i in game_gabungan:
    print("-->",i)
    print("--> transfer data game",i,"ke serfer")

# distionary (dict) -> {key:value} / {kuci:isi}
# -> berurutan, bisa di ubah, bolrh duplikat

kamus_anime = {
   "one_piece": "monkey D luffy",
   "demon_slayer": "tanjiro",
   "waifu":{
       "one piece": "big mon",
       "demon slayer": "nezuko"
       }
}

print("kamus anime:", kamus_anime)
print("mc bemon slayer:", kamus_anime["demon_slayer"])
print("waifu naruto", kamus_anime["waifu"]["demon slayer"])

# merubah item dari dictionary
kamus_anime["naruto"] = "shikamaru"
print("mc naruto", kamus_anime["naruto"])

# mengubah item dari dictionary
kamus_anime["demon slayer"] = 'tanjiro'
print("mc demon slayer", kamus_anime["demon slayer"])

# apus item dari dictionary
del(kamus_anime["one_piece"])
print("KAMUS ANIME TERBARU:", kamus_anime)

harun = {
    "nama": 15,
    "asal": "bogor",
    "kelas": "10 a"
}

print(harun["kelas"])

# 2. menambahkan niai

harun["berat_badan"] = 75
print(harun["berat_badan"])

# 3. mengubah nilai
harun["berat_badan"] = 65
print(harun)

# 4. menghapu nilai
del(harun["berat_badan"])
print(harun)

# 5. mengecek key
print("berat_badan" in harun)

# 6. mendapat kan key dan value
# cara ngecek ada key apa gk
print(harun.keys())
# cara ngecek ada velue apa gk
print(harun.values())

# 7. looping di dalam dictionary
for key in harun:
    print(key)

for velue in harun.values():
    print(velue)

for key, velue in harun.items():
    print(f"{key} <- {velue}") # f berguna intuk memasukan variabel

# 8. nasted dictionary
kelas = {
     "siswa1": {
         "nama": "harun",
         "umur": 15,
         "asal": "bogor",
         "hobi": {
             "hobi1": "makan",
             "hobi2": "tidur",
             "hobi3": "marah marah",
             "hobi4": {
                 "bola1": "bola sepak",
                 "bola2": "bola basket",
                 "bola3": "bola voli",
             },
         },
     },
    "siswa2":{
        "nama": "umaer",
        "umur": 17,
        "asal": "beksi",
        "hobi": "mancing"
    },
 }
print(kelas["siswa1"])
print(kelas["siswa2"])