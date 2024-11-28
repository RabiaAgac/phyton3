sayiler=[1,2,3,4,5]
isimler=["ali","mehmet","ayşe"]
print(type(sayiler))

print(isimler[-3])
print(isimler[2])

ogrenci1=["Ali","yılmaz","2200000",60,50,70]
print(ogrenci1[0] + " " +ogrenci1[1])

ortalama=(ogrenci1[3]+ogrenci1[4]+ogrenci1[5])/3
print("Ortalamanız: " + str(ortalama))

ogrenciler = [["Ali","Yılmaz",60,50,70], ["Ayşe","Yılmaz",80,50,70]]

print(ogrenciler[0][0])
print(ogrenciler[1][0])



programlama_diller = ["Python","C#","Java","Javascript"]


sonuc = len(programlama_diller)
sonuc = programlama_diller + ["Go","Delphi"]

sonuc = "Python" in programlama_diller
sonuc = "React" in programlama_diller

del programlama_diller[0]

print(programlama_diller)



sehirler = ['izmir','istanbul']
plakalar = [35,34]

plakalar = {'kocaeli': 41, 'istanbul': 34,'izmir': 36 }

plakalar['izmir'] = 35


print(plakalar['kocaeli'])
print(plakalar['istanbul'])
print(plakalar['izmir'])