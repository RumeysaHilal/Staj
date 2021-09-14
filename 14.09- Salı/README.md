# Tkinter ile Html Nasıl Kullanılır?

Tkinter ile html kullanmak için öncelikle bazı modülleri indirmek gerekir bunlar pillow, requests, tkhtmlview 'dir. Tkhtmlview tek başına indirilmeye çalışınca hata alınacaktır. Öncelikle requests indirilmeli. Daha sonra kullanılacak yerde from tkhtmlview import HTMLLabel diyerek dahil etmek gerekir. Dahil ettikten sonra bir değişkene atama yaparak kullanılacak pencere ve içine yazılacak yazılar, gösterilecek resimler, verilecek bağlantılar html yazımına uygun olarak yazılır. < html > etiketi içerisine yazılmaz HTMLLabel içerisinde html= şeklinde parametre olarak yazım yapılır.

Bazı html etiketleri ve özellikleri:

| Etiket | İşlevi |
|--------|---------|
| < p> < /p> | Paragraflar içerisine yazılır.|
| < a href="link"> < /a>| Link vermek için kullanılır etiket arasına nasıl görünmesi istendiği yazılır.|
| < h1> < /h1> | En büyük başlık stilidir. Rakam büyüdükçe boyut küçülür.|
| < h3> < /h3> | h1 başlığından küçük boyutta yazı ekrana getirir.|
| < img src="resim.png"> | Resim ekler.|
| < ul> < /ul> | Listeleme yapar. |

Yapılan Json log viewer arayüzünün "About" ve "How to Use" kısmı html ile yazılmıştır. 


![v23](https://user-images.githubusercontent.com/66912242/133235337-09ecb2d9-e7f1-4dd9-9249-46e5336da4c3.PNG)


![v21](https://user-images.githubusercontent.com/66912242/133236835-5e8e7845-d7e1-4f9f-a7d2-c3e978bfca74.PNG)


![v22](https://user-images.githubusercontent.com/66912242/133235516-969a5f92-4ef3-49ba-bfea-6d0cd9be4c9f.PNG)
