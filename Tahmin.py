import requests
from bs4 import BeautifulSoup
from csv import writer
import os

url2="https://www.otoeksper.com.tr/ikinci-el"   # Verilerin alındığı 1. Site
response2=requests.get(url2)
soup2=BeautifulSoup(response2.text,"html.parser")
page2=-2
#sayfa2=soup2.find(class_="sayfalama").text[::-1][2:4]    # sayfa sayısını sabit tutmak istemiyorsanız güncel olarak bütün dataları almak istiyorsanız 10. ve 11. yorum satırlarını kaldırın!
#sayfa2=int(sayfa2)                                                                # yaklaşık 600 veri alınıyor fazlasına ihtiyacınız varsa bunu yapın 
sayfa3=10 # güncel sayfa aldıysanız bu satırı kaldırın!

print("Veriler toplanıyor lütfen bekleyiniz..\n(bu işlem yaklaşık 30 saniye sürecektir)")
# print(sayfa2)

while page2<sayfa3: # güncel sayfa alıyorsanız sayfa3'ü sayfa2 yapınız
    page2+=1
    response2=requests.get(f"{url2}"+f"?sayfa={page2}")
    soup2=BeautifulSoup(response2.text,"html.parser")
    ilanlar2=soup2.find_all(class_="Arac-Foto")
    with open ("***BURAYA OLUŞTURULACAK OLAN CSV DOSYA YOLUNU GİRİNİZ KODLA AYNI DİZİNDE OLMALI!***","a",newline='',encoding="utf-8")as file: # örnek "C:/Users/theod/OneDrive/Masaüstü/python/Projeler/Repos/test.csv"
        csv=writer(file)
        if page2==-1:
            csv.writerow(["yakit","vites","model","km","fiyat"]) 
        else:  
            for ilan2 in ilanlar2:
                yakit=ilan2.find(class_="Arac-Ozellik Yakit").text
                vites=ilan2.find(class_="Arac-Ozellik Vites").text
                model=ilan2.find(class_="Arac-Ozellik Yil").text
                model=int(model) 
                km=ilan2.find(class_="Arac-Ozellik Km").text
                km=float(km)
                fiyat=ilan2.find(class_="Arac-Ozellik Fiyat").text[0:5]
                fiyat=float(fiyat)             
                csv.writerow([yakit,vites,model,km,fiyat])

url="https://www.araba.com/otomobil" # Verilerin alındığı 2. Site
page=-1
response=requests.get(f"{url}"+f"?siralama=fiyata-gore&sayfa={page}")
soup=BeautifulSoup(response.text,"html.parser")
# sayfa=soup.find_all(class_="btn item")[6].text # sayfa sayısı
sayfa=19
print("Veriler toplanıyor lütfen bekleyiniz..\n")
while page<sayfa+1: 
    page += 1 
    response=requests.get(f"{url}"+f"?siralama=fiyata-gore&sayfa={page}")
    soup=BeautifulSoup(response.text,"html.parser")
    ilanlar=soup.find_all(class_="card-list-item")  
    with open ("***BURAYA OLUŞTURULACAK OLAN CSV DOSYA YOLUNU GİRİNİZ YUKARDAKİ İLE AYNI DOSYA OLMALI***","a",newline='',encoding="utf-8")as file:
        csv=writer(file)
                
        for ilan in ilanlar:  # Veri Düzenlemesi 

            yakit=ilan.find(class_="search-category-mileage").text[10:18]
            vites=ilan.find(class_="search-category-mileage").text[18:38]
            model=ilan.find(class_="title").text[0:5]
            model=int(model)
            km=ilan.find(class_="search-category-mileage").find("b").text
            km=float(km)
            fiyat=ilan.find(class_="sl-price").text[0:4]
            fiyat=float(fiyat)

            if yakit==" Benzin":
                yakit="Benzinli"
            elif yakit=="  Benzin":
                yakit="Benzinli"
            elif yakit==" Benzin ":
                yakit="Benzinli"
            elif yakit=="Benzin  ":
                yakit="Benzinli"
            elif yakit=="zin  Oto":
                yakit="Benzinli"
            elif yakit=="Benzin":
                yakit="Benzinli"
            else:
                pass

            
            if yakit==" Dizel":
                yaikt="Dizel"
            elif yakit=="  Dizel":
                yakit="Dizel"
            elif yakit=="  Dizel ":
                yakit="Dizel"
            elif yakit==" Dizel  ":
                yakit="Dizel"
            elif yakit==" Dizel ":
                yakit="Dizel"
            elif yakit=="Dizel  O":
                yakit="Dizel"
            elif yakit=="Dizel  D":
                yakit="Dizel"
            else:
                pass

            if yakit==" Hibrit ":
                yakit="Benzinli/LPG"
            elif yakit=="  Hibrit":
                yakit="Benzinli/LPG"
            else:
                pass
            

            if vites==" Düz Vites":
                vites="Düz"
            elif vites=="  Düz Vites":
                vites="Düz"
            elif vites=="üz Vites":
                vites="Düz"
            elif vites=="Düz Vites":
                vites="Düz"
            else:
                pass


            if vites==("  Otomatik Vites"):
                vites="Otomatik"
            elif vites==(" Otomatik Vites"):
                vites="Otomatik"
            elif vites==("tomatik Vites"):
                vites="Otomatik"
            elif vites=="matik Vites":
                vites="Otomatik"
            elif vites=="Otomatik Vites":
                vites="Otomatik"
            else:
                pass


            if vites==" Yarı Otomatik Vites":
                vites="Yarı Otomatik"
            elif vites=="Yarı Otomatik Vites":
                vites="Yarı Otomatik"
            else:
                pass
                            
            csv.writerow([yakit,vites,model,km,fiyat])

