import json
#Dictionary veri tipindeki verileri json dosyasına dönüştürür.
kisi_dict = {
    "isim" : "hilal",
    "soyisim" : "sevinc"
}

with open("kisi.json","w") as json_dosya:
    json.dump(kisi_dict,json_dosya)