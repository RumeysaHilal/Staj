# Tkinter Penceresine Başlık Vermek, İcon Değiştirmek ve İki Grafiği Aynı Pencerede Tabbed Widget ile Göstermek

### Başlık Vermek

Başlık vermek için oluşturduğumuz ana pencereyi title("baslik") şeklinde fonksiyon ile kullanmak yeterlidir.

### İcon Değiştirmek 

İcon değiştirmek için iconphoto() fonksiyonu kullanılabilir. Bir değişkene PhotoImage(file="resim.png") şeklinde PhotoImage sınıfına dönüşümü yapıldıktan sonra ana pencere değişkeni ile root.iconphoto(False, degisken_adi) şeklinde tanımlama yapılabilir. ".ico" uzantılı bir icon ile de root.iconbitmap("new-icon.ico") şeklinde başka bir tanımlama da yapılabilir.

### Tabbed Widged

Öncelikle ttk import edilmiş olmalı. Bir değişkene (tabControl gibi) ttk.Notebook(root) diyerek atama yapılır. Bu yapılan sekmelerin bulunacağı sayfa içindir. Root ana ekran olarak belirlenen değişken adıdır. Daha sonra sekme olarak görünecek frame ataması ttk.Frame(tabControl) şeklinde başka bir değişkene yapılır (tab1 gibi). Bu tanımlamanın ana ekranda görünmesi için tabControl.add(tab1,text="Tab1") şeklinde eklemesi yapılır ve text olarak belirtilen yerde sayfa ismi verilir. Ekranda görünmesi için ana tab bloğu paketlemesi yapılır. Aynı şekilde ikinci bir sekme oluşturulur. 

Yaptığım arayüzde ilk sekmede line charta ait grafiğin olması için canvas olarak belirlediğim aynı sayfada açma komutunda root değil açılmasını istediğim sekmenin frame ismini verdim. İkinci sekmede de pie chart grafiğine ait görselin yer alması için ikinci canvas tanımımda da  ikinci frame ismini verdim.

**Görseller:**

Değiştirdiğim icon ve pencere ismi:

![v11](https://user-images.githubusercontent.com/66912242/133090358-3c8677c6-37f2-49dd-8fe7-ddb0ee3ef75f.PNG)

Dosya seçimi yapılana kadar sekmeler görünmeyecek şekilde yazdım.

![v12](https://user-images.githubusercontent.com/66912242/133090566-fcb3669f-3f53-49c5-8f16-cfe70ece821b.PNG)

**İlk sekme:**


![v13](https://user-images.githubusercontent.com/66912242/133090631-53e89d7a-637e-4e64-9709-b3835a1acec5.PNG)

**İkinci sekme:**


![v14](https://user-images.githubusercontent.com/66912242/133091050-168a19a5-09b0-45a3-8932-d48c18e8faa6.PNG)

