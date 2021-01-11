# coding=utf-8
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sys
import sqlite3

conn = sqlite3.connect("veritabani.db") # VERITABANI OLUSTURMA
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Student
    (
        FirsName TEXT,
        LastName TEXT,
        No TEXT,
        Password TEXT
    )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Teacher
    (
        FirsName TEXT,
        LastName TEXT,
        No TEXT,
        Password TEXT,
        GivenLesson TEXT
    )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Lesson
    (
        No TEXT,
        LesCode TEXT,
        IsComp TEXT,
        AKTS INT,
        Note TEXT
    )""")
conn.commit()

class GUI():
    def __init__(self, root):   #BUTUN WIDGETLARI TEK BIR YERDE TOPLAYIP, ISIME YARAYANLARINI BELLI EKRANLARDA AKTIFLESTIREREK KULLANACAGIM.
        self.root = root
        self.root.iconbitmap(".//images//00 - denemeicon.ico")
        self.root.geometry("800x600+100+50")
        self.root.resizable(0, 0)
        
        global anaBG
        anaBG = ImageTk.PhotoImage(Image.open(".//images//01 - bg.png"))
        self.bgLabel1 = Label(image=anaBG)
        global anaBG2
        anaBG2 = ImageTk.PhotoImage(Image.open(".//images//01.1 - bg.png"))
        self.bgLabel2 = Label(image=anaBG2)
        global ogrenciBG
        ogrenciBG = ImageTk.PhotoImage(Image.open(".//images//02 - ogrenci ekrani.png"))
        self.bgLabel3 = Label(image=ogrenciBG)
        global ogretmenBG
        ogretmenBG = ImageTk.PhotoImage(Image.open(".//images//03 - ogretmen ekrani.png"))
        self.bgLabel4 = Label(image=ogretmenBG)
        
        self.ogrenciButonu = Button(root, text="Öğrenci", width=15, height=2, command=self.Ogrenci) # BUTONLAR VE ISLEVLERI
        self.ogretmenButonu = Button(root, text="Öğretmen", width=15, height=2, command=self.Ogretmen)
        self.ogrenciGirisYapButonu = Button(root, text="Giriş yap", bg="LightCyan2", width=35, height=3, command=self.ogrenciGirisi)
        self.ogretmenGirisYapButonu = Button(root, text="Giriş yap", bg="LightCyan2", width=35, height=3, command=self.ogretmenGirisi)
        self.ogrenciKayitOlButonu = Button(root, text="Kayıt ol", bg="AntiqueWhite1", width=35, height=3, command=self.ogrenciKayitOl)
        self.ogrenciKayitTamamlaButonu = Button(root, text="Kayıt ol", bg="AntiqueWhite1", width=35, height=3, command=self.ogrenciKayitTamamla)
        self.ogretmenKayitOlButonu = Button(root, text="Kayıt ol", bg="AntiqueWhite1", width=35, height=3, command=self.ogretmenKayitOl)
        self.ogretmenKayitTamamlaButonu = Button(root, text="Kayıt ol", bg="AntiqueWhite1", width=35, height=3, command=self.ogretmenKayitTamamla)
        self.anaMenuButonu = Button(root, text="Ana Menü", width=15, height=2, command=self.anaMenu)
        self.dersSecimiButonu = Button(root, text="Ders Seçimi", width=20, height=2, command=self.dersSecimi)
        self.dersProgramiButonu = Button(root, text="Ders Programı", width=20, height=2, command=self.dersProgrami)
        self.sinavOlusturButonu = Button(root, text="Sınav Oluştur", width=20, height=2, command=self.sinavOlustur)
        self.sinavOlusturButonu2 = Button(root, text="Sınav Oluştur", width=20, height=2, command=self.sinavOlusturma)
        self.dersSecimiOnayButonu = Button(root, text="Onayla", width=15, height=2, command=self.dersSecimiOnayla)

        self.ogrnIsimLabel = Label(root, text="Ad", font="kalam 12 bold")   # LABELLAR, TEXTBOXLAR, COMBOBOXLAR...
        self.ogrnIsim = StringVar()
        self.ogrnIsimGirisi = Entry(root, textvariable=self.ogrnIsim)
        self.ogrtIsimLabel = Label(root, text="Ad", font="kalam 12 bold")
        self.ogrtIsim = StringVar()
        self.ogrtIsimGirisi = Entry(root, textvariable=self.ogrtIsim)

        self.ogrnSoyisimLabel = Label(root, text="Soyad", font="kalam 12 bold")
        self.ogrnSoyisim = StringVar()
        self.ogrnSoyisimGirisi = Entry(root, textvariable=self.ogrnSoyisim)
        self.ogrtSoyisimLabel = Label(root, text="Soyad", font="kalam 12 bold")
        self.ogrtSoyisim = StringVar()
        self.ogrtSoyisimGirisi = Entry(root, textvariable=self.ogrtSoyisim)
        
        self.ogrnNumaraLabel = Label(root, text="Okul Numarası", font="kalam 12 bold")
        self.ogrnNumara = StringVar()
        self.ogrnNumaraGirisi = Entry(root, textvariable=self.ogrnNumara)
        self.ogrtNumaraLabel = Label(root, text="Okul Numarası", font="kalam 12 bold")
        self.ogrtNumara = StringVar()
        self.ogrtNumaraGirisi = Entry(root, textvariable=self.ogrtNumara)
        
        self.ogrnSifreLabel = Label(root, text="Şifre", font="kalam 12 bold")
        self.ogrnSifre = StringVar()
        self.ogrnSifreGirisi = Entry(root, textvariable=self.ogrnSifre, show="*")
        self.ogrtSifreLabel = Label(root, text="Şifre", font="kalam 12 bold")
        self.ogrtSifre = StringVar()
        self.ogrtSifreGirisi = Entry(root, textvariable=self.ogrtSifre, show="*")


        derslerList = []
        data=cursor.execute("""select DersAdi from Bilgisayar_Muhendisligi""")  # DB'DEKI TUM DERSLERIN LISTESI
        for i in data:
            derslerList.append(i[0])
            
        self.ogrtVerdigiDersLabel = Label(root, text="Verilen Ders", font="kalam 12 bold")
        self.ogrtVerdigiDersCombo = ttk.Combobox(root, width=35, values=(derslerList))

        self.ders01Label = Label(root, text="Ders 01", font="kalam 12 bold")    # DERS SECIMI ICIN KULLANILACAK COMBOBOXLAR.
        self.ders01Combo = ttk.Combobox(root, width=35, values=(derslerList))
        self.ders02Label = Label(root, text="Ders 02", font="kalam 12 bold")
        self.ders02Combo = ttk.Combobox(root, width=35, values=(derslerList))
        self.ders03Label = Label(root, text="Ders 03", font="kalam 12 bold")
        self.ders03Combo = ttk.Combobox(root, width=35, values=(derslerList))
        self.ders04Label = Label(root, text="Ders 04", font="kalam 12 bold")
        self.ders04Combo = ttk.Combobox(root, width=35, values=(derslerList))
        self.ders05Label = Label(root, text="Ders 05", font="kalam 12 bold")
        self.ders05Combo = ttk.Combobox(root, width=35, values=(derslerList))
        self.ders06Label = Label(root, text="Ders 06", font="kalam 12 bold")
        self.ders06Combo = ttk.Combobox(root, width=35, values=(derslerList))
        self.ders07Label = Label(root, text="Ders 07", font="kalam 12 bold")
        self.ders07Combo = ttk.Combobox(root, width=35, values=(derslerList))
        self.ders08Label = Label(root, text="Ders 08", font="kalam 12 bold")
        self.ders08Combo = ttk.Combobox(root, width=35, values=(derslerList))
        self.ders09Label = Label(root, text="Ders 09", font="kalam 12 bold")
        self.ders09Combo = ttk.Combobox(root, width=35, values=(derslerList))
        self.ders10Label = Label(root, text="Ders 10", font="kalam 12 bold")
        self.ders10Combo = ttk.Combobox(root, width=35, values=(derslerList))

        self.sinavTarihiLabel = Label(root, text="Sınav Tarihi", font="kalam 12 bold")
        self.tarihGun = ttk.Combobox(root, width=2, values=("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"))
        self.tarihAy = ttk.Combobox(root, width=2, values=("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"))
        self.tarihYil = ttk.Combobox(root, width=4, values=("2020", "2021"))

        self.sinavBaslangicSaatiLabel = Label(root, text="Sınav Başlangıç Saati", font="kalam 12 bold")
        self.baslSa = ttk.Combobox(root, width=2, values=("08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18"))
        self.baslDk = ttk.Combobox(root, width=2, values=("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"))

        self.sinavBitisSaatiLabel = Label(root, text="Sınav Bitiş Saati", font="kalam 12 bold")
        self.bitSa = ttk.Combobox(root, width=2, values=("08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"))
        self.bitDk = ttk.Combobox(root, width=2, values=("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"))
        # Buraya kadar olan kisim tum widgetleri iceriyor. Hangi ekranda hangisinin kullanilacagi asagidaki fonksiyonlarla saglandi. Su anda hepsi devre disi, ekranlarda gecis yaptikca bir kismi aktif ediliyor, bir kismi devre disi birakiliyor gibi dusunebilirsin.
        
        self.anaMenu()


    def anaMenu(self):  # Ana ekran.
        self.root.title("MUDSS")
        self.ekraniTemizle()
        self.bgLabel1.pack()
        self.ogrenciButonu.place(x=196, y=400, anchor=W)
        self.ogretmenButonu.place(x=479, y=400, anchor=W)
        

    def Ogrenci(self):  # Ana menuden ogrenci secilirse cikacak ekran.
        self.root.title("Öğrenci - MUDSS")
        self.ekraniTemizle()
        self.bgLabel2.pack()

        self.ogrenciGirisYapButonu.place(x=265, y=285)
        self.ogrenciKayitOlButonu.place(x=265, y=350)
        self.anaMenuButonu.place(x=337, y=500)
        
        self.ogrnNumaraLabel.place(x=265, y=196)
        self.ogrnSifreLabel.place(x=265, y=246)
        
        self.ogrnNumaraGirisi.place(x=397, y=200)
        self.ogrnSifreGirisi.place(x=397, y=250)
    def Ogretmen(self): # Ana menuden ogretmen secilirse cikacak ekran.
        self.root.title("Öğretmen - MUDSS")
        self.ekraniTemizle()
        self.bgLabel2.pack()

        self.ogretmenGirisYapButonu.place(x=265, y=285)
        self.ogretmenKayitOlButonu.place(x=265, y=350)
        self.anaMenuButonu.place(x=337, y=500)
        
        self.ogrtNumaraLabel.place(x=265, y=196)
        self.ogrtSifreLabel.place(x=265, y=246)
        
        self.ogrtNumaraGirisi.place(x=397, y=200)
        self.ogrtSifreGirisi.place(x=397, y=250)


    def ogrenciGirisi(self):    # Ogrenci giris yapma ekrani.
        ogrnBul = ("SELECT * FROM Student WHERE No=? AND Password=?")
        cursor.execute(ogrnBul, [(self.ogrnNumara.get()), (self.ogrnSifre.get())])  # NUMARA VE SIFRE DB'DE VARSA (KAYITLIYSA) GIRISE IZIN VERILIR.
        sonuclar = cursor.fetchall()
        if sonuclar:
            for i in sonuclar:
                global No
                No = self.ogrnNumara.get()
                print(No, " numarali kullanici giris yapti.")
                self.ekraniTemizle()
                self.bgLabel3.pack()
                self.dersSecimiButonu.place(x=194, y=400, anchor=W)
                self.dersProgramiButonu.place(x=443, y=400, anchor=W)
                self.anaMenuButonu.place(x=337, y=500)
        else:
            messagebox.showerror("", "Numaranız veya şifreniz yanlış!") # DEGILSE IZIN VERILMEZ.
    def ogretmenGirisi(self):   # Ogretmen giris yapma ekrani.
        ogrtBul = ("SELECT * FROM Teacher WHERE No=? AND Password=?")
        cursor.execute(ogrtBul, [(self.ogrtNumara.get()), (self.ogrtSifre.get())])
        sonuclar = cursor.fetchall()
        if sonuclar:
            for i in sonuclar:
                global NoT
                NoT=self.ogrtNumara.get()
                self.ekraniTemizle()
                self.bgLabel4.pack()
                self.sinavOlusturButonu.place(x=194, y=400, anchor=W)
                self.dersProgramiButonu.place(x=443, y=400, anchor=W)
                self.anaMenuButonu.place(x=337, y=500)
        else:
            messagebox.showerror("", "Numaranız veya şifreniz yanlış!")


    def dersSecimi(self):   # Ders secimi butonu tiklandiginda bu ekrana girilecek. Bu ekranda ogrencinin bilgilerine gore hangi sinifta oldugu databaseden ogrenilip mufredatta kendisine uygun dersler listelenecek.
        print(No, "numarali kullanici ders programi olusturdu.")
        self.ekraniTemizle()
        self.bgLabel2.pack()
        self.ders01Label.place(x=220, y=65)
        self.ders01Combo.place(x=300, y=66)
        self.ders02Label.place(x=220, y=105)
        self.ders02Combo.place(x=300, y=106)
        self.ders03Label.place(x=220, y=145)
        self.ders03Combo.place(x=300, y=146)
        self.ders04Label.place(x=220, y=185)
        self.ders04Combo.place(x=300, y=186)
        self.ders05Label.place(x=220, y=225)
        self.ders05Combo.place(x=300, y=226)
        self.ders06Label.place(x=220, y=265)
        self.ders06Combo.place(x=300, y=266)
        self.ders07Label.place(x=220, y=305)
        self.ders07Combo.place(x=300, y=306)
        self.ders08Label.place(x=220, y=345)
        self.ders08Combo.place(x=300, y=346)
        self.ders09Label.place(x=220, y=385)
        self.ders09Combo.place(x=300, y=386)
        self.ders10Label.place(x=220, y=425)
        self.ders10Combo.place(x=300, y=426)
        self.dersSecimiOnayButonu.place(x=340, y=475)
        conn.commit()
    def dersSecimiOnayla(self):
        data=cursor.execute("select * from Bilgisayar_Muhendisligi")
        secilenDersler = [self.ders01Combo.get(), self.ders02Combo.get(), self.ders03Combo.get(), self.ders04Combo.get(), self.ders05Combo.get(), self.ders06Combo.get(), self.ders07Combo.get(), self.ders08Combo.get(), self.ders09Combo.get(), self.ders10Combo.get()]
        top=int(0)  # DERS SECIMINDE 30 KREDI ASILIRSA PROGRAM HATA VERECEK.
        for k in data:
            if(secilenDersler.count(int(k[2]))!=0):
                    top+=int(k[2])
        if(top>30):
            self.Cikis()
        for i in range(10):
            for j in range(i+1,10):
                if secilenDersler[j] != "":
                    if secilenDersler[i] == secilenDersler[j]:
                        messagebox.showerror("", "Lütfen aynı dersi birden fazla kez girmeyiniz.")
                        break
                    else:
                        continue
                else:
                    self.Cikis()
        self.ekraniTemizle()
        self.anaMenu()
        messagebox.showinfo("", "Ders seçimi tamamlandı!")
    def dersProgrami(self): # Ders secimi yapildiktan sonra ders programi olusturulacak. Yazdigin fonksiyonu direkt burada calistirabilirsin.
        print("Ders programı oluşturuldu.")
        dersler=[]
        atanmis=[]
        data=cursor.execute("""select * from Lesson""")
        for i in data:
            if(i[0]==No and i[2]==0):
                dersler.append(i[1])
        data=cursor.execute("""select * from Bilgisayar_Muhendisligi""")
        
        saatvegun=[[9,10,11,12,13,14,15,16,17],[9,10,11,12,13,14,15,16,17],[9,10,11,12,13,14,15,16,17],
                   [9,10,11,12,13,14,15,16,17],[9,10,11,12,13,14,15,16,17]]#0,0 indexi pazartesi saat 9:00-10:00...
        for i in data:
            if(dersler.count(i[0])!=0):
                kredi=int(i[2])
                for j in range(kredi):
                    atanmis.append([i[1],randomGunSaat(saatvegun)])
        for a in range(len(atanmis)-1):
            for i in range(len(atanmis)-1):
                if(atanmis[i+1][1][0]<atanmis[i][1][0]):
                    current=atanmis[i+1]
                    atanmis[i+1]=atanmis[i]
                    atanmis[i]=current
        for k in range(len(atanmis)-1):
            for j in range(len(atanmis)-1):
                if(atanmis[j+1][1][0]==atanmis[j][1][0] and atanmis[j+1][1][1]<atanmis[j][1][1]):
                    current2=v[j+1]
                    atanmis[j+1]=atanmis[j]
                    atanmis[j]=current2
        try:
            dosya = open(No+"_dersprogrami.txt","w")
        except FileNotFoundError:
            print("Dosya Acilamadi!")
            time.sleep(0.5)
            exit()
        for i in range(len(atanmis)-1):
            dosya.write(str(atanmis[i][0])+" "+StringeCevir(atanmis[i][1][0],atanmis[i][1][1])+"\n")
        dosya.close()

    def StringeCevir(gun,saat): # INT OLARAK RASTGELE BELIRLENMIS GUN VE SAATLER STRING'E DONUSTURULUYOR.
        donus=""
        if(gun==0):
            donus+="Pazartesi, "
        elif(gun==1):
            donus+="Sali, "
        elif(gun==2):
            donus+="Carsamba, "
        elif(gun==3):
            donus+="Persembe, "
        elif(gun==4):
            donus+="Cuma, "
        if(saat==9):
            donus+="Saat 9:00-10:00"
        elif(saat==10):
            donus+="Saat 10:00-11:00"
        elif(saat==11):
            donus+="Saat 11:00-12:00"
        elif(saat==12):
            donus+="Saat 12:00-13:00"
        elif(saat==13):
            donus+="Saat 13:00-14:00"
        elif(saat==14):
            donus+="Saat 14:00-15:00"
        elif(saat==15):
            donus+="Saat 15:00-16:00"
        elif(saat==16):
            donus+="Saat 16:00-17:00"
        elif(saat==17):
            donus+="Saat 17:00-18:00"
        return donus
        
    def sinavOlustur(self): # Her hocanin bir dersi var. Sinav olusturmaya tikladiginda bu ekran karsisina cikacak.
        self.ekraniTemizle()
        self.bgLabel2.pack()
        self.sinavTarihiLabel.place(x=200, y=225)
        self.tarihGun.place(x=420, y=225)
        self.tarihAy.place(x=460, y=225)
        self.tarihYil.place(x=500, y=225)
        self.sinavBaslangicSaatiLabel.place(x=200, y=275)
        self.baslSa.place(x=420, y=275)
        self.baslDk.place(x=460, y=275)
        self.sinavBitisSaatiLabel.place(x=200, y=325)
        self.bitSa.place(x=420, y=325)
        self.bitDk.place(x=460, y=325)
        self.sinavOlusturButonu2.place(x=318, y=375)
        self.anaMenuButonu.place(x=337, y=500)
    def sinavOlusturma(self):   # Sinav olusturma ekranindaki bilgiler girildikten sonra "Sinav Olustur" butonuna basilinca cikan ekran.
        if self.tarihGun.get() == "" or self.tarihAy.get() == "" or self.tarihYil.get() == "" or self.baslSa.get() == "" or self.baslDk.get() == "" or self.bitSa.get() == "" or self.bitDk.get() == "":
            messagebox.showerror("", "Lütfen boş kutucukları doldurunuz!")  # BOSLUK ISTENMIYOR.
        elif (self.tarihAy.get() == "02" and self.tarihYil.get() == "2020" and int(self.tarihGun.get())>29) or (self.tarihAy.get() == "02" and self.tarihYil.get() == "2021" and int(self.tarihGun.get())>28) or (self.tarihAy.get() == "04" and int(self.tarihGun.get())>30) or (self.tarihAy.get() == "06" and int(self.tarihGun.get())>30) or (self.tarihAy.get() == "09" and int(self.tarihGun.get())>30) or (self.tarihAy.get() == "11" and int(self.tarihGun.get())>30):
            messagebox.showerror("", "Geçersiz bir tarih girişi yaptınız!") # 29 SUBAT 2021 GIBI TARIHLER KABUL EDILMEYECEK.
            self.sinavOlustur()
        else:
            tarih = self.tarihGun.get()+"/"+self.tarihAy.get()+"/"+self.tarihYil.get()
            baslangicSaati = self.baslSa.get()+"."+self.baslDk.get()
            bitisSaati = self.bitSa.get()+"."+self.bitDk.get()
            ogrtBul = ()
            cursor.execute(("SELECT * FROM Teacher WHERE No=?"), [NoT])
            sonuc = cursor.fetchall()   # TEST BILGILERI GIRILDIKTEN SONRA DB'YE KAYDEDILECEK.
            cursor.execute("insert into Test values('%s', '%s', '%s', '%s')"%(sonuc[4], tarih, baslangicSaati, bitisSaati))
            conn.commit()
            
    def ogrenciKayitOl(self):# Ogrenci kayit olma butonuna tikladigi zaman karsisina gelen kaydolma ekrani
        self.root.title("Kayıt Ol (Öğrenci)")
        self.ekraniTemizle()
        self.bgLabel2.pack()

        self.ogrnNumaraGirisi.delete(0, END)
        self.ogrnSifreGirisi.delete(0, END)

        self.ogrenciKayitTamamlaButonu.place(x=265, y=375)
        self.anaMenuButonu.place(x=337, y=500)

        self.ogrnIsimLabel.place(x=265, y=166)
        self.ogrnSoyisimLabel.place(x=265, y=216)
        self.ogrnNumaraLabel.place(x=265, y=266)
        self.ogrnSifreLabel.place(x=265, y=316)
        
        self.ogrnIsimGirisi.place(x=397, y=170)
        self.ogrnSoyisimGirisi.place(x=397, y=220)
        self.ogrnNumaraGirisi.place(x=397, y=270)
        self.ogrnSifreGirisi.place(x=397, y=320)
    def ogretmenKayitOl(self):  # Aynisi ogretmenler icin
        self.root.title("Kayıt Ol (Öğretmen)")
        self.ekraniTemizle()
        self.bgLabel2.pack()

        self.ogretmenKayitTamamlaButonu.place(x=265, y=390)
        self.anaMenuButonu.place(x=337, y=500)

        self.ogrtIsimLabel.place(x=200, y=136)
        self.ogrtSoyisimLabel.place(x=200, y=186)
        self.ogrtNumaraLabel.place(x=200, y=236)
        self.ogrtSifreLabel.place(x=200, y=286)
        self.ogrtVerdigiDersLabel.place(x=200, y=336)

        self.ogrtIsimGirisi.place(x=467, y=140)
        self.ogrtSoyisimGirisi.place(x=467, y=190)
        self.ogrtNumaraGirisi.place(x=467, y=240)
        self.ogrtSifreGirisi.place(x=467, y=290)
        self.ogrtVerdigiDersCombo.place(x=360, y=340)


    def ogrenciKayitTamamla(self):  # Kaydolma ekranindaki bilgiler girildikten sonra "kayit ol" butonuna tiklanmasi sonucu bilgileri databaseye giren fonksiyon.
        if self.ogrnIsimGirisi.get()=="" or self.ogrnNumaraGirisi.get()=="" or self.ogrnSoyisimGirisi.get()=="" or self.ogrnSifreGirisi.get()=="":
            messagebox.showerror("", "Lütfen bütün bilgileri eksiksiz giriniz.")
        else:
            cursor.execute("insert into Student values('%s', '%s', '%s', '%s')"%(self.ogrnIsim.get(), self.ogrnSoyisim.get(), self.ogrnNumara.get(), self.ogrnSifre.get()))
            conn.commit()
            print("Öğrenci kaydı tamamlandı!\n\nAdı:", self.ogrnIsimGirisi.get(), "\nSoyadı:", self.ogrnSoyisim.get(), "\nNumara:", self.ogrnNumaraGirisi.get(), "\nŞifre:", self.ogrnSifreGirisi.get())                   
            messagebox.showinfo("", "Kayıt işleminiz tamamlandı!")
    def ogretmenKayitTamamla(self): # Aynisi ogretmenler icin.
        if self.ogrtIsimGirisi.get()=="" or self.ogrtSoyisimGirisi.get()=="" or self.ogrtNumaraGirisi.get()=="" or self.ogrtSifreGirisi.get()=="" or self.ogrtVerdigiDersCombo.get()=="":
            messagebox.showerror("", "Lütfen bütün bilgileri eksiksiz giriniz.")
        else:
            cursor.execute("insert into Teacher values('%s', '%s', '%s', '%s', '%s')"%(self.ogrtIsim.get(), self.ogrtSoyisim.get(), self.ogrtNumara.get(), self.ogrtSifre.get(), self.ogrtVerdigiDersCombo.get()))
            conn.commit()
            print("Öğretmen kaydı tamamlandı!\n\nAdı:", self.ogrtIsimGirisi.get(), "\nSoyadı:", self.ogrtSoyisimGirisi.get(), "\nNumara:", self.ogrtNumaraGirisi.get(), "\nŞifre:", self.ogrtSifreGirisi.get(), "\nVerdiği Ders:", self.ogrtVerdigiDersCombo.get())
            messagebox.showinfo("", "Kayıt işleminiz tamamlandı!")


    def ekraniTemizle(self):    # Ekranlarda gecis yaparken widgetlari TEK TEK devre disi birakmamak (gizlemek) icin GUI'deki butun widgetlari silen fonksiyon.
        self.bgLabel1.pack_forget()
        self.bgLabel2.pack_forget()
        self.bgLabel3.pack_forget()
        self.bgLabel4.pack_forget()
        
        self.ogrenciButonu.place_forget()
        self.ogretmenButonu.place_forget()
        self.ogrenciGirisYapButonu.place_forget()
        self.ogretmenGirisYapButonu.place_forget()
        self.ogrenciKayitOlButonu.place_forget()
        self.ogrenciKayitTamamlaButonu.place_forget()
        self.ogretmenKayitOlButonu.place_forget()
        self.ogretmenKayitTamamlaButonu.place_forget()
        self.anaMenuButonu.place_forget()
        self.dersSecimiButonu.place_forget()
        self.dersProgramiButonu.place_forget()
        self.sinavOlusturButonu.place_forget()
        self.sinavOlusturButonu2.place_forget()
        self.dersSecimiOnayButonu.place_forget()
        
        self.ogrnIsimLabel.place_forget()
        self.ogrnSoyisimLabel.place_forget()
        self.ogrnNumaraLabel.place_forget()
        self.ogrtIsimLabel.place_forget()
        self.ogrtSoyisimLabel.place_forget()
        self.ogrtNumaraLabel.place_forget()
        self.ogrnSifreLabel.place_forget()
        self.ogrtSifreLabel.place_forget()
        self.ogrtVerdigiDersLabel.place_forget()
        self.sinavTarihiLabel.place_forget()
        self.sinavBaslangicSaatiLabel.place_forget()
        self.sinavBitisSaatiLabel.place_forget()
        self.ders01Label.place_forget()
        self.ders02Label.place_forget()
        self.ders03Label.place_forget()
        self.ders04Label.place_forget()
        self.ders05Label.place_forget()
        self.ders06Label.place_forget()
        self.ders07Label.place_forget()
        self.ders08Label.place_forget()
        self.ders09Label.place_forget()
        self.ders10Label.place_forget()

        self.ogrnIsimGirisi.delete(0, END)
        self.ogrtIsimGirisi.delete(0, END)
        self.ogrnSoyisimGirisi.delete(0, END)
        self.ogrtSoyisimGirisi.delete(0, END)
        self.ogrnNumaraGirisi.delete(0, END)
        self.ogrtNumaraGirisi.delete(0, END)
        self.ogrnSifreGirisi.delete(0, END)
        self.ogrtSifreGirisi.delete(0, END)
        self.ogrtVerdigiDersCombo.delete(0, END)
        self.tarihGun.delete(0, END)
        self.tarihAy.delete(0, END)
        self.tarihYil.delete(0, END)
        self.baslSa.delete(0, END)
        self.baslDk.delete(0, END)
        self.bitSa.delete(0, END)
        self.bitDk.delete(0, END)

        self.ogrnIsimGirisi.place_forget()
        self.ogrtIsimGirisi.place_forget()
        self.ogrnSoyisimGirisi.place_forget()
        self.ogrtSoyisimGirisi.place_forget()
        self.ogrnNumaraGirisi.place_forget()
        self.ogrtNumaraGirisi.place_forget()
        self.ogrnSifreGirisi.place_forget()
        self.ogrtSifreGirisi.place_forget()
        self.ogrtVerdigiDersCombo.place_forget()
        self.tarihGun.place_forget()
        self.tarihAy.place_forget()
        self.tarihYil.place_forget()
        self.baslSa.place_forget()
        self.baslDk.place_forget()
        self.bitSa.place_forget()
        self.bitDk.place_forget()
        self.ders01Combo.place_forget()
        self.ders02Combo.place_forget()
        self.ders03Combo.place_forget()
        self.ders04Combo.place_forget()
        self.ders05Combo.place_forget()
        self.ders06Combo.place_forget()
        self.ders07Combo.place_forget()
        self.ders08Combo.place_forget()
        self.ders09Combo.place_forget()
        self.ders10Combo.place_forget()
        

    def Cikis(self):
        self.root.quit
        sys.exit(0)


if __name__ == '__main__':  # Program calistiriliyor.

    root = Tk()
    GUI = GUI(root)
    root.mainloop()
