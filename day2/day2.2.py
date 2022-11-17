#! Kullanıcının girdiği sayı kadar vize-final sınavları girilebilmesi beklenmektedir.

vize_sayisi = int(input('vize sayısı giriniz: '))
final_sayisi = int(input('final sayısı giriniz: '))

vize_ort = 0
final_ort = 0

for i in range(1,vize_sayisi+1):
    vize_ort += float(input('vize'+str(i)+': '))


for i in range(1,final_sayisi+1):
    final_ort += float(input('final'+str(i)+': '))

print(f"Ortalama = {(vize_ort/vize_sayisi)*0.4 + (final_ort/final_sayisi)*0.6} ")