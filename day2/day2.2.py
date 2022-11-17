#! Kullanıcının girdiği sayı kadar vize-final sınavları girilebilmesi beklenmektedir.
# ders sayısı gireceğiz ona göre her ders için 1 vize 1 final girilecek
# ve girilen vize final dersin ortalaması alınıp geçip kalınan
# ders sayısını bulmamız gerekli


ders_sayisi = int(input('ders sayısı giriniz: '))

temp=0

for i in range(1,ders_sayisi+1):
    
    vize = int(input(f'vize{i}: '))
    final = int(input(f'final{i}: '))
    ortalama = (vize*0.4)+(final*0.6)
    
    if (ortalama>=0) and (ortalama<=49):
        harf = 'FF'
    elif (ortalama>=50) and (ortalama<=59):
        harf = 'DD'
    elif (ortalama>=60) and (ortalama<=69):
        harf = 'CC'
    elif (ortalama>=70) and (ortalama<=79):
        harf = 'BB'
    elif (ortalama>=80) and (ortalama<=100):
        harf = 'AA'
    else:
        print('Hatalı girdiniz.')
    print(f"Not ortalaması: {ortalama}, Harf notu: {harf} ")
    
    if harf != 'FF':
        temp+=1

print(f"Geçilen ders sayısı: {temp} ")
print(f"Kalınan ders sayısı: {ders_sayisi-temp} ")