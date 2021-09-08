import sys
import matplotlib.pyplot as plt
import json

arguman=sys.argv #Çalıştırma esnasında komut satırından argüman almak için yazdım. 

#Argüman liste şeklinde alınıyor.

try:
    arg = sys.argv[1] #Argüman alınmaması durumunu kontrol ettim. Eğer veri girilmezse hata oluşacak ve bu except bloğunun çalışmasını sağlayacak.
except:
    print ("Komut satirindan arguman alinamadi..")
    sys.exit() #Argüman alınmaması durumunda çıkış yapılması için yazdım.

with open (arguman[1]) as f: # Liste şeklinde alındığı için ikinci dosyanın alınması için 1 indisini verdim.
     veri=json.load(f) #Json verilerinin bir sözlüğe aktarımını yaptım.

x_ekseni=list() #Süreyi atmak için tanımladım.
y1_ekseni=list() #Uzun bir veri setini alacağımız için veriye aktarım için tanımladım.
y2_ekseni=list()

for i in range(0,94):
    x_ekseni.append(i) #Zamanın listeye aktarımı için yazdım.
    y1_ekseni.append(veri[i]["totallines"]) #Satırları bir listeye ekledim.
    y2_ekseni.append(veri[i]["totalchars"]) 
    
    
plt.plot(x_ekseni,y1_ekseni,label="Toplam Satır")
plt.plot(x_ekseni,y2_ekseni,label="Toplam karakter") #Listeye eklediğim verileri tablo için erlerine yazdım. 
plt.title("Zamana Göre Toplam Karakter ve Satır Sayısı")
plt.xlabel("Zaman") 
plt.ylabel("Toplam Karakter ve Toplam Satır")
plt.legend() #Grafik çubuklarının isimlerinin ekranda çıkması için yazdım.
plt.grid(True) #Arka taraftaki çizgilerin belirgin olması için True değeri verdim.
plt.show() #Çalıştırınca ekrana grafiğin gelmesi için show fonksiyonunu kullandım.