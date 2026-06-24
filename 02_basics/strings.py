#strings
ad = "Hazal"
sirket = "Vivid"

bilgi = "Hazal'ın çalıştığı yer Vivid."
print(bilgi)

#String Concatenation

bilgi2 = ad + "'ın çalıştığı yer" + " " + sirket
print(bilgi2)

#Concatenation string and numbers
ad = "Camille"
yas = 11
int_to_str = str(yas)
# sonuc = ad + "'ın yaşı" + " " + yas #TypeError: can only concatenate str (not "int") to str
sonuc = ad + "'ın yaşı" + " " + int_to_str
print(sonuc)