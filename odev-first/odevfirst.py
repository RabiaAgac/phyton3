#1
markalar=["Toyota", "Bmw" , "Renault" , "Mercedes"]

#2
print(len(markalar))

#3.1
print(markalar[0])

#3.2
print(markalar[3])

#4
markalar[2]="Togg"

#5
sonuc="Togg" in markalar
print(sonuc)

#6
print(markalar+["Ford","Citroen"])

#7
del(markalar[-1])
print(markalar)

#8
ogrenci1=["Yiğit", "Bilgi", 2010, [70, 80, 90]]
ogrenci2=["Ada", "Bilgi", 2011, [70, 70, 90]]
ogrenci3=["Çınar", "Turan", 2017, [60, 60, 90]]

#9
ogrenci1yas=2024-ogrenci1[2]
ogrenci2yas=2024-ogrenci2[2]
ogrenci3yas=2024-ogrenci3[2]
 
print(ogrenci1yas)
print(ogrenci2yas)
print(ogrenci3yas)

#10
ogrenci1ortalama=(ogrenci1[3][0] + ogrenci1[3][1] + ogrenci1[3][2])/3
ogrenci2ortalama=(ogrenci2[3][0] + ogrenci2[3][1] + ogrenci2[3][2])/3
ogrenci3ortalama=(ogrenci3[3][0] + ogrenci3[3][1] + ogrenci3[3][2])/3

print(ogrenci1ortalama)
print(ogrenci2ortalama)
print(ogrenci3ortalama)








