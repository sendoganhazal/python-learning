"""
Dosya işlemleri: 
    - dosyadan veri okuma
    - okunan verinin işlenmesi
    - dosyaya veri yazma veya keydetme
    - with yapısı

Neden dosya işlemleri yapıyoruz?
    - yapay zeka veriden öğrenir, veriyi python ortamına yüklememiz ve işlememiz lazım bu nedenle dosya işlemlerinin mantığını öğrenicez

Dosya: verinin kalıcı olarak saklandığı yapılar.
    - kullanıcı listeleri
    - not kayıtları
    - log dosyaları
    - csv veri dosyaları
"""

# dosya açma ve okuma
# "r" = read -> okuma modu
dosya = open("ornek.txt","r", encoding = "UTF-8")

icerik = dosya.read() #tüm dosyayı okur

print(f"Dosya İçeriği: {icerik}")

dosya.close() # dosyayı kapar

#satır satır okuma
dosya = open("ornek.txt","r", encoding="UTF-8")

for satir in dosya:
    
    print(f"Satır: {satir.strip()}") # strip() -> satır sonundaki boşlukları temizler

dosya.close()