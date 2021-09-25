# Json Log Viewer Üzerinde Düzeltmeler

* Her dosyayı çalıştırabilecek şekilde döngüler düzenlendi.

* Scrollbar ile birleştirilmeye çalışılan table frame'i treeview ile değiştirildi. Scrollbar çalışmadığı için bu değişime gidildi. Böylece tabloda ne kadar veri olursa olsun aşağı kaydırarak görülebilir.

* Aralık verilerek alınan action bilgisinin içerisi string metodları kullanılarak ne kadar uzun olursa olsun alınması sağlandı. 

* Dosya açılırken utf-8 ile açılması sağlandı. Böylece Türkçe karakterler düzgün şekilde tabloda ve grafikte görünüyor.

* Report menüsü için try-except blokları yazıldı dosya açılmadan raporların istenme durumu için. 

![3](https://user-images.githubusercontent.com/66912242/134690416-40865a13-3625-4051-ac67-d6f0fd0189a3.PNG)

* Tab Widget kısmı her açılan dosyaya göre yenilenecek şekilde değiştirildi. Daha önce her dosya için yeni üç sekme oluşturuluyordu.

![5](https://user-images.githubusercontent.com/66912242/134772172-59d57e93-f918-41b4-b7e8-20627816e87c.PNG)

![6](https://user-images.githubusercontent.com/66912242/134772173-c73125a7-b260-4349-b0ee-ecc35d97da94.PNG)


* Report kısmında oluşturulan pdf dosyalarının ismi, açılan dosyanın ismiyle grafiğin ismi birlikte olacak şekilde değiştirildi.

**Örnek kayıt edilmiş bir pie grafiği:**

![2](https://user-images.githubusercontent.com/66912242/134690086-6f55f4cc-58b6-4f7e-9565-0dfd08e62226.PNG)



