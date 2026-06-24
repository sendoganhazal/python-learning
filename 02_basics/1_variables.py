"""
- Değişken Kavramı: veriyi saklamak için kullandığımız isimlendirilmiş bir alandır.
    - değişken = bilgiyi tuttuğumuz kutu
    - değişkenlerin isimlendirme kuralları:
        - rakamla başlanmaz: 1_var = 
        - boşluk içermer kaan hoca = 
        - özel karakter içermez önemli_değişken
        - büyük küçük harf duyarlıdır degisken ile Degisken aynı değildir neden çünkü d-D farklı harflerdir ve büyük-küçük harf duyarlılığı vardır.
- Integer: tam sayıları temsil eden değişken tipimiz. 
- float: ondalıklı sayıları temsil eder.
- string: metinsel verileri temsil eder
- Veri tipi kontrolü ve Tip dönüşümleri: bir değişkenin hangi veri tipinde olduğunu öğrenmek ve veri tipleri arasında dönüşüm yapmak
- liste: birden fazla veriyi tel bir değişken içerisinde saklamamızı sağlar
    - indeksleme ve slicing
    - list metotları
- tuple: birden fazla veriyi saklayan bir veri yapısıdır, tuple değiştirilemez.
- sözlük (dictionary): verileri anahtar-değer (key-value) mantığıyla saklar.
- set: benzersiz yani unique elemanlardan oluşan bir veri yapısıdır. Aynı elemandan birden fazla kez olamaz.
- veri yapıları arasındaki farklar: liste, tuple, sözlük, set
liste:
    - sıralıdır, değiştirilebilir, tekrar eden elemanlara izin verir
    - liste = [1, 2, 3]
    - kullanım: eleman sırası önemliyse, veri güncellenecekse
    - numpy array in temelini oluşturmaktadır

Tuple:
    - sıralıdır, değiştirilemez, tekrar eden elemanlara izin verir
    - tuple = (1, 2, 3, 4)    
    - kullanım: veri sabit kalacaksa, güvenli yapı gerekiyorsa

dictionary:
    - anahtar-değer (key-value pair)
    - anahtarlar benzersizdir
    - değerler tekrar edebilir
    - değiştirilebilir
    - ogrenci = {"isim":"kaan", "yas": 35}
    - anlamlı veri saklamak, etiketli veri tutmak
    - pandas dataframe temelini oluşturur

Set:
    - sırasızdır, tekrar eden elemanları kabul etmez, değiştirilebilir
    - set = {1, 2, 3, 4}
    - kullanım: tekrar eden değerleri temizlemek için, küme işlemleri yapmak için
"""