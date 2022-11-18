#bir şirket çalışanları verilerini tutan dosya tutulacak.
#kullanıcıdan çalışan sayısı alınacak
#çalışan sayısı kadar isim-soyisim-maaş bilgisi alınacak
#dosyadaki her satıra Ad Soyad - Maaş kalıbında çalışan bilgileri eklenecek.
#Programın sonunda dosyadan bilgileri satır satır okuyup listeleyecek kod yazılacak.

while True:

    try:
        calisan_sayisi = int(input('Calisan sayisi giriniz: '))
    except ValueError:
        print('Sayisal bir değer giriniz.')
    else:
        break

for i in range(1,calisan_sayisi+1):

    isim = input(f"{i}. calisan adi: ")
    soyisim = input(f"{i}. calisan soyadi: ")

    while True:

        try:
            maas = int(input(f"{i}. calisan maasi: "))
        except ValueError:
            print('Sayisal bir değer giriniz.')
        else:
            break
    
    f = open('ws2\employees.txt','a', encoding='utf-8')
    f.write(f"{isim} - {soyisim} - {maas} \n")
    f.close()
    
file1 = open('ws2\employees.txt', 'r')
lines = file1.readlines()

for line in lines:
    print(line)