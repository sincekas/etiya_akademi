"""3 adet sayısal değişken tanımlayınız.

Bu sayılardan en büyük ve en küçük olanı ekrana ayrı ayrı yazdırınız.

Bu ödev ile ilgili sorular ;
1-Farklı kombinasyonlar yaptığınızda doğru sonuca ulaştınız mı? -Evet"""

sayi1 = 8
sayi2 = 7
sayi3 = 9

if (sayi1>sayi2) and (sayi1>sayi3):
    print(f"En buyuk sayi:{sayi1} ")
    if sayi2>sayi3:
        print(f"En kucuk sayi:{sayi3} ")
    else:
        print(f"En kucuk sayi:{sayi2} ")

if (sayi2>sayi1) and (sayi2>sayi3):
    print(f"En buyuk sayi:{sayi2} ")
    if sayi1>sayi3:
        print(f"En kucuk sayi:{sayi3} ")
    else:
        print(f"En kucuk sayi:{sayi1} ")

if (sayi3>sayi1) and (sayi3>sayi2):
    print(f"En buyuk sayi:{sayi3} ")
    if sayi1>sayi2:
        print(f"En kucuk sayi:{sayi2} ")
    else:
        print(f"En kucuk sayi:{sayi1} ")