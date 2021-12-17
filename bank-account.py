hesapA ={
    "ad":"ilyas Türkmen",
    "hesapNo":"13245678",
    "bakiye":3000,
    "ekHesap":2000
}

hesapB ={
    "ad":"Ali Türkmen",
    "hesapNo":"12345678",
    "bakiye":2000,
    "ekHesap":1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap["bakiye"] >=miktar:
        print("paranizi alabilirsiniz")
    else:
        toplam =hesap["bakiye"]+hesap["ekHesap"]

        if (toplam >=miktar):
            ekHesapKullanimi = input("ek hesap kullanilsin mi (evet/hayır)")

            if ekHesapKullanimi == "evet":
                print("paranizi alabilirsiniz")
            else:
                print(f"{hesap['hesapNo']} nolu hesabanizda {hesap['bakiye']} bulunmaktadır")

        else:
            print("üzgünüz bakiye yetersiz")

paraCek(hesapA,2000)
