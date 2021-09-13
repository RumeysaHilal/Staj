from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

root=Tk() # Ana 
root.title("JSON Log Viewer")
photo= PhotoImage(file="moon.png")
root.iconphoto(True,photo)
menubar=Menu(root) 

def grafik():
    
    x_ekseni=list() 
    y1_ekseni=list() 
    y2_ekseni=list()
    
    dizi=list() # Bu dizi JSON dosyadaki "Basılan tuş" veri bilgisinin alınabilmesi içindir
    basilantus=list()# # Bu ikinci diziyi basılan tuşlardan tekrarlı olanlarını bir kere tutmak için kullandım.
    basilantus1=list() # Basilan tus ifadesini silip sadece tuşun kalması için atanan dizi
    sayilar=list() # Bu dizi "Tuşun basılma sayısı" verisini tutar.
    basilmasayisi=list() # Birkaç kez basılan tuşların basılma sayısı da sayilar[] dizisinde birkaç kez tutuluyor. Bu verileri tekrarsız bir şekilde tutmak için olan dizi.
    explode=[0,0,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
    #Seçilen dosyanın dizinini alıyor.
    
    #Dosya seçilmemesi durumunda ekrana mesaj gelmesi için try-except bloğu yazdım.
    try:
        with open (root.filename) as f: 
            veri=json.load(f) #Json verilerinin bir sözlüğe aktarımını yaptım.
    except:
        messagebox.showerror("Hata!","Dosya seçilmedi.")
    
    for i in range(0,94):
        dizi.append(veri[i]["action"])  # Basılan tuşu bulabilmek için sözlükten bu bilgiyi çektim ve diziye ekledim
        x_ekseni.append(i) #Zamanın listeye aktarımı için yazdım.
        y1_ekseni.append(veri[i]["totallines"]) #Satırları bir listeye ekledim.
        y2_ekseni.append(veri[i]["totalchars"]) #Karakterleri listeye ekledim.
        
    
    figure = Figure(figsize=(5, 5), dpi=100) #Ortaya çıkacak tablonun boyutu ve inç (dpi) değerlerini girdim.
    plt = figure.add_subplot(1, 1, 1) #Tablonun konacağı yerin noktaları 
    plt.plot(x_ekseni,y1_ekseni,label="Toplam Satır")
    plt.plot(x_ekseni,y2_ekseni,label="Toplam karakter") 
    plt.set_title("Zamana Göre Toplam Karakter ve Satır Sayısı")
    plt.set_xlabel("Zaman")
    plt.set_ylabel("Toplam Karakter ve Toplam Satır")
    plt.legend() #Grafik çubuklarının isimlerinin ekranda çıkması için yazdım.
    plt.grid(True) #Arka taraftaki çizgilerin belirgin olması için True değeri verdim.
    
    tabNot=ttk.Notebook(root) #Tab widget için tanımlama yaptım.
    tab1=ttk.Frame(tabNot) #İlk tab için tanımladım.
    
    tabNot.add(tab1,text="Line Chart") #Ana kısma eklenmesini ve ismini verdim.
    tabNot.pack(expand=1,fill="both") #Ekranda görünmesi için paketledim.
    
    canvas = FigureCanvasTkAgg(figure, tab1) #Belirlenen tablonun nerede gösterileceğini belirttim.
    toolbar = NavigationToolbar2Tk(canvas,tab1) #Normal matplotlib tablosunun altında yer alan toolbar için ekledim.
    canvas.get_tk_widget().pack() #Ekranda görünmesi için paketleme işlemi yaptım.
    
    ####### ↓↓↓ İkinci grafik için gerekli olan kodların kısmı ↓↓↓

    for i in range(0, 94):
        a = 0  # a değişkeni o tuşun kaç kere basıldığını tutmak için var. Her döngüde farklı bir tuşa geçileceği için her seferinde 0'ladım.
        a = dizi.count(veri[i]["action"])  # count metodu ile dönüştürülen dosyadaki basılan tuşların kaç defa basıldığına dair bilgiyi a değişkenine aktardık.
        sayilar.append(a)  # Bu bilgiyi sayilar[] dizisine ekledim

        if (dizi[i] not in basilantus):  # Burada amaç tekrarsız bir dizi oluşturmaktır. Bu yüzden if koşulunu kullandım. Eğer basilantus[] dizisinde bu eleman yoksa:
            basilantus.append(dizi[i])  # O zaman veriyi basilantus[] dizisine ekle
            basilmasayisi.append(sayilar[i])  # Aynı zamanda basılan tuşun kaç kere basıldığına karşılık gelen ve yine aynı indekste bulunan basılma sayısını basilmasayisi[] dizisine ekle
        
    for i in range(0, 29):  # basilantus[] dizisinin uzunluğu sayısınca döndürdüm
        basilantus1.append((basilantus[i][14:23]))  # Sadece harflerin eklenmesi için yazdım

    tab2=ttk.Frame(tabNot) #İkinci kısım için tab widget tanımlaması yaptım.
    tabNot.add(tab2,text="Pie Chart") #Ana kısma eklenmesini ve isminin ne olacağını belirttim.
    
    figure2 = Figure(figsize=(10, 8), dpi=100) 
    plt2=figure2.add_subplot(1,1,1)
    
    plt2.pie(basilmasayisi, labels=basilantus1, explode=explode, wedgeprops={'edgecolor': 'black'}, radius=1.2,
                  textprops={'fontsize': 8, 'color': "#065535"}, rotatelabels=45, autopct='%1.1f%%') # Dairesel grafiğin çizilmesi
    canvas2 = FigureCanvasTkAgg(figure2, tab2) # Tablonun sayfası belirlenir
    toolbar2 = NavigationToolbar2Tk(canvas2, tab2)
    canvas2.get_tk_widget().pack() # Pack ile ekranda görünmesi sağlanır.
    
    
filemenu=Menu(menubar,tearoff=0) #Menünün nerden başlayacağını ve menü çubuğunu belirttim.
filemenu.add_command(label="New") # Menü elemanlarının isimlerini ve gerekli olanların komutlarını verdim.
filemenu.add_command(label="Open",command=grafik)
filemenu.add_command(label="Save")
filemenu.add_separator() #Üsttekiler ve alttakiler arasında ayırıcı olarak koydum.
filemenu.add_command(label="Exit", command=root.quit) 
menubar.add_cascade(label="File", menu=filemenu) #Menünün adı

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to Use")
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.geometry("700x600")
root.mainloop() #Kodun ekranda çalışması için gerekli kısım.
