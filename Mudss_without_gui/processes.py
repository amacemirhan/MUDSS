# -*- coding: utf-8 -*-
import sqlite3
import time
import random
def DersSecim(No):#string tipinde Ogrenci numarasiyla cagirilmali
    connection=sqlite3.connect('veritabani.db')
    cursor=connection.cursor()
    print("****Marmara Universtesi Ders Secim Sistemi Ders Secme Ekrani****")
    print("Maksimum 30 kredilik ders secebilirsiniz\nBilgisayar Muhendisligi Dersleri\n")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Lesson (No TEXT,LesCode TEXT,
                            IsComp INT,Akts INT,Note TEXT)""")
    data=cursor.execute("""select * from Bilgisayar_Muhendisligi""")
    for i in data:
        print(i[0],"\t",i[1],"\t",i[2])
    ders=1
    while(ders!="0"):
        ders=input("Seçmek istediginiz ders kodunu giriniz(Cikmak icin 0 giriniz):")
        ders=ders.upper()
        kontrol=False
        data=cursor.execute("""select * from Bilgisayar_Muhendisligi""")
        for j in data:
            if(j[0]==ders):
                kontrol=True
                akts=int(j[2])
        top=0
        data=cursor.execute("""select * from Lesson""")
        for k in data:
            if(k[0]==No and k[2]==0):
                top += int(k[3])
        data=cursor.execute("""select * from Lesson""")
        for z in data:
            if(kontrol==False):
                print("Boyle bir ders bulunmamaktadir.")
                break
            elif(top+akts>30):
                print("Toplam 30 krediden fazla ders secemezsiniz.")
                break
            elif(z[0]==No and z[1]==ders and z[2]==1):
                print("Secmek istediginiz ders zaten basariyla tamamlamıssiniz.")
                break
            elif(z[0]==No and z[1]==ders and z[2]==0):
                print("Secmek istediginiz ders zaten halihazirda secili")
                break
            else:
                cursor.execute("""insert into Lesson (No,LesCode,
                                  IsComp,Akts) values(?,?,?,?)""",(No,ders,0,akts))
                print("Dersi basariyla sectiniz")
                break
        connection.commit()
    connection.close()
def Gno(Letter):
    if(Letter=="AA"):
        return 4.0
    elif(Letter=="BA"):
        return 3.5
    elif(Letter=="BB"):
        return 3.0
    elif(Letter=="CB"):
        return 2.5
    elif(Letter=="CC"):
        return 2.0
    elif(Letter=="DC"):
        return 1.5
    elif(Letter=="DD"):
        return 1.0
    elif(Letter=="FD"):
        return 0.5
    elif(Letter=="FF"):
        return 0.0
    else:
        return False
       
def DersGoruntule(No):
    connection=sqlite3.connect('veritabani.db')
    cursor=connection.cursor()
    print("****Marmara Universtesi Ders Secim Sistemi Ders Goruntuleme Ekrani****")
    data=cursor.execute("""select * from Lesson""")
    top=0
    print("Suanda almis oldugunuz dersler:")
    for i in data:
        if(i[0]==No and i[2]==0):
            print(i[1])
            top=top+i[3]
    print("Almıs oldugunuz derslerin kredi toplamı:",top)
    top=0
    ntop=0.0
    j=0
    print("Suana kadar tamamladiginiz dersler:")
    data=cursor.execute("""select * from Lesson""")
    for i in data:
        if(i[0]==No and i[2]==1):
            print(i[1])
            top=top+i[3]
            ntop=ntop+Gno(i[4])
            j=j+1
    print("Tamamlamıs oldugunuz derslerin kredileri toplamı: ",top)
    if(j!=0):
        print("Genel Not Ortalamaniz: ",ntop/j)
    print("Mezun olmak icin geriye kalan kredi sayiniz: ",240-top)
    connection.close()
def DersTamamla(No):
    connection=sqlite3.connect('veritabani.db')
    cursor=connection.cursor()
    print("****Marmara Universtesi Ders Secim Sistemi Ders Tamamlama Ekrani****")
    data=cursor.execute("""select * from Lesson""")
    ders=input("Tamamlamis oldugunuz dersin kodunu yaziniz:")
    harf=input("Dersi tamamladiginiz harf notunu giriniz.(Yalnızca:AA,BA,BB,CB,CC,DC,DD,FD,FF)")
    ders=ders.upper()
    harf=harf.upper()
    if (Gno(harf)==False):
        print("Yanlis harf notu girdiniz.")
        time.sleep(1)
        exit()
    degisiklik=False
    for i in data:
        if(i[0]==No and i[1]==ders and i[2]==0):
            print("Dersiniz basariyla kaydedildi.")
            cursor.execute("""UPDATE Lesson SET 
                              IsComp=1,Note=? WHERE No=? and LesCode=?;""",(harf,No,ders))
            connection.commit()
            degisiklik=True
            break
        elif(No==i[0] and i[1]==ders and i[2]==1):
            print("Dersiniz zaten tamamlanmıs girdiginiz not guncellendi.")
            cursor.execute("""UPDATE Lesson SET 
                              Note=? WHERE No=? and LesCode=? """,(harf,No,ders))
            connection.commit();
            degisiklik=True
            break
        
    if(degisiklik==False):
        print("Tamamlamak istediginiz ders bulunamadi sectiginizden emin olunuz.")
    connection.close()
def StringeCevir(gun,saat):
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
def randomGunSaat(ls):
    while (True):
        g=random.randint(0, 4)#random gun indexi aldik
        s=random.randint(0, 8)#random saat indexi aldik
        current=-1
        if(ls[g][s]!=""):
            current=ls[g][s]
            ls[g][s]=""
            return g,current
def listeSirala(ls):
    for a in range(len(ls)-1):
        for i in range(len(ls)-1):
            if(ls[i+1][1][0]<ls[i][1][0]):
                current=ls[i+1]
                ls[i+1]=ls[i]
                ls[i]=current
    for k in range(len(ls)-1):
        for j in range(len(ls)-1):
            if(ls[j+1][1][0]==ls[j][1][0] and ls[j+1][1][1]<ls[j][1][1]):
                current2=ls[j+1]
                ls[j+1]=ls[j]
                ls[j]=current2
    return ls
def listeYazdir(ls,No):
    try:
        dosya = open(No+"_dersprogrami.txt","w")
    except FileNotFoundError:
        print("Dosya Acilamadi!")
        time.sleep(0.5)
        exit()
    for i in range(len(ls)-1):
        dosya.write(str(ls[i][0])+" "+StringeCevir(ls[i][1][0],ls[i][1][1])+"\n")
    dosya.close()
def DersProgramiOlustur(No):
    connection=sqlite3.connect('veritabani.db')
    cursor=connection.cursor()
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
    listeSirala(atanmis)
    listeYazdir(atanmis,No)
    connection.close()

    
    
    
    
    
    
    
    
    
    
    
    