print("materi 9-pythan 3 funtion")
print("-------------------------")
def say_hello(name):
    # print("hello mr", name)
    # kasih f diawal string menyisipikan variabel/parameter
    print(f"hello mr, {name}")
    print("baek baek aee")

say_hello_mini = lambda name: print(f"hello mr, {name}")
# panggil fungsinya dibawah ini
say_hello("syahid")
say_hello("juna")
say_hello("harun")
print("----------->") 


# contoh penerapan labda_higher_order fungtion
# mab()-soted()-lifter()
jajan_mingguan = [100, 53000, 67000, 42000, 89000]
# sorted() -> mengurutkan data
urutan_jajan = sorted(jajan_mingguan)
urutan_jajan_terbalik = sorted(jajan_mingguan, reverse=True)
print(f"urutan uang dari besar:{urutan_jajan}")
print(f"urutan uang terbalik: {urutan_jajan_terbalik}")
# map() --> mentranformasi data
kurangi_uang = map(lambda uang: uang-67000, jajan_mingguan)
#list() mengudah data objek map menjadi list
list_kurangi_uang = list(kurangi_uang)
print(f"map uang berkurang: {list_kurangi_uang}")
# filter() menyaring/ mengfilter data
filter_banyak = filter(lambda uang: uang > 53000, jajan_mingguan)
list_jajan_banyak = list("53000")
print(f"filter jajan diatas 50rb:{list_jajan_banyak}")
