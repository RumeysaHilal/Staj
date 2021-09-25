from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.messagebox import askyesno
from tkinter import ttk
from tkhtmlview import HTMLLabel
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from tkdocviewer import *

root = Tk()  # Ana
root.title("JSON Log Viewer")
photo = PhotoImage(file="moon.png")
root.iconphoto(True, photo)
menubar = Menu(root)
tabNot = ttk.Notebook(root)  # Tab widget için tanımlama yaptım.


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
    <img src="image/v25.png">
    <p> Grafiklerin altında yer alan araç çubuklarından büyüteç ile istenen bölge yakınlaştırılabilir. Geri tuşuna veya ev tuşuna basılarak eski haline dönülebilir. İstenilen grafik kaydedilebilir. Grafik üzerinde çok yönlü ok ile oynama yapılabilir. 
    Configuration tool ile root.tablonun boyutunda ve yerinde oynamalar yapılabilir.</p>
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


def bubble_sort(tablo):  # root.tabloyu basılma sayısına göre büyükten küçüğe sıralarken kullanmak için yazdım.
    for i in range(0, len(tablo)):
        for j in range(0, len(tablo) - 1):
            if tablo[j][1] < tablo[j + 1][1]:
                tablo[j], tablo[j + 1] = tablo[j + 1], tablo[j]  # Değişim yaptım.