dosya = open("*** CSV DOSYA YOLU****","r",encoding="utf-8") 
veri_sayisi = 0
for satir in dosya:
    veri_sayisi+=1
veri_sayisi=veri_sayisi-1
dosya.close()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
veriler=pd.read_csv('*** CSV DOSYA YOLU ***') 

yakitlar=veriler.iloc[:,0:1].values
yakitlar2=veriler.iloc[:,0:1].values
vitesler=veriler.iloc[:,1:2].values
model_km=veriler.iloc[:,2:4].values
fiyat=veriler.iloc[:,4:5].values
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
yakitlar[:,0]=le.fit_transform(veriler.iloc[:,0])
vitesler[:,0]=le.fit_transform(veriler.iloc[:,1:2])


ohe=preprocessing.OneHotEncoder()
yakitlar=ohe.fit_transform(yakitlar).toarray()
vitesler=ohe.fit_transform(vitesler).toarray()


sonuc=pd.DataFrame(data=yakitlar, index=range(veri_sayisi),columns=["Benzinli/LPG","Benzinli","Dizel"])
sonuc1=pd.DataFrame(data=vitesler, index=range(veri_sayisi),columns=["Otomatik","Düz","Yarı Otomatik"])
sonuc2=pd.DataFrame(data=model_km, index=range(veri_sayisi),columns=["Model","Km"])
sonuc3=pd.DataFrame(data=fiyat, index=range(veri_sayisi),columns=["Fiyat"])

s=pd.concat([sonuc,sonuc1,sonuc2],axis=1)
s2=pd.concat([s,sonuc3],axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(s,sonuc3,test_size=1,random_state=0)

from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators=100,random_state=0)
rf_reg.fit(x_train,y_train)

class Girdiler():
    yakıt_giris=input("yakıt türü seçiniz:\n1)Benzin/LPG\n2)Benzin\n3)Dizel\n")
    yakıt_giris=int(yakıt_giris)
    if yakıt_giris==1:
        b=0.0
        c=1.0
        e=0.0
    elif yakıt_giris==2:
        b=1.0
        c=0.0
        e=0.0
    elif yakıt_giris==3:
        b=0.0
        c=0.0
        e=1.0
    else:
        print("geçersiz giriş")


    vites_giris=input("vites türü seçiniz:\n1)Düz Vites\n2)Otomatik Vites\n3)Yarı Otomatik Vites\n")
    vites_giris=int(vites_giris)

    if vites_giris==1:
        x=1.0
        y=0.0
        z=0.0
    elif vites_giris==2:
        x=0.0
        y=1.0  
        z=0.0
    elif vites_giris==3:
        x=0.0
        y=0.0  
        z=1.0  
    else:
        print("geçersiz giriş")
    arac_yıl=input("Arac yılını giriniz(örnek:2012):\n")
    arac_yıl=int(arac_yıl)
    arac_km=input("Arac kilometresini giriniz (örnek:212.000):\n")
    arac_km=float(arac_km)

inp=Girdiler()
price=f"{rf_reg.predict([[inp.b,inp.c,inp.e,inp.x,inp.y,inp.z,inp.arac_yıl,inp.arac_km]])} ₺" 
print(price)
os.remove("*** CSV DOSYA YOLU ***") # Verileri güncel tutmak için uygulama kapandıktan sonra veriler silinecektir.
# veriler silinsin istemiyorsanız 227. satırı kaldırın !
