from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkhtmlview import HTMLLabel
import matplotlib
import matplotlib.pyplot as plt
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

root = Tk()  # Ana
root.title("JSON Log Viewer")
photo = PhotoImage(file="moon.png")
root.iconphoto(True, photo)
menubar = Menu(root)


def yardim():
    top = Toplevel()
    top.title("Nasıl Kullanılır")
    top.geometry("700x400")

    my_label = HTMLLabel(top, html="""
    <h3> Json Log Viewer Nedir?</h3>
    <p> Json Log Viewer, json formatında olan log dosyasının içindeki zaman,basılan karakterler, toplam karakter ve toplam satır sayısının grafiklerini gösteren bir arayüzdür.</p>
    <h3> Nasıl Kullanılır? </h3> 
    <p> File kısmında Open diyerek açmak istenilen dosya seçilir.</p>
    <img src="image/v24.png">
    <p>Dosya seçildikten sonra aç butonuna tıklanır. Ekrana iki farklı sekmede grafikler gelir. Biri line grafiği iken diğeri pie grafiğidir. Hangi grafikler olduğu sekmelerin üzerinde yazmaktadır. </p>
    <img src="imagev25.png">
    <p> Grafiklerin altında yer alan araç çubuklarından büyüteç ile istenen bölge yakınlaştırılabilir. Geri tuşuna veya ev tuşuna basılarak eski haline dönülebilir. İstenilen grafik kaydedilebilir. Grafik üzerinde çok yönlü ok ile oynama yapılabilir. 
    Configuration tool ile tablonun boyutunda ve yerinde oynamalar yapılabilir.</p>
    <img src="image/v26.png"/>
    <p> About kısmından kodlayan kişi hakkında bilgiler alınabilir.</p>
    """)
    my_label.pack()


def hakkinda():
    top2 = Toplevel()
    top2.title("Hakkında")
    top2.geometry("350x250")

    label2 = HTMLLabel(top2, html=""" <h3>  Hakkında </h3>
        <p> İsim Soyisim: Rümeysa Hilal Sevinç </p>
        <a href= 'https://github.com/RumeysaHilal'>Github </a> 
        """)
    label2.pack(pady=20, padx=20)


def bubble_sort(tablo):  # Tabloyu basılma sayısına göre büyükten küçüğe sıralarken kullanmak için yazdım.
    for i in range(0, len(tablo)):
        for j in range(0, len(tablo) - 1):
            if tablo[j][1] < tablo[j + 1][1]:
                tablo[j], tablo[j + 1] = tablo[j + 1], tablo[j]  # Değişim yaptım.


def grafik():
    x_ekseni = list()
    y1_ekseni = list()
    y2_ekseni = list()

    dizi = list()  # Bu dizi JSON dosyadaki "Basılan tuş" veri bilgisinin alınabilmesi içindir
    basilantus = list()  # # Bu ikinci diziyi basılan tuşlardan tekrarlı olanlarını bir kere tutmak için kullandım.
    basilantus1 = list()  # Basilan tus ifadesini silip sadece tuşun kalması için atanan dizi
    sayilar = list()  # Bu dizi "Tuşun basılma sayısı" verisini tutar.
    basilmasayisi = list()  # Birkaç kez basılan tuşların basılma sayısı da sayilar[] dizisinde birkaç kez tutuluyor. Bu verileri tekrarsız bir şekilde tutmak için olan dizi.
    explode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    root.filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                               filetypes=(("json files", "*.json"), ("all files", "*.*")))
    # Seçilen dosyanın dizinini alıyor.

    # Dosya seçilmemesi durumunda ekrana mesaj gelmesi için try-except bloğu yazdım.
    try:
        with open(root.filename) as f:
            veri = json.load(f)  # Json verilerinin bir sözlüğe aktarımını yaptım.
    except:
        messagebox.showerror("Hata!", "Dosya seçilmedi.")
        root.mainloop() #Hata çıktığı zaman ana sayfadan devam etmesi için ekledim.

    for i in range(0, 94):
        dizi.append(veri[i]["action"])  # Basılan tuşu bulabilmek için sözlükten bu bilgiyi çektim ve diziye ekledim ikinci grafic için gerekli
        x_ekseni.append(i)  # Zamanın listeye aktarımı için yazdım.
        y1_ekseni.append(veri[i]["totallines"])  # Satırları bir listeye ekledim.
        y2_ekseni.append(veri[i]["totalchars"])  # Karakterleri listeye ekledim.

    figure = Figure(figsize=(7, 7), dpi=100)  # Ortaya çıkacak tablonun boyutu ve inç (dpi) değerlerini girdim.
    plt = figure.add_subplot(1, 1, 1)  # Tablonun konacağı yerin noktaları
    plt.plot(x_ekseni, y1_ekseni, label="Toplam Satır")
    plt.plot(x_ekseni, y2_ekseni, label="Toplam karakter")
    plt.set_title("Zamana Göre Toplam Karakter ve Satır Sayısı")
    plt.set_xlabel("Zaman")
    plt.set_ylabel("Toplam Karakter ve Toplam Satır")
    plt.legend()  # Grafik çubuklarının isimlerinin ekranda çıkması için yazdım.
    plt.grid(True)  # Arka taraftaki çizgilerin belirgin olması için True değeri verdim.

    tabNot = ttk.Notebook(root)  # Tab widget için tanımlama yaptım.
    tab1 = ttk.Frame(tabNot)  # İlk tab için tanımladım.

    tabNot.add(tab1, text="Line Chart")  # Ana kısma eklenmesini ve ismini verdim.

    tabNot.pack(expand=1, fill="both")  # Ekranda görünmesi için paketledim.

    canvas = FigureCanvasTkAgg(figure, tab1)  # Belirlenen tablonun nerede gösterileceğini belirttim.
    toolbar = NavigationToolbar2Tk(canvas, tab1)  # Normal matplotlib tablosunun altında yer alan toolbar için ekledim.
    canvas.get_tk_widget().pack()  # Ekranda görünmesi için paketleme işlemi yaptım.

    ####### ↓↓↓ İkinci grafik için gerekli olan kodların kısmı ↓↓↓

    for i in range(0, 94):
        a = 0  # a değişkeni o tuşun kaç kere basıldığını tutmak için var. Her döngüde farklı bir tuşa geçileceği için her seferinde 0'ladım.
        a = dizi.count(veri[i]["action"])  # count metodu ile dönüştürülen dosyadaki basılan tuşların kaç defa basıldığına dair bilgiyi a değişkenine aktardık.
        sayilar.append(a)  # Bu bilgiyi sayilar[] dizisine ekledim
        if (dizi[i] not in basilantus):  # Burada amaç tekrarsız bir dizi oluşturmaktır. Bu yüzden if koşulunu kullandım. Eğer basilantus[] dizisinde bu eleman yoksa:
            basilantus.append(dizi[i])  # O zaman veriyi basilantus[] dizisine ekle
            basilmasayisi.append(sayilar[i])  # Aynı zamanda basılan tuşun kaç kere basıldığına karşılık gelen ve yine aynı indekste bulunan basılma sayısını basilmasayisi[] dizisine ekle

    for i in range(0, 29):  # basilantus[] dizisinin uzunluğu adeddince döndürdüm
        basilantus1.append((basilantus[i][13:25]))  # Sadece harflerin eklenmesi için yazdım

    tab2 = ttk.Frame(tabNot)  # İkinci kısım için tab widget tanımlaması yaptım.
    tabNot.add(tab2, text="Pie Chart")  # Ana kısma eklenmesini ve isminin ne olacağını belirttim.

    figure2 = Figure(figsize=(10, 8), dpi=100)  # Pencerede oluşturulan tuvalin boyutu
    plt2 = figure2.add_subplot(1, 1, 1)

    plt2.pie(basilmasayisi, labels=basilantus1, explode=explode, wedgeprops={'edgecolor': 'black'}, radius=1.2,
             textprops={'fontsize': 10, 'color': "#065535"}, rotatelabels=30,
             autopct='%1.1f%%')  # Dairesel grafiğin çizilmesi
    
    canvas2 = FigureCanvasTkAgg(figure2, tab2)  # Tablonun sayfası belirlenir
    toolbar2 = NavigationToolbar2Tk(canvas2, tab2)
    canvas2.get_tk_widget().place(relx=1,rely=1,anchor=CENTER)
    canvas2.get_tk_widget().pack()  # Pack ile ekranda görünmesi sağlanır

    # ↓↓↓↓↓↓ Tablo için gerekli kodların

    tablo = list()  # Basılan tuş, basılma sayısı ve yüzdelik diliminin hepsini bir arada tutabileceğim bir liste tanımladım.
    for i in range(0,
                   29):  # Basılma sayılarının yüzdeliklerini hesapladım, basılma sayısı ve basılan tuşla birlikkte listeye attım.
        per = round((basilmasayisi[i] * 100) / len(dizi), 1)
        tablo.append([basilantus1[i], basilmasayisi[i], per])
    bubble_sort(
        tablo)  # Azalan şekilde sıralanmasını istediğimiz için azalan şekilde sıralayacak bir kabarcık sıralama algoritması kullandım.

    tab3 = ttk.Frame(tabNot)  # Diğer iki sekmede yaptığım gibi yeni bir sekme oluşturdum.
    tabNot.add(tab3, text="Pie Chart Table")
    tablo.insert(0, ["Karakterler", "Basılma Sayısı",
                     "Yüzdelik Değer"])  # Tablodaki başlıkları belirtmek için listenin ilk baışna başlıkları ekledim.

    for row in range(0, len(tablo)):  # Satırlar için döngü
        for column in range(0, 3):  # Sütunlar için döngü
            if row == 0:  # Listenin ilk başında başlıklar bulunduğu için ilk satır için özel bir kontrol yaptım.
                label = Label(tab3, text=tablo[row][column], bg="grey", fg="white", padx=1, pady=1)
                label.config(font=("Times 13 bold"))  # Yazı stilini verdim.
            else:  # İlk satırdan sonrası için normal şekilde gidecek satırlar için yazım.
                label = Label(tab3, text=tablo[row][column], bg="white", fg="black", padx=1, pady=1)
                label.config(font=("Times 10 bold"))
            label.grid(row=row, column=column, sticky="nsew", padx=1,
                       pady=1)  # Satır sütun değerlerini, hücrenin nereye konacağı, pixel değerlerini yazdım.
            tab3.grid_columnconfigure(column, weight=1)


filemenu = Menu(menubar, tearoff=0)  # Menünün nerden başlayacağını ve menü çubuğunu belirttim.
filemenu.add_command(label="New")  # Menü elemanlarının isimlerini ve gerekli olanların komutlarını verdim.
filemenu.add_command(label="Open", command=grafik)
filemenu.add_command(label="Save")
filemenu.add_separator()  # Üsttekiler ve alttakiler arasında ayırıcı olarak koydum.
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)  # Menünün adı

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to Use", command=yardim)
helpmenu.add_command(label="About", command=hakkinda)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.geometry("750x750+200+10")
root.mainloop()  # Kodun ekrana gelmesi için gerekli kısım.
