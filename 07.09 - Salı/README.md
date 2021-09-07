# Komut Satırından Argüman Almak Nasıl Yapılır?

Argüman almak için öncelikle sys modülünü import etmiş olmamız gerekir. Sys modülü kullandığımız pythonda çeşitli işlemler yapmamızı sağlar. dir(sys) yazarak fonksiyonlarını ve niteliklerini görebiliriz.

sys.argv komut satırında çalıştırma esnasındaki parametreleri liste olarak tutar. Eğer bir değişkene eşitlemişsek indislerle istediğimiz parametreye ulaşabiliriz.

sys.exit komutunu kullanarak programı durmaya zorlayabiliriz bir hata durumunda. try-except bloğunda veya bir if-else bloğunda kullanılabilir.

Bu klasörde makine idsi, zaman, toplam karakter, toplam satır ve basılan tuşların kaydının olduğu json formatında log dosyasından bir komut satırı uygulaması geliştirdim. Argüman olarak bu dosyayı alan python dosyası, y ekseni toplam karakter sayısını, x ekseni ise toplam satır sayısını gösteren bir line chart ekrana getiriyor. 

***Görseli de bu şekilde:***

![linechart](https://user-images.githubusercontent.com/66912242/132350734-9bd92315-86c7-490a-8d6a-e73caad106c7.png)
