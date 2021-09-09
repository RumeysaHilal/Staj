# Tkinter ile Matplotlib Grafiğini Aynı Pencerede Çizmek

#### Tkinter nedir?
Tkinter, python ile çalışan grafiksel bir kullanıcı arayüzüdür. Basit bir yapıya sahiptir. 

#### Tkinter ile matplotlib grafiği çizmek
Öncelikle tkinter import edilmiş olmalı.Arayüz için ben root adında bir taban oluşturdum Tk() diyerek. menubar isimli değişkenin Menu olduğunu belirterek ana çerçeveyii parametre olarak verdim.
Daha sonra komut olarak vermek için bir fonksiyon tanımı yaptım grafik içinde. İçerisinde Menubardan gelecek dizinin içinden dosyanın ayrımını,grafik çizmek için gerekli verilerin ayıklamasını ve grafiğin çizilmesi için gereken fonksiyonları yazdım.
Normal matplotlib arayüzünde açılan toolbar eklentisinin de açılan pencerede görünmesi için bu fonksiyonun içerisinde tanımladım.

Fonksiyonun altında menubarın elemanlarını tanımladım ve isimlendirmesini yaptım. Ana çerçevenin boyutunu da yazdım.

**Açılan Ana Pencere:**

![tk1](https://user-images.githubusercontent.com/66912242/132694879-cdd5d4d2-aa31-487a-95f6-90b157ac961f.PNG)

**Ana Pencerenin Menüsü:**

![tk2](https://user-images.githubusercontent.com/66912242/132695022-35ecdbc1-1a37-4890-91e4-db8dc9d63712.PNG)

**Open Tıklandığı Zaman Açılan Pencere:**
İlk önce ana dizinde açılıyor sonra kendimiz istediğimiz klasöre gidip seçim yapabiliriz. Kodda uzantı kısmını belirttiğim için sadece .json formatını gösteriyor. Ancak sağ alt köşedeki oka basarak tüm dosyaları da seçebiliriz.

![tk3](https://user-images.githubusercontent.com/66912242/132695696-41655635-d2b9-47f9-aee7-474805b31efc.PNG)

**Grafik:**

![tk4](https://user-images.githubusercontent.com/66912242/132696079-f02901ae-cd60-4c40-9591-9fdac743389e.PNG)
