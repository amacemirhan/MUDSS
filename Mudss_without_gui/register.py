import sqlite3
def registerStd():
    connection=sqlite3.connect("veritabani.db")
    cursor=connection.cursor()
    print("****Marmara Universtesi Ders Secim Sistemi Ogrenci Kayit Olma****")
    ad=input("Adinizi girniz:")
    soyad=input("Soyadinizi giriniz:")
    email=input("E posta adresinizi giriniz:")
    no=input("Ogrenci numaranizi giriniz:")
    sifre=input("Olusturmak istediginiz sifre:")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Student (FirsName TEXT,LastName TEXT,
                            Email TEXT,No TEXT,Password TEXT)""")
    cursor.execute("""insert into Student (FirsName,LastName,
                              Email,No,Password) values(?,?,?,?,?)""",(ad,soyad,email,no,sifre))
    connection.commit()
    connection.close()
    print("Ogrenci kaydiniz basariyla tamamlanmistir.")
def registerTch():
    connection=sqlite3.connect("veritabani.db")
    cursor=connection.cursor()
    print("****Marmara Universtesi Ders Secim Sistemi Ogretmen Kayit Olma****")
    ad=input("Adinizi girniz:")
    soyad=input("Soyadinizi giriniz:")
    email=input("E posta adresinizi giriniz:")
    sifre=input("Olusturmak istediginiz sifre:")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Teacher (FirsName TEXT,LastName TEXT,
                            Email TEXT,Password TEXT)""")
    cursor.execute("""insert into Teacher (FirsName,LastName,
                              Email,Password) values(?,?,?,?)""",(ad,soyad,email,sifre))
    connection.commit()
    connection.close()
    print("Ogretmen kaydiniz basariyla tamamlanmistir.")
#registerStd()
#registerTch()
def loginStd():
    connection=sqlite3.connect("veritabani.db")
    cursor=connection.cursor()
    print("****Marmara Universtesi Ders Secim Sistemi Ogrenci Girisi****")
    no=input("Ogrenci numaranizi giriniz:")
    sifre=input("Sifrenizi giriniz:")
    data=cursor.execute("""select No,Password from Student""")
    for i in data:
        if(i[0]==no and i[1]==sifre):
            return no
    
    return -1
def loginTch():
    connection=sqlite3.connect("veritabani.db")
    cursor=connection.cursor()
    print("****Marmara Universtesi Ders Secim Sistemi Ogretmen Girisi****")
    email=input("E posta adrsinizi giriniz:")
    sifre=input("Sifrenizi giriniz:")
    data=cursor.execute("""select Email,Password from Teacher""")
    for i in data:
        if(i[0]==email and i[1]==sifre):
            return True
        else:
            return False
#print(loginTch())
#print(loginStd())