def grafik():
    
    for i in tabNot.winfo_children(): #Notebook'a ait sekmeleri gezmek için bir döngü oluşturdum.
        i.destroy() #Sekmeleri kaldırdım.
    
    x_ekseni = list()
    y1_ekseni = list()
    y2_ekseni = list()

    dizi = list()  # Bu dizi JSON dosyadaki "Basılan tuş" veri bilgisinin alınabilmesi içindir
    basilantus = list()  # # Bu ikinci diziyi basılan tuşlardan tekrarlı olanlarını bir kere tutmak için kullandım.
    basilantus1 = list()  # Basilan tus ifadesini silip sadece tuşun kalması için atanan dizi

    sayilar = list()  # Bu dizi "Tuşun basılma sayısı" verisini tutar.
    basilmasayisi = list()  # Birkaç kez basılan tuşların basılma sayısı da sayilar[] dizisinde birkaç kez tutuluyor. Bu verileri tekrarsız bir şekilde tutmak için olan dizi.
    explode =list()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                               filetypes=(("json files", "*.json"), ("all files", "*.*")))
    # Seçilen dosyanın dizinini alıyor.

    # Dosya seçilmemesi durumunda ekrana mesaj gelmesi için try-except bloğu yazdım.
    try:
        with open(root.filename,encoding="utf8") as f:
            veri = json.load(f)  # Json verilerinin bir sözlüğe aktarımını yaptım.
    except:
        messagebox.showerror("Hata!", "Dosya seçilmedi.")
        return 0 #Devam edip hataya yol açmaması için yazdım.

    for i in range(0, len(veri)):
        dizi.append(veri[i]["action"])  # Basılan tuşu bulabilmek için sözlükten bu bilgiyi çektim ve diziye ekledim ikinci grafic için gerekli
        x_ekseni.append(i)  # Zamanın listeye aktarımı için yazdım.
        y1_ekseni.append(veri[i]["totallines"])  # Satırları bir listeye ekledim.
        y2_ekseni.append(veri[i]["totalchars"])  # Karakterleri listeye ekledim.

    root.figure = Figure(figsize=(7, 7), dpi=100)  # Ortaya çıkacak root.tablonun boyutu ve inç (dpi) değerlerini girdim.
    plt = root.figure.add_subplot(1, 1, 1)  # root.tablonun konacağı yerin noktaları
    plt.plot(x_ekseni, y1_ekseni, label="Toplam Satır")
    plt.plot(x_ekseni, y2_ekseni, label="Toplam karakter")
    plt.set_title("Zamana Göre Toplam Karakter ve Satır Sayısı")
    plt.set_xlabel("Zaman")
    plt.set_ylabel("Toplam Karakter ve Toplam Satır")
    plt.legend()  # Grafik çubuklarının isimlerinin ekranda çıkması için yazdım.
    plt.grid(True)  # Arka taraftaki çizgilerin belirgin olması için True değeri verdim.

    tab1 = ttk.Frame(tabNot)  # İlk tab için tanımladım.
    tabNot.add(tab1, text="Line Chart")  # Ana kısma eklenmesini ve ismini verdim.
    tabNot.pack(expand=1, fill="both")  # Ekranda görünmesi için paketledim.

    canvas = FigureCanvasTkAgg(root.figure, tab1)  # Belirlenen root.tablonun nerede gösterileceğini belirttim.
    toolbar = NavigationToolbar2Tk(canvas, tab1)  # Normal matplotlib root.tablosunun altında yer alan toolbar için ekledim.
    canvas.get_tk_widget().pack()  # Ekranda görünmesi için paketleme işlemi yaptım.

    ####### ↓↓↓ İkinci grafik için gerekli olan kodların kısmı ↓↓↓

    for i in range(0, len(veri)):
        a = 0  # a değişkeni o tuşun kaç kere basıldığını tutmak için var. Her döngüde farklı bir tuşa geçileceği için her seferinde 0'ladım.
        a = dizi.count(veri[i]["action"])  # count metodu ile dönüştürülen dosyadaki basılan tuşların kaç defa basıldığına dair bilgiyi a değişkenine aktardık.
        sayilar.append(a)  # Bu bilgiyi sayilar[] dizisine ekledim
        if (dizi[i] not in basilantus):  # Burada amaç tekrarsız bir dizi oluşturmaktır. Bu yüzden if koşulunu kullandım. Eğer basilantus[] dizisinde bu eleman yoksa:
            basilantus.append(dizi[i])  # O zaman veriyi basilantus[] dizisine ekle
            basilmasayisi.append(sayilar[i])  # Aynı zamanda basılan tuşun kaç kere basıldığına karşılık gelen ve yine aynı indekste bulunan basılma sayısını basilmasayisi[] dizisine ekle


    for i in range(0,len(basilantus)):  # basilantus[] dizisinin uzunluğu adeddince döndürdüm
        cmt=basilantus[i].split(":",1)
        b=cmt[1].replace(" ","")
        b=b.replace("\n","")
        basilantus1.append(b)  # Sadece harflerin eklenmesi için yazdım

    tab2 = ttk.Frame(tabNot)  # İkinci kısım için tab widget tanımlaması yaptım.
    tabNot.add(tab2, text="Pie Chart")  # Ana kısma eklenmesini ve isminin ne olacağını belirttim.

    root.figure2 = Figure(figsize=(10, 8), dpi=100)  # Pencerede oluşturulan tuvalin boyutu
    plt2 = root.figure2.add_subplot(1, 1, 1)


    plt2.pie(basilmasayisi, labels=basilantus1,  wedgeprops={'edgecolor': 'black'}, radius=1.2,
             textprops={'fontsize': 10, 'color': "#065535"}, rotatelabels=15,
             autopct='%1.1f%%')  # Dairesel grafiğin çizilmesi

    canvas2 = FigureCanvasTkAgg(root.figure2, tab2)  # root.tablonun sayfası belirlenir
    toolbar2 = NavigationToolbar2Tk(canvas2, tab2)
    canvas2.get_tk_widget().place(relx=1, rely=1, anchor=CENTER)
    canvas2.get_tk_widget().pack()  # Pack ile ekranda görünmesi sağlanır

    # ↓↓↓↓↓↓ tablo için gerekli kodlar ↓↓↓↓↓↓↓↓

    root.tablo = list()  # Basılan tuş, basılma sayısı ve yüzdelik diliminin hepsini bir arada tutabileceğim bir liste tanımladım.
    for i in range(0,len(basilmasayisi)):  # Basılma sayılarının yüzdeliklerini hesapladım, basılma sayısı ve basılan tuşla birlikkte listeye attım.
        per = round((basilmasayisi[i] * 100) / len(dizi), 1)
        root.tablo.append([basilantus1[i], basilmasayisi[i], per])

    bubble_sort(root.tablo)  # Azalan şekilde sıralanmasını istediğimiz için azalan şekilde sıralayacak bir kabarcık sıralama algoritması kullandım.

    tab3 = ttk.Frame(tabNot)  # Diğer iki sekmede yaptığım gibi yeni bir sekme oluşturdum.
    tabNot.add(tab3, text="Pie Chart Table")
    root.tablo.insert(0, ["Karakterler", "Basilma Sayisi","Yuzdelik Deger"])  # root.tablodaki başlıkları belirtmek için listenin ilk baışna başlıkları ekledim.

    style=ttk.Style() #Satır aralarını düzenlemek için tanımladık.
    style.configure("Treeview",rowheight=50) # Tablonun satır aralığını değiştirmek için yazdım.
    style.configure("Treeview.Heading", font=(None, 20)) #Başlık boyutunu değiştirmek için yazdım.
    style.configure("Treeview.Columns",font=(None,15)) # Sütunların

    tab3.grid_columnconfigure(3, weight=5)
    tab3.grid_rowconfigure(len(root.tablo)-1, weight=1)

    #Scrollbar frame ile kullanırken düzgün çalışmadığı için Treeview yapısı ile tablo oluşturdum.
    tree=ttk.Treeview(tab3)
    tree.grid(rowspan=50,columnspan=15,sticky="nsew")

    tree["columns"]=("1","2","3")
    tree["show"]="headings"

    tree.column("1",width=90,anchor="c") # Sütunların genişliği ve nereye konumlandırılacağını yazdım.
    tree.column("2", width=90, anchor="c")
    tree.column("3", width=90, anchor="c")

    tree.heading("1", text=root.tablo[0][0]) #Yerleştirilecekler başlıkları tabloda nerde olduklarını belirttim.
    tree.heading("2", text=root.tablo[0][1])
    tree.heading("3", text=root.tablo[0][2])

    treeview=tree
    for i in range(1,len(root.tablo)): #Tablodaki verilerin eklenmesini sağladım.
        treeview.insert("", 'end', text=f"L{i}",values=(root.tablo[i][0],root.tablo[i][1],root.tablo[i][2]))

def mesajkutusu(adi, w, h):
    soru = askyesno(title="Bilgilendirme",
                    message="Raporu görüntülemek ister misiniz?")  # Kaydedilen dosyanın açılıp açılmayacağını belirlemek için soru ekranı
    if soru:  # Mesaj kutusundan olumlu yanıt geldiğinde çalışması için koşul kullandım
        ekran = Toplevel()  # Dosyanın açılacağı pencereyi belirledim.
        ekran.title(adi)  # Açılan dosyanın adının pencerenin başlığı olması için yazdım.
        ekran.geometry(
            f"{w}x{h}+100+30")  # Grafiklerin ve root.tablonun boyutları farklı olduğu için uzunluk ve genişliği parametre olarak alıp burada kullandım
        doc = DocViewer(ekran)  # Dosyanın görüntüleneceği pencereyi belirttim.
        doc.pack(side="top", expand=1, fill="both")  # Dosyanın görünmesi için yazdım.
        doc.display_file(adi)  # Hangi dosyanın ekranda görüneceğini yazdım.

def dosya_adi():
    dosyaadi = root.filename.split(".json")  # Rapor hazırlanırken aynı isimde oluşturulmaması ve hangi dosyaya ait grafikler olduğunu belirtirken kullanmak için yazdım.
    dosyaadi = dosyaadi[0].split("/") #Uzantı öncesi indiste yer aldığı için ilk indisi verdim ve dizin olduğu zaman / ile bölü yerleri ayırdım.
    return dosyaadi[len(dosyaadi)-1] # En son kısımda yer aldığı için indis olarak uzunluğun bir eksiğini verdim.

def line_report():
    try: #Dosya açılmış olmadan rapor oluşturmaya çalışınca hata gelmesi için yazdım.
        root.figure
    except:
        messagebox.showerror("Hata", "Dosya seçilmedi.")
        return 0
    root.figure.savefig(f"linechart_{dosya_adi()}.pdf")  # Dosya olarak kaydetmek için gerekli kod
    mesajkutusu(f"linechart_{dosya_adi()}.pdf", 700,
                700)  # Mesaj kutusu ve kaydedilen dosyanın ekrana gelmesi için yazılan fonksiyonu çağırdım.

def pie_report():
    try:
        root.figure2
    except:
        messagebox.showerror("Hata", "Dosya seçilmedi.")
        return 0
    root.figure2.savefig(f"piechart_{dosya_adi()}.pdf")
    mesajkutusu(f"piechart_{dosya_adi()}.pdf", 750, 750)

def tablo_report():
    try:
        len(root.tablo)>0
    except:
        messagebox.showerror("Hata","Dosya seçilmedi!")
        return 0

    for i in range(0,len(root.tablo)):
        if len(root.tablo[i][0])> 45:
            root.tablo[i][0]=root.tablo[i][0][-46:] #Çok uzun olduğu zaman tabloya sığmadığı için böyle bir yöntem kullandım.

    doc = SimpleDocTemplate(f"tablo_{dosya_adi()}.pdf", pagesize=A4)  # Dosyanın ismi ve sayfa boyutu verildi.
    table = Table(root.tablo, 3 * [inch*2.5], len(root.tablo) * 3)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (1, 1), 'Helvetica'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, -1), 8),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.blue),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))  # Oluşturulacak dosyanın stilleri
    doc.build([table])
    mesajkutusu(f"tablo_{dosya_adi()}.pdf", 800, 800)


filemenu = Menu(menubar, tearoff=0)  # Menünün nerden başlayacağını ve menü çubuğunu belirttim.
filemenu.add_command(label="New")  # Menü elemanlarının isimlerini ve gerekli olanların komutlarını verdim.
filemenu.add_command(label="Open", command=grafik)
filemenu.add_command(label="Save")
filemenu.add_separator()  # Üsttekiler ve alttakiler arasında ayırıcı olarak koydum.
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)  # Menünün adı

reportmenu = Menu(menubar, tearoff=0)
reportmenu.add_command(label="Linechart Report", command=line_report)
reportmenu.add_command(label="Piechart Report", command=pie_report)
reportmenu.add_command(label="Table Report", command=tablo_report)
menubar.add_cascade(label="Reports", menu=reportmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to Use", command=yardim)
helpmenu.add_command(label="About", command=hakkinda)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.geometry("750x750+200+10")
root.mainloop()  # Kodun ekrana gelmesi için gerekli kısım.
