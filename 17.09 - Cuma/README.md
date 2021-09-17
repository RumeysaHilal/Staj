# JSON Log Viewer 

Json Log Viewer, dosya olarak seçilen json formatındaki log dosyasının içindeki toplam karakter ve toplam satır bilgisiyle zamana göre çizgi grafik, basılan tuşların sayısı ile de pasta grafik ortaya çıkaran bir arayüzdür. Ek olarak pasta grafikteki basılan tuşun ismi, basım sayısı ve basım yüzdesinin yer aldığı bir tablo da vardır.

# Kurulum

## > Windows 10 için

Kurulum yapmak istenilen ortamda python kurulu olmalıdır. Buradan indirilen zip dosyası öncelikle klasöre ayıklanır. Ayıklanan klasörde main.py uzantılı ana dosya bulunur. Dosyayı çalıştırmadan önce gerekli kütüphaneleri dahil etmek için aşağıda yazılan kod komut satırına yazılır. 

Komut satırını açmak için dizinin bulunduğu kısma cmd yazmak yeterlidir. Ya da windows arama kısmına cmd yazarak çalıştırılır ve bulunan dizin cd program_yolu şeklinde verilerek gidilebilir. 

![e1](https://user-images.githubusercontent.com/66912242/133676815-ecc3c671-ff48-471c-a8d7-9ecd736c569f.PNG)

![e2](https://user-images.githubusercontent.com/66912242/133676822-ae03333b-fd4e-475d-a4e6-946ac762afcb.PNG)

**Gerekli kütüphaneler için:**

    pip install -r requirements.txt
    
İşlem bittiği zaman yüklü ise buradaki gibi "Requirement already satisfied" , yüklü değil ise yüklendiğini belirten "successfully"  yazısı komut satırında görünür.

![e3](https://user-images.githubusercontent.com/66912242/133678296-ff18a357-6534-401f-90be-06fe368f2b46.PNG)


# Çalıştırma

Programı çalıştırmak için yeniden komut satırını açınız. 
Komut satırına aşağıdaki komutu yazınız:

    python main.py
    
Program çalışacaktır.

![e4](https://user-images.githubusercontent.com/66912242/133680595-1da8a0ed-2a37-4d35-a9b4-f7c24ff68856.PNG)

# Özellikler
1. Dosya Açma
2. Dosyadan veri çekme
3. Veri üzerinde işlem yapma 
4. İşlenen verilerle grafik ve tablo oluşturma

**Ekran Görüntüleri:**
#### İlk Açılan Ekran:

![e5](https://user-images.githubusercontent.com/66912242/133679755-7b45115b-7407-40e1-a9a0-b6463fee5160.PNG)

#### Dosya Seçmek İçin Kullanılan Alan: 

![e10](https://user-images.githubusercontent.com/66912242/133680094-fa88e36f-da2e-46e8-b2e5-f545ddf17cea.PNG)

#### Grafikler ve Tablo:

![e7](https://user-images.githubusercontent.com/66912242/133680578-bed96187-2246-4d9e-9ff0-f12878056499.PNG)

![e8](https://user-images.githubusercontent.com/66912242/133680581-1dea79d6-2118-4d6b-adc7-5f849125fc00.PNG)

![e9](https://user-images.githubusercontent.com/66912242/133760117-27e0d86f-59f5-44e7-a1be-9d99175e8766.PNG)


