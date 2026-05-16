from abc import ABC, abstractmethod


# Abstract Class
class Kaynak(ABC):
    def __init__(self, baslik, kayitNo):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, baslik):
        self._baslik = baslik

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, kayitNo):
        self._kayitNo = kayitNo

    def __str__(self):
        return f"Başlık: {self._baslik}, Kayıt No: {self._kayitNo}"


# Book Class
class Kitap(Kaynak):
    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    def __str__(self):
        return f"""
Kitap Adı: {self.baslik}
Kayıt No: {self.kayitNo}
Yazar: {self._yazar}
Sayfa Sayısı: {self._sayfa_sayisi}
"""


# Magazine Class
class Dergi(Kaynak):
    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)
        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no

    def __str__(self):
        return f"""
Dergi Adı: {self.baslik}
Kayıt No: {self.kayitNo}
Yayın Dönemi: {self._yayin_donemi}
Sayı No: {self._sayi_no}
"""


# Abstract Operation Class
class Islem(ABC):

    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass


# Book Operations
class KitapIslem(Islem):
    def __init__(self):
        self.kitaplar = []

    def ekle(self, kitap):
        for k in self.kitaplar:
            if k.kayitNo == kitap.kayitNo:
                print("Bu kayıt numarası zaten موجود!")
                return
        self.kitaplar.append(kitap)
        print("Kitap başarıyla eklendi.")

    def sil(self, kayitNo):
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                self.kitaplar.remove(kitap)
                print("Kitap silindi.")
                return
        print("Kitap bulunamadı.")

    def guncelle(self, kayitNo, yeni_baslik):
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                kitap.baslik = yeni_baslik
                print("Kitap güncellendi.")
                return
        print("Kitap bulunamadı.")

    def listele(self):
        if not self.kitaplar:
            print("Kayıt bulunamadı.")
        else:
            for kitap in self.kitaplar:
                print(kitap)


# Magazine Operations
class DergiIslem(Islem):
    def __init__(self):
        self.dergiler = []

    def ekle(self, dergi):
        for d in self.dergiler:
            if d.kayitNo == dergi.kayitNo:
                print("Bu kayıt numarası zaten mevcut!")
                return
        self.dergiler.append(dergi)
        print("Dergi başarıyla eklendi.")

    def sil(self, kayitNo):
        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                self.dergiler.remove(dergi)
                print("Dergi silindi.")
                return
        print("Dergi bulunamadı.")

    def guncelle(self, kayitNo, yeni_baslik):
        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                dergi.baslik = yeni_baslik
                print("Dergi güncellendi.")
                return
        print("Dergi bulunamadı.")

    def listele(self):
        if not self.dergiler:
            print("Kayıt bulunamadı.")
        else:
            for dergi in self.dergiler:
                print(dergi)


# Menu Class
class Menu:
    def __init__(self):
        self.kitap_islem = KitapIslem()
        self.dergi_islem = DergiIslem()

    def menu_goster(self):
        print("""
========= KÜTÜPHANE YÖNETİM SİSTEMİ =========

1- Kitap Ekle
2- Kitap Sil
3- Kitap Güncelle
4- Kitapları Listele
5- Dergi Ekle
6- Dergi Sil
7- Dergi Güncelle
8- Dergileri Listele
9- Çıkış
""")

    def calistir(self):

        while True:
            self.menu_goster()
            secim = input("Seçiminizi giriniz: ")

            if secim == "1":
                baslik = input("Kitap adı: ")
                kayitNo = input("Kayıt No: ")
                yazar = input("Yazar: ")
                sayfa = input("Sayfa Sayısı: ")

                kitap = Kitap(baslik, kayitNo, yazar, sayfa)
                self.kitap_islem.ekle(kitap)

            elif secim == "2":
                kayitNo = input("Silinecek kayıt no: ")
                self.kitap_islem.sil(kayitNo)

            elif secim == "3":
                kayitNo = input("Güncellenecek kayıt no: ")
                yeni_baslik = input("Yeni kitap adı: ")
                self.kitap_islem.guncelle(kayitNo, yeni_baslik)

            elif secim == "4":
                self.kitap_islem.listele()

            elif secim == "5":
                baslik = input("Dergi adı: ")
                kayitNo = input("Kayıt No: ")
                yayin = input("Yayın dönemi: ")
                sayi = input("Sayı No: ")

                dergi = Dergi(baslik, kayitNo, yayin, sayi)
                self.dergi_islem.ekle(dergi)

            elif secim == "6":
                kayitNo = input("Silinecek kayıt no: ")
                self.dergi_islem.sil(kayitNo)

            elif secim == "7":
                kayitNo = input("Güncellenecek kayıt no: ")
                yeni_baslik = input("Yeni dergi adı: ")
                self.dergi_islem.guncelle(kayitNo, yeni_baslik)

            elif secim == "8":
                self.dergi_islem.listele()

            elif secim == "9":
                print("Programdan çıkılıyor...")
                break

            else:
                print("Geçersiz seçim!")


# Main
menu = Menu()
menu.calistir()