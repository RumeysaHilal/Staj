# Markdown nedir?

####  Markdown,  github'da readme dosyaları yazılırken kullanılan, html benzeri bir işaretleme dilidir. Stil ve yazım olarak daha kolaydır.

### *Markdown'da Başlık*
Başlık boyuntunu belirtmek için "#" işareti kullanılır. Hashtag ne kadar çoksa o kadar küçük yazı elde edilir. Kullanıldığı zaman bold tipinde yazım ortaya çıkar. Kullanılmadığında bu paragraftaki gibi bir stil ile yazılmış olur. Arada bir boşluk bırakılması gerekir.

**Örnek olarak:**
###### Header 
    <h6> Header 6 adet '#' kullanıldı. (HTML karşılığı) </h6>

### *Markdown'da Paragraf*
Paragraf için herhangi bir işaret kullanmaya gerek yoktur. Normal bir word dosyasına yazım yapar gibi yazılır. Normal bir paragraf gibi içten değil satır başıdan yazmaya başlanır. Alt satır geçmek için htmlde bulunan <br> ifadesine benzer bir işarete gerek yoktur alt satıra geçmek için bir tab boşluk bırakmak veya alta geçilmesini istediğimiz satırın sonuna bir ('\') eğik çizgi koymamız yeterli olur. Boşluk koymadan alt satıra geçildiğinde yazı satırın devamı gibi algılanır ve alt satıra geçmez.Bir tab boş bırakarak normal formdan ayrılmasını da sağlayabiliriz.\

### *Markdown'da Listeler*
Listeleme işlemi için normal sayıların yanına '.' koyarak noktalama yapılır ya da " yıldız,-,+" kullanılarak sırasız listeler oluşturulur. Bir tab boşluk bırakılırsa listenin herhangi bir maddesinin iç içe listeler oluşturulabilir. Sıralı şekilde yazarken noktanın yanında herhangi bir rakam olması yeterlidir, kendisi sıralı şekilde ekrana göster. Parantez kapatma kullanılmaz listeleme yaparken ( ")" ) . Sırasız şekilde listeleme işleminde ise "+" işareti içi dolu yuvarlak oluştururken "-" işareti içi boş yuvarlak oluşturur. Yıldız işareti ise kare şeklinde listeleme oluşturur.

+ a
+ b
   - a
        * d

**Örnek olarak:**   
![liste1](https://user-images.githubusercontent.com/66912242/131729097-2caec6a4-22a0-45a2-b60f-adf4c3612513.PNG)
![liste2](https://user-images.githubusercontent.com/66912242/131729219-549f79ef-6ac0-491b-a282-d475e937418f.PNG)

Sırası karışık yazılmasına rağmen ilk olarak hangi sayıdan başlandı ise sıranın devamını ona göre getirir.

### *Markdown'da Yazı Stili*
Yazı stilinde italic ve bold ayarlarını yıldız veya alt çizgi kullanarak sağlanır. İki yıldızın arasına veya alt çizginin arasına yazılırsa italic, dört tanenin arasına yazılırsa bold olur. Yarısı bir tarafta yarısı bir tarafta olacak şekilde ortaya yazılır. İşaretler ve kelime arasına boşluk koyulmaz, kelimeler arasındaki boşluklar sorun değildir.

    (Örnek *italic yazı* veya _italic yazi_)
*italic yazı* 

    (Örnek **bold yazı** veya __bold yazi__)
__bold yazı__

### *Markdown'da Resimler*
Resim eklemek için !"[alternatif metin]"(url) şeklindeki kalıp doldurulur.(Tırnak işaretleri olmadan yazılır. Tırnak işaretleri olmadan link olarak algılanıyor alternatif metin) Issues kısmında new issue diyerek konmak istenen resim veya fotoğraf seçilirse bu kalıpta bir metin ortaya çıkar. Çıkan metni readme kısmında koymak istediğimiz kısma yapıştırırak resmi eklemiş oluruz.

### *Markdown'da Tablo Oluşturma*
Altgr + küçüktür büyüktür kısmına basılarak oluşturulan işaretle birlikte iki işaret arasına bir kolon ismi gelecek şekilde yazılar yazılır. Bir alt satırına yine aynı işaret arasına düz çizgiler yerleştirilir. Diğer satırlara da kolonların gösterdiği değerler,veriler yerleştirilir. 

**Örnek olarak:** 

![tablo](https://user-images.githubusercontent.com/66912242/131736903-e131053a-df5d-4e5a-a435-1c90aa5df980.PNG)

|birinci kolon|ikinci kolon|
|-------------|------------|
|k1|a1|
|k2|a2|



### *Markdown'da Link Bırakma*  
Link bırakmak da resim ekleme kalıbının başında ünlem olmayanı olarak tanımlanabilir. Köşeli parantezler içerisinde referans isim olarak ne kullanacksa o, normal parantezler içerisinde de link bulunur.

**Örnek olarak:**   
![ref](https://user-images.githubusercontent.com/66912242/131740180-ab5a85c4-7c3e-4cac-be76-b39c904cd737.PNG)   

[referans](google.com)


### *Markdown'da Kod Ekleme* 
Ters tırnak içinde yazılır. Ters tırnak klavyede Altgr + virgül kombinasyonu ile yapılır.

**Örnek olarak:**   
![kod](https://user-images.githubusercontent.com/66912242/131741083-673b256e-41eb-4fa7-ae64-6e45edcdd7c4.PNG)

`print("Hello world!")`


### *Markdown'da Alıntı Yapma* 
">" işareti kullanarak alıntı yapılır.

**Örnek olarak:**  
![alıntı](https://user-images.githubusercontent.com/66912242/131741698-e6d624aa-f942-43e8-90c4-c954af23a207.PNG)
>"Selam!"


