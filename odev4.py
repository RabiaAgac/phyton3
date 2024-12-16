# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def selamlama():
    for i in range(13):
         print("hoşgeldiniz")


selamlama()


# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

#dikdörtgen çevre

def çevre():
     a=10
     b=20
     print(2*(a+b))

çevre()

#dikdörtgen alan

def alan():
     a=10
     b=20
     print(a*b)

alan()


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)

import random

def yazi_tura():
    
    sonuc = random.choice(["Yazı", "Tura"])
    return sonuc
print(yazi_tura()) 

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
sayi1=int(input("1. aralığı girirniz: "))
sayi2=int(input("2. aralığı giriniz: "))
print(sayi1,"ile",sayi2,"aralarındaki asal sayılar; ")
for i in range(sayi1,sayi2+1):
     if i>1:
          for j in range(2,i):
               if i%j==0:
                    break
               else:
                   print(i)
               

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
sayi=21
def tamBolen(sayi):
    return [i for i in range(1, sayi + 1) if sayi % i == 0]
print(tamBolen(sayi))
