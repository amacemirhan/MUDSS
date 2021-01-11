# -*- coding: utf-8 -*-
import register
import processes
import time
while(True):
    print("""Hosgeldiniz ne yapmak istersiniz ?
    1.Sisteme Giris Yap
    2.Siteme Kayit Ol
    3.Cikis""")
    secim=int(input(""))
    if(secim==1):
        print("""Girisinizi seciniz.\n
          1.Ogrenci Giris\n
          2.Ogretmen Giris\n""")
        secim2=int(input(""))
        if(secim2==1):
            no=register.loginStd()
            if(no!=-1):
                while(secim!=5):
                    print("""Programa basariyla giris yaptiniz\n
                          1.Derslerimin Istatigini Goruntule
                          2.Ders Secimi Yap
                          3.Tamamladigin Dersleri Sisteme Gir
                          4.Ders Programi Olustur
                          5.Cikis Yap""")
                    secim=int(input(""))
                    if(secim==1):
                        processes.DersGoruntule(no)
                    elif(secim==2):
                        processes.DersSecim(no)
                    elif(secim==3):
                        processes.DersTamamla(no)
                    elif(secim==4):
                        processes.DersProgramiOlustur(no)
                        print("Ders programiniz oLusturuldu ve yazildi ilgili dizinde bulabilirsiniz.")
                    elif(secim==5):
                        print("Cikis yapiliyor")
                        time.sleep(0.3)
                        print(".")
                        time.sleep(0.3)
                        print("..")
                        time.sleep(0.3)
                        exit()
                    else:
                        print("Yanlis secim yaptiniz.")
                        time.sleep(0.5)
                        exit()
            else:
                print("Sistemde Kaydiniz Bulunmamaktadir")
                time.sleep(1)
                exit()
        elif(secim2==2):
            register.loginTch()
        else:
            print("Yanlis secim yaptiniz.")
    elif(secim==2):
        print("""Kaydinizi seciniz.\n
          1.Ogrenci Kayit\n
          2.Ogretmen Kayit\n""")
        secim3=int(input(""))
        if(secim3==1):
            register.registerStd()
        elif(secim3==2):
            register.registerTch()
        else:
            print("Yanlis secim yaptiniz.")
    elif(secim==3):
        break
    else:
        print("Yanlis secim yaptiniz.")
        
    
