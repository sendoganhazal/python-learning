"""
user defined (kullanıcı tanımlı) fonksiyonlar
    - kendi fonksiyonumuz
    - parametre
    - return
    - print vs return
    - birden fazla output
    - varsayılan ve keyword parametreleri
    - docstring nedir
"""

"""
fonksiyon tanımlama: def 

def fonksiyon_adi():
    kod_blok

"""

#Fonksiyon tanımlama (define)
def selam_ver() :
    print("Selam Dünyalı!")
    
#Fonksiyonu çağırma (call)
selam_ver()

# Parametre KUllanımı
def selam_ver(isim) :
    
    print(f"Selam, Ben {isim} Akıllı Asistanıyım!")

selam_ver("Trai Akademisi")
selam_ver("Ucanble")

# Birden Fazla Parametre Kullanımı
def selam_ver(isim, selamlama_cumlesi) : 
    print(f"{isim} {selamlama_cumlesi}")
    
selam_ver("Kaan Hoca","akıllı asistanı size merhaba diyor")

#Return kullanımı
def topla(a,b) :
    sonuc = a + b
    print(f"sonuc : {sonuc}")
    return sonuc

toplama_islemi_sonucu = topla(3,8)
print(f"toplama islemi sonucu: {toplama_islemi_sonucu}")

#birden fazla değer döndürme

def hesapla(x,y) :
    topla = x + y
    carp = x * y
    return topla,carp

hesapla_topla, hesapla_carp = hesapla(3,9)

print(f"hesapla_topla: {hesapla_topla}")
print(f"hesapla_carp: {hesapla_carp}")


