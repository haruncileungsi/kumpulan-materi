print("materi 08 function")
print("=================")

#. funcion di awali dengan keywort "def"
def hallo_ngab ():
    print("hello ngab")
    print("hello juga kak")

#. function dengan parmeter 'nama'
def sapa_sapa (nama) :
    print("hello kak", nama)
    print("apa kabar kak", nama)
    print("--------------------")

print("cobain fungsinya:")
hallo_ngab()
sapa_sapa("harun")
sapa_sapa("jihan")
sapa_sapa("dhita")

# fungsi luas persegi panjang
def luas_persegi_panjang (panjang, lebar):
    print("> panjang", panjang)
    print("> lebar", lebar)
    rumus = panjang - lebar
    print("luas persegi panjang =", rumus)

luas_persegi_panjang(30, 40)
luas_persegi_panjang(70, 90)