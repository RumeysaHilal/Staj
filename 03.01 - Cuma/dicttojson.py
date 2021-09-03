import json
# Dictionary veri tipindeki verileri json stringine çevirir.
kisi_dict = {
    "isim":"hilal",
    "soyisim":"sevinc",
    "yas":"20",
}

kisi_json=json.dumps(kisi_dict)
print(kisi_json)