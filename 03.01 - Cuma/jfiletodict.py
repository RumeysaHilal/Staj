import json
with open ("kisi.json") as f:
    veri=json.load(f)

print(veri["isim"])