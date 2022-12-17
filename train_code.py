import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
veriler=pd.read_csv('C:/Users/theod/OneDrive/Masaüstü/python/31-Projeler/son testler/datalar2.csv')


yakitlar=veriler.iloc[:,0:1].values
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


sonuc=pd.DataFrame(data=yakitlar, index=range(198),columns=["Benzinli/LPG","Benzinli","Dizel"])
sonuc1=pd.DataFrame(data=vitesler, index=range(198),columns=["Otomatik","Düz"])
sonuc2=pd.DataFrame(data=model_km, index=range(198),columns=["Model","Km"])
sonuc3=pd.DataFrame(data=fiyat, index=range(198),columns=["Fiyat"])

s=pd.concat([sonuc,sonuc1,sonuc2],axis=1)
s2=pd.concat([s,sonuc3],axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(s,sonuc3,test_size=1,random_state=0)

from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators=100,random_state=0)
rf_reg.fit(x_train,y_train)

print(rf_reg.predict([[1,0,0,1,0,2022,15.330]]))