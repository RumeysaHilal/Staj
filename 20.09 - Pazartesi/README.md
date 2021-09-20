# Menubara Reports Menüsü Eklemek, Matplotlib Grafiklerini ve Oluşturulan Tabloyu PDF Olarak Kaydetmek ve Ekranda Göstermek

Reports menüsü daha önce yapılan file ve help menuleri gibi hazırlanır. Ekrana gelen matplotlib grafiklerini kaydetmek için grafiği ekrana getiren figure savefig("dosya_adi.pdf") şeklinde fonksiyonla kullanılır ve dosya bulunulan dizine kaydedilir. Kayıt işlemini yaptıktan sonra ekrana bir mesaj kutusu gelir ve kaydedilen dosyanın açılmasını isteyip istenmediği sorulur. Cevap "Evet" ise ekrana gelmesi için tkdocviewer kütüphanesi import edilerek, yeni bir pencere oluşturup display_file("dosya_adi") şeklinde fonksiyonla kullanılır. Fonksiyonu kullanmadan önce görünecek pencere DocViewer() ile kullanılır ve ekrana getirilmesi sağlanır. tkdocviewer indirilmesi yapıldıktan sonra ek olarak ghostscript isimli indirmenin de yapılması gerekir. Eğer yapılmazsa pdf dosyasını açmaya çalışınca ekran gelir ama içerik gelmez ve hata gösterilir. 

Tablo için yeniden dosyanın içinde tablo oluşturma kodları yazılır. Bu şekilde tablonun pdfe kaydı yapılır. 


![1](https://user-images.githubusercontent.com/66912242/134000419-883fb12b-56c2-493e-88b4-981be8f93780.PNG)


![2](https://user-images.githubusercontent.com/66912242/134000423-e97f6b3b-c8ed-422a-9fd6-52ef1d5bdf6a.PNG)


![3](https://user-images.githubusercontent.com/66912242/134000424-e42ac6e0-6dc0-4924-a933-33ca2f3955f4.PNG)


![4](https://user-images.githubusercontent.com/66912242/134000425-251b9476-159f-4e8b-b805-543e4aac300b.PNG)



![5](https://user-images.githubusercontent.com/66912242/134000428-57c7ca60-b303-4f44-a813-cd8ec65c33c2.PNG)
