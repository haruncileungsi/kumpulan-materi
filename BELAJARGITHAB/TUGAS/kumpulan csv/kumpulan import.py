# panggilan module kumpulan doa
import doa
import random
import math
#import math (module matematika)
doa_sebelum_makan = doa.doa_setelah_makan()
print(f"doa sebelum makan: {doa_sebelum_makan}")
tebak_angka = random. randint(11, 64)

# tugas pekanan ke satu (1)

import doa
import random
import math
doa_sebelum_tidur = doa.doa_sebelum_tidur()
doa_bangun_tidur = doa.doa_bangun_tidur()
doa_sebelum_makan = doa.doa_setelah_makan()
print(f"doa sebelum makan: {doa_sebelum_makan}")
print(f"doa sebelum tidur: {doa_sebelum_tidur}")
print(f"doa bangun tidur: {doa_bangun_tidur}")
tebak_angka = random.randint(20, 65)

# tugas ke dua (2)
import doa

uang_jajan = [50000, 30000, 15000, 70000, 10000] 
print (doa.tambah_lima_rebu(uang_jajan))

# tugas ke tiga (3)
import rangking
nilai = [75, 90, 60, 88, 100, 55]
nilai_urut = rangking.urut_nilai(nilai)
print(f"urutkan nilai santri : {nilai_urut}")

nilai_tertinggi = rangking.nilai_tertinggi(nilai)
print(f"nilai tertinggi santri : {nilai_tertinggi}")
nilai_terendah = rangking.nilai_terendah(nilai)
print(f"nilai terendah santri : {nilai_terendah}")

import emoji 
mood = ["senang", "sedih", "marah", "ati"]
print(emoji.convert_moot(mood))