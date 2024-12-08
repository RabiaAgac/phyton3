sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.
for x in sayilar:
    print(x)

# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?
ucun_katlari= [sayi for sayi in sayilar if sayi % 3 == 0]
print("3'ün katı olan sayılar:", ucun_katlari)

# 3- "sayilar" listesinde tüm sayıların toplamı nedir?

toplam =(3+5+7+2+12+32+45)
print("Sayıların toplamı:", toplam)


# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (index ve find komutlarından faydalanınız.)
urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]
iphone_urunleri = []
for urun in urunler:
    if urun.find("iphone") != -1:
        iphone_urunleri.append(urun)

print("iPhone ürünleri:", iphone_urunleri)

# 5- "urunler" listesinde kaç adet samsung ürünü vardır? (find metodu)
urun.find("samsung")
samsung_sayisi=sum(1 for urun in urunler 
    if urun.find("samsung") != -1)
print("Samsung ürün sayısı:", samsung_sayisi)