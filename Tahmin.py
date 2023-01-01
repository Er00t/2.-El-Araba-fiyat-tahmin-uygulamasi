import tkinter as tk 
from tkinter import messagebox 
from tkinter.ttk import Combobox 
import requests 
from bs4 import BeautifulSoup 
from csv import writer,DictReader 
import os 
import pandas as pd 
import numpy as np 
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor 


def Veri_Topla():
    messagebox.showinfo(title="uyarı",message="Bu işlem yaklaşık 40-50 saniye sürecektir\nVeriler toplanırken lütfen bekleyiniz.")
    url2="https://www.otoeksper.com.tr/ikinci-el"   
    response2=requests.get(url2)
    soup2=BeautifulSoup(response2.text,"html.parser")
    page2=-2
    sayfa3=10 
    print("Veriler toplanıyor lütfen bekleyiniz..\n(bu işlem yaklaşık 30 saniye sürecektir)")
    while page2<sayfa3: 
        page2+=1
        response2=requests.get(f"{url2}"+f"?sayfa={page2}")
        soup2=BeautifulSoup(response2.text,"html.parser")
        ilanlar2=soup2.find_all(class_="Arac-Foto")
        with open ("*** CSV DOSYA YOLU ***","a",newline='',encoding="utf-8")as file:   #  <==  CSV DOSYA YOLUNU EKLEMEYİ UNUTMAYIN PROJE İLE AYNI DİZİNDE OLMASINA DİKKAT EDİN
            csv=writer(file)                                                           #       dosya bu şekilde olmalı ==> "C:/Users/Alperen/OneDrive/Masaüstü/python/test/proje.csv"
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
                    if yakit=="Hibrid":
                        yakit="Benzinli/LPG"
                    else:
                        pass  
                    csv.writerow([yakit,vites,model,km,fiyat])

    url="https://www.araba.com/otomobil" 
    page=-1
    response=requests.get(f"{url}"+f"?siralama=fiyata-gore&sayfa={page}")
    soup=BeautifulSoup(response.text,"html.parser")
    sayfa=20
    print("Veriler toplanıyor lütfen bekleyiniz..\n")
    while page<sayfa+1: 
        page += 1 
        response=requests.get(f"{url}"+f"?siralama=fiyata-gore&sayfa={page}")
        soup=BeautifulSoup(response.text,"html.parser")
        ilanlar=soup.find_all(class_="card-list-item")  
        with open ("*** CSV DOSYA YOLU ***","a",newline='',encoding="utf-8")as file:   # <== *** CSV DOSYA YOLU ***
            csv=writer(file)
                    
            for ilan in ilanlar:  

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
                elif yakit=="Hibrid":
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
    with open("*** CSV DOSYA YOLU ***","r",newline="",encoding="utf-8")as okuma: # <== *** CSV DOSYA YOLU ***
        DictReader(okuma)
        for oku in okuma:
            output_text.insert("end",oku) 


root=tk.Tk() # açılış
root.geometry("700x420+500+250")
root.resizable(False,False)
root.title("2.El Araç Fiyatı bul by Er00t")

data_button=tk.Button(root,text="Verileri topla",fg="black",bg="gray",command=Veri_Topla)
data_button.pack(padx=10,pady=10)
veri_label=tk.Label(text="Veriler",fg="red")
veri_label.pack(anchor="w",padx=40)
output_text = tk.Text(root,height=8)
output_text.pack()


# yakıt seçim
def Tahmin():

    dosya = open("*** CSV DOSYA YOLU ***","r",encoding="utf-8")  # <== *** CSV DOSYA YOLU ***
    veri_sayisi = 0
    for satir in dosya:
        veri_sayisi+=1
    veri_sayisi=veri_sayisi-1
    dosya.close()

    veriler=pd.read_csv('*** CSV DOSYA YOLU ***')               # <== *** CSV DOSYA YOLU ***
    yakitlar=veriler.iloc[:,0:1].values
    yakitlar2=veriler.iloc[:,0:1].values
    vitesler=veriler.iloc[:,1:2].values
    model_km=veriler.iloc[:,2:4].values
    fiyat=veriler.iloc[:,4:5].values
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


    x_train, x_test, y_train, y_test =train_test_split(s,sonuc3,test_size=1,random_state=0)

    rf_reg=RandomForestRegressor(n_estimators=100,random_state=0)
    rf_reg.fit(x_train,y_train)
    
    return rf_reg

yakıt = tk.Label(root,text = "Yakıt türü",fg="red")
yakıt.pack(anchor="w",padx=40)
list_yakıt=["Benzin/LPG",
    "Benzin",
    "Dizel"]
yakıt_getir=tk.StringVar()
yakıt_giris=Combobox(root,values=list_yakıt,textvariable=yakıt_getir)
yakıt_giris.pack(anchor="w",padx=40)





    


vites = tk.Label(root,text = "Vites türü",fg="red")
vites.pack(anchor="w",padx=40)
list_vites=["Düz Vites",
    "Otomatik Vites",
    "Yarı Otomatik Vites"]
vites_getir=tk.StringVar()
vites_giris=Combobox(root,values=list_vites,textvariable=vites_getir)
vites_giris.pack(anchor="w",padx=40)
vites_getir.get()

        

yıl = tk.Label(root,text = "Arac yılı",fg="red")
yıl.pack(anchor="w",padx=40)
list_yıl=["1990",
"1991",
"1992",
"1993",
"1994",
"1995",
"1996",
"1997",
"1998",
"1999",
"2000",
"2001",
"2002",
"2003",
"2004",
"2005",
"2006",
"2007",
"2008",
"2009",
"2010",
"2011",
"2012",
"2013",
"2014",
"2015",
"2016",
"2017",
"2018",
"2019",
"2020",
"2021",
"2022",
"2023"]
yıl_getir=tk.StringVar()
arac_yıl=Combobox(root,values=list_yıl,textvariable=yıl_getir)
arac_yıl.pack(anchor="w",padx=40)
yıl_getir.get()


km = tk.Label(root,text = "Araç kilometre (120.000)",fg="red")
km.pack(anchor="w",padx=40)
arac_km=tk.Entry(root,textvariable="örnek(120.000)",width=23)
arac_km.pack(anchor="w",padx=40)
arac_km.get()
def Secim():
    class Yakıt():
        if yakıt_getir.get()=="Benzin/LPG":
            b=0.0
            c=1.0
            e=0.0
        elif yakıt_getir.get()=="Benzin":
            b=1.0
            c=0.0
            e=0.0
        elif yakıt_getir.get()=="Dizel":
            b=0.0
            c=0.0
            e=1.0
        else:
            pass
    inp=Yakıt()
    class Vites():
        if vites_getir.get()=="Düz Vites":
            x=1.0
            y=0.0
            z=0.0
        elif vites_getir.get()=="Otomatik Vites":
            x=0.0
            y=1.0  
            z=0.0
        elif vites_getir.get()=="Yarı Otomatik Vites":
            x=0.0
            y=0.0  
            z=1.0  
        else:
            pass
    inpv=Vites()
    
    
    try:
        price=f"{Tahmin().predict([[inp.b,inp.c,inp.e,inpv.x,inpv.y,inpv.z,yıl_getir.get(),arac_km.get()]])} ₺" 
        messagebox.showinfo(title="Heplama Sonucu",message=price)
    except FileNotFoundError:
        messagebox.showinfo(title="Hata",message="Hesaplama işlemini Verileri topladıktan sonra yapınız!")       
    except AttributeError:
        messagebox.showinfo(title="Hata",message="Yanlış veri girişi!")
    except ValueError:
        messagebox.showinfo(title="Hata",message="Yanlış veri girişi!")
    return price
   

son_buton=tk.Button(text="hespla",bg="red",command=Secim)
son_buton.pack(ipadx=30,ipady=10)

root.mainloop()
os.remove("*** CSV DOSYA YOLU ***")   # <== *** CSV DOSYA YOLU ***
