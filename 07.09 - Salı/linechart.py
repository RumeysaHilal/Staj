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

x_ekseni=list() #Üzerinde çalışma yapacağım için liste değişkenleri oluşturdum.
y_ekseni=list()

for i in range(0,94):
    x_ekseni.append(veri[i]["totallines"]) #Satır sayılarını bir listeye ekledim.
    y_ekseni.append(veri[i]["totalchars"]) #Karakter sayılarını bir listeye ekledim.
    
    
plt.plot(x_ekseni,y_ekseni) #Listeye eklediğim verileri tablo için erlerine yazdım. 
plt.title("Toplam Satır Sayısındaki Karakter Sayısı")
plt.xlabel("Toplam Satir") #x ekseninin ismini verdim.
plt.ylabel("Toplam Karakter") #y ekseninin ismini verdim.
plt.grid(True) #Arka taraftaki çizgilerin belirgin olması için True değeri verdim.
plt.show() #Çalıştırınca ekrana grafiğin gelmesi için show fonksiyonunu kullandım.
