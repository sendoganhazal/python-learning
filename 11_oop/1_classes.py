"""
Class Nedir?    
    - bir nesnenin (object) nasıl olacağını tanımlayan bir şablondur.
    - class bir taslak yada plan gibidir
    - öğrenci:
        - isim, yaş, bmlüm 
        - ders çalışmak, sınava girmek 

Class tanımlama: Ogrenci > class ismi
class Ogrenci:
    pass
    
Class neden kullanırız?
    - kodun daha düzenli olması için
    - kod tekrarını azaltır
    - büyük projelerde yönetimi kolaylaştırır
    - scikit learn -> en önemli machine learning kütüphanesi -> LinearRegression() class tanımlamış olur.

Neler Öğreneceğiz?
    - __init__ metodu (initializer): nesne oluşturulduğunda otomatik olarak çalışan özel bir metottur. (kurucu metod)
    - attribute ve method
    - object oluşturma
    - Mini proje
"""

"""
Ogrenci class
    - isim
    - yaş
"""


class Ogrenci:
    def __init__(self, isim, yas):  # self = oluşturulan nesneyi temsil eder, isim ve yaş başlangıç parametrelerimiz
        print(f"Yeni bir öğrenci oluşturuluyor: {isim}, {yas}")

# nesne (object) oluşturma
ogrenci1 = Ogrenci("Hazal",20)

"""
Attribute bir class a veya nesneye ait özellikleri temsil eden değişkenlerdir.
yani bir nesnenin verilerini tutan yapılarıdır
Öğrenci:
    - isim, yaş ve bölüm: bunlar öğrencinin attribute larıdır.
"""

# attribute kullanımı
class Ogrenci:
    def __init__(self, isim, yas):
        self.isim = isim  # self.isim -> ogrenci1 nesnesinin isim attribute u
        self.yas = yas  # self.yas -> ogrenci1 nesnesinin yaş attribute u
        

# ogrenci1 nesnesinin attribute larına nasıl ulaşabiliriz?
ogrenci1 = Ogrenci("Hazal", 35)
print(f"Öğrenci ismi: {ogrenci1.isim}, Öğrenci yaşı: {ogrenci1.yas}")

"""
Metot (method): bir class içerisinde tanımlanan fonksiyonlardır
bir nesnenin yapabileceği işlemleri temsil ederler
"""


class Ogrenci:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        
    def tanit(self):  # self parametresi -> nesneyi temsil eder
        print(f"Merhaba, benim adım: {self.isim}")   

ogrenci1 = Ogrenci("Hazal", 35)
ogrenci1.tanit()  # ogrenci1 nesnesinin tanit metodunu çağırıyoruz
ogrenci2 = Ogrenci("Kaan", 25)
ogrenci2.tanit()  # ogrenci2 nesnesinin tanit metodunu çağırıyoruz

"""
Object oluşturma ve class kullanımı
    - class: şablon -> araba
    - object (nesne): şablondan üretilen yapı (mercedes, audi)

"""


# attribute değerlerine erişim


# method

"""
Kitap: Python programlama
Yazar: Kaan
Sayfa sayısı: 500
"""

# birden fazla obje oluşturma
