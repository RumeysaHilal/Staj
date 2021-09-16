from tkinter import *
from tkinter import filedialog
import matplotlib
import matplotlib.pyplot as plt
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

root=Tk() # Ana çerçeve
menubar=Menu(root) 

def grafik():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
    #Seçilen dosyanın dizinini alıyor.
    
    for i in root.filename.split("/"): #Dizini "/" ile ayırarak liste haline getirdim..
        if i.endswith(".json"): #Json dosyası ile işlem yapacağım için sonu uzantı ile biten eleman kontrolünü yaptım.
            dosyaadi=i  # Listede .json uzantısı ile biten elemanın tamamını daha sonra işlem yapmak için değişkene atadım.
    
    with open (dosyaadi) as f: 
        veri=json.load(f) #Json verilerinin bir sözlüğe aktarımını yaptım.

    x_ekseni=list() 
    y1_ekseni=list() 
    y2_ekseni=list()

    for i in range(0,94):
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
    
    canvas = FigureCanvasTkAgg(figure, root) #Belirlenen tablonun nerede gösterileceğini belirttim.
    toolbar = NavigationToolbar2Tk(canvas,root) #Normal matplotlib tablosunun altında yer alan toolbar için ekledim.
    canvas.get_tk_widget().pack() #Ekranda görünmesi için paketleme işlemi yaptım.
    
    
filemenu=Menu(menubar,tearoff=0) #Menünün nerden başlayacağını ve menü çubuğunu belirttim.
filemenu.add_command(label="New") # Menü elemanlarının isimlerini ve gerekli olanların komutlarını verdim.
filemenu.add_command(label="Open",command=grafik)
filemenu.add_command(label="Save")
filemenu.add_separator() #Üsttekiler ve alttakiler arasında ayırıcı olarak koydum.
filemenu.add_command(label="Exit", command=root.quit) 

menubar.add_cascade(label="File", menu=filemenu) #Menünün adı
root.config(menu=menubar)
root.geometry("640x480")
root.mainloop() #Kodun ekrana gelmesi için gerekli kısım.



