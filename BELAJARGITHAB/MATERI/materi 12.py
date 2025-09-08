import json
# tambahkan bodule 'json' dengan 'import'
print("MATERI 12 - JSON FILE HANDLING")
print("=======READ JSON =======")
file_path_json = r"C:\pelajaran koding\materi kelas\materi.json"
with open(file_path_json, "r") as file_materi:
    # json.load() -> membaca file json
    data_materi =json.load(file_materi)
    # akses data json dengan 'key' nya
    print(f"judul berkas: {data_materi['title']}")
    print(f"Total kelas A: {data_materi['total']}")
    print(f"status santri: {data_materi['status_santri']}")
    print(f"status kelulusan: {data_materi['status_lulus']}")
    print(f"pelajaran: {data_materi['pelajaran']}")
    #ekstak data list dengan for loop
    for pelajaran in data_materi['pelajaran']:
        print(f"-> {pelajaran}")
    # ekstak semua data array objek surat
    # di pythan di sebut jd list of dictionary
    # key surat : no, nama, ayat, turun
    print("_" * 50) # menggandakan simbol dengan perkaliaan
    print("| NO | Nama Surat | Ayat | Tempat Turun |")
    print("_" * 50)
    for surah in data_materi['surah']:
        print(f"| {surah['no']} | {surah['nama']} | {surah['ayah']} | {surah['turun']} |")