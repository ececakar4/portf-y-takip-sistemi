# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:45:42 2026

@author: ececa
"""
import pandas as pd

varliklar= []
fiyatlar= []
adetler= []

while True :
    varlikadi= input("varlık adını giriniz: ")
    if varlikadi.lower()=='q':
        break
    try:
        fiyat = float(input(f"{varlikadi} birim fiyatı nedir ? "))
        adet = float(input(f"kaç adet {varlikadi} var? "))
        
        varliklar.append(varlikadi)
        fiyatlar.append(fiyat)
        adetler.append(adet)
    except ValueError:
        print("lütfen geçerli bir sayı girin")
        
veriler ={
    'varlik':varliklar,
    'birimfiyat': fiyatlar,
    'adet': adetler
}

df =pd.DataFrame(veriler)

if not df.empty:
    df['toplamdeger']=df['birimfiyat']*df['adet']
    
    print("\n" + "="*30)
    print(df)
    
    toplampara=df['toplamdeger'].sum()
    print(f"\ntoplam portföy değeri: {toplampara} USD")
else:
    print("hiç veri girilmedi")
    
    
    