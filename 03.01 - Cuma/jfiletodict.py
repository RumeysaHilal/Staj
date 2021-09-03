import json
#JSON dosyasındaki verileri alır.
with open ("kisi.json") as f:
    veri=json.load(f)

print(veri["isim"])
