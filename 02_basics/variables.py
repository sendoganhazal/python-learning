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

#integers (int)
print("*** INTEGERS ***")

age = 34
student_quantity = 55000
degree = -5

print(age)
print(student_quantity)
print(degree)

#calculation

a = 10
b = 5

print("a:",a,", b:",b)

sum = a + b
print("a+b",sum)

multiplication = a * b
print("a*b",multiplication)

subtraction = a - b
print("a-b",subtraction)

division = a / b
print("a/b",division)

# There is a quantity of products and each product has a unit price. 
# I want to know the total cost of the products I bought.

product_quantity = 8
unit_price = 100

cost_of_product = product_quantity * unit_price

print("Quantity of Products:",product_quantity, ", Unit Price:", unit_price)
print("Cost of Product:", cost_of_product)


# Raise calculator app

unit_price = 250
print("unit price:", unit_price)

rate_of_rise = int(input("Write the rate_of_rise:"))
print("Rate of rise", rate_of_rise)

updated_price = unit_price + unit_price * rate_of_rise / 100
print("Updated price", updated_price)