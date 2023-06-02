def toplama(sayi1, sayi2):
    return sayi1 + sayi2

def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def carpma(sayi1, sayi2):
    return sayi1 * sayi2

def bolme(sayi1, sayi2):
    if sayi2 != 0:
        return sayi1 / sayi2
    else:
        raise ValueError("Hatalı giriş. Bölme işleminde ikinci sayı sıfır olamaz.")

def hesap_makinesi():
    print("Hesap Makinesi")
    print("1 => Toplama")
    print("2 => Çıkarma")
    print("3 => Çarpma")
    print("4 => Bölme")

    while True:
        selected = input("İşleminizi hangi seçenekle yapmak istersiniz?\n")
        
        if selected in ("1", "2", "3", "4"):
            try:
                sayi1 = float(input("1. sayıyı girin: "))
                sayi2 = float(input("2. sayıyı girin: "))
            except ValueError:
                print("Hatalı giriş. Lütfen sayı girin.")
                continue
            
            if selected == "1":
                result = toplama(sayi1, sayi2)
                print("Cevap: ", int(result) if result.is_integer() else result)
            elif selected == "2":
                result = cikarma(sayi1, sayi2)
                print("Cevap: ", int(result) if result.is_integer() else result)
            elif selected == "3":
                result = carpma(sayi1, sayi2)
                print("Cevap: ", int(result) if result.is_integer() else result)
            elif selected == "4":
                try:
                    result = bolme(sayi1, sayi2)
                    print("Cevap: ", int(result) if result.is_integer() else result)
                except ValueError as e:
                    print(str(e))
        else:
            print("Geçersiz seçenek. Lütfen 1-4 arasında bir seçenek girin.")

hesap_makinesi()
