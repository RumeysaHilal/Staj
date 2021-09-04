import json
import matplotlib.pyplot as plt
import seaborn as sns

with open ("mytraf.json") as f:
    veri=json.load(f) #Json verilerinin bir sözlüğe aktarımını yaptım.

saatler=list()
ortalama=list()

for i in range(0,100):
    saatler.append(veri["records"][i][9]) # İlk 100 verinin saatlerini listeye ekledim.
    ortalama.append(veri["records"][i][7]) # İlk 100 verinin saatlik ortalama yoğunluğunu listeye ekledim.

axes= sns.regplot(x=saatler,y=ortalama) #Tablonun eksenlerini belirtir.
sns.set_style("whitegrid") #Grafik yazısının stilini belirler.

axes.set_title("Farklı günlere ait saatlere göre trafik yoğunluğu grafiği") #Başlık
axes.set_ylabel("ortalama") # Y düzleminin ismi
axes.set_xlabel("Saatler") # X düzleminin ismi

plt.plot(saatler,ortalama,"ro") # Satır ve sütun verilerini gönderip nokta şeklinde ekrana
# çıktı vermesi için ro komutunu kullandım.
plt.show() #Tabloyu göstermesi için kullandım.
