class öğrenci:
    def __init__(self, ad, soyad, cinsiyet,  notlar):
        self.ad = ad
        self.soyad = soyad
        self.cinsiyet = cinsiyet
        self.notlar = notlar
    

    def ortalama_not(self):
        return sum(self.notlar) / len(self.notlar)


    def __str__(self):
        return f" okulumuzun öğrencisi olan: {self.ad} {self.soyad}, Cinsiyet: {self.cinsiyet}, Notları: {self.notlar}"
        
insan = öğrenci("Eren", "Sönmez","Erkek", [80,75,62,76])
insan2 = öğrenci("buğra", "demir","Erkek", [85,66,94,12])
insan3 = öğrenci("burak", "taştemur","Kız", [14,26,87,96])


print(insan)
print(f"Ortalama Not: {insan.ortalama_not()}")

print(insan2)
print(f"Ortalama Not: {insan2.ortalama_not()}")

print(insan3)
print(f"Ortalama Not: {insan3.ortalama_not()}")


notlar = {
    'eren': [80,75,62,76],
    "buğra": [85,66,94,12],
    "burak" : [14,26,87,96]
}

def not_guncelle():
    print("Öğrenci Not Güncelleme Sistemi")
    ogrenci = input("Güncellemek istediğiniz öğrencinin adını girin: ")

    if ogrenci in notlar:
        print(f"{ogrenci}'nin mevcut notları: {notlar[ogrenci]}")
        yeni_not = input("Yeni notu girin (örnek: 85, 90, 78): gibi")
        
        not_listesi = [int(n) for n in yeni_not.split(',')]
        
        notlar[ogrenci] = not_listesi
        print(f"{ogrenci}'nin güncellenmiş notları: {notlar[ogrenci]}")

        ortalama = sum(notlar[ogrenci]) / len(notlar[ogrenci])
        print(f"{ogrenci}'nin güncellenmiş not ortalaması: {ortalama:.2f}")

    else:
        print("Bu isimde bir öğrenci bulunamadı.")


not_guncelle()
