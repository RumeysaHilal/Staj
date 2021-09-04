# Python Matplotlib ile Json Dosyasından Alınan Verilerle Nasıl Grafik Çizilir?

Öncelikle çalışılacak veri seti seçilmelidir. Bu veri setinin json formatında olması gerekir. Bir py dosyasında json modülü import ederek bir sözlüğe aktarım yaptım
**load** fonksiyonuyla. İki ayrı liste değişkeni tanımlayarak verileri listelere append fonksiyonu ile ekledim. Ben veri setimin ilk 100 verisini kullandığım için range ile bir for döngüsü oluşturdum. Eksenleri belirtmek için seabornu kullanarak grafik altyapımı oluşturdum. Başlığı ve eksenlerin adlandırmasını yaptım ve en son ekrana çıktısının ggelmesi için matplotlibden show fonksiyonunu kullandım.

Veri setini İstanbul büyükşehir Belediyesi Açık Veri Portalından aldım. Mayıs ayı trafik yoğunluk verisi ismi de.


Son olarak çıktı şu şekildedir: 

![grafik](https://user-images.githubusercontent.com/66912242/132095601-de983eab-701c-4b13-b7c4-cb04029fc3db.PNG)


