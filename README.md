## YOLO-DARKNET İLE MARUL TESPİTİ

Yolo algoritması kullanılarak nesne tespit işlemi gerçekleştirilecek. Tüm işlemler 
sırasıyla aşağıda adımlar halinde gösterilmiştir.

### ADIM-1: "Git Bash" Kurulumu

Git Bash sayesinde Github üzerinde bulunan klasörleri bilgisayarımıza indirebilmekteyiz.
Git Bash’i indirebilmek için aşağıda verilen adrese gidilir.

https://git-scm.com/downloads 

Bu adresteki sistem sizin bilgisayarınızda hangi işletim sistemi bulunduğunu otomatik olarak
algılayacaktır. Bilgisayarınızda bulunan işletim sistemine tıklanır ve indirme işlemine başlanır.

<img align="center" src="img/img1.png">

Setup dosyası bilgisayara indikten sonra tüm adımlara Next diyerek kurulum tamamlanır.

### ADIM-2: Darknet Kurulumu

Öncelikle çalışmalarımızı yapacağımız bir klasör oluşturmamız gerekiyor. Ben D’nin altına DeepLearningProjects
isminde bir klasör oluşturdum bu klasör içerisine de LettuceDetection isminde bir klasör daha oluşturdum. 
Tüm çalışmalarımızı ve darknet’i bu klasör içerisine kuracağım. Çalışmamda marul resimlerinin bulunduğu veri
setini kullanarak marul tespiti yapacağım için LettuceDetection ismini koydum. 

Daha sonra oluşturulan LettuceDetection klasörü içerisine girilir ve mause ile sağ tıklanarak “Git Bash Here”
seçeneği seçilir ve git komut satırı açılır.

<img align="center" src="img/img2.png">

Ardından aşağıdaki şekilde gösterilen Git Bash açılır.

<img align="center" src="img/img3.png">

Git Bash açıldıktan sonra Darknet klasörlerinin bulunduğu github hesabına gitmek için aşağıdaki github adresine
gidilir. 

https://github.com/AlexeyAB/darknet 

<img align="center" src="img/img4.png">

Bu adreste yolov4 modelini eğitebilmemiz için gerekli dosyalar bulunmaktadır. Bu github adresi kopyalanır ve Git Bash’e
geri dönülür. Aşağıdaki kod satırı Git Bash üzerine yazılır:

=> git clone https://github.com/AlexeyAB/darknet 

Ardından Darknet, LettuceDetection klasörümüzün içerisine yüklenmiş olur. 

<img align="center" src="img/img5.png">

İndirilen darknet dosyasının içerisine girilir ve içerisinde bulunan Makefile dosyası Notepad ile açılır.
Daha sonra bu dosya içerisindeki bazı parametreler aşağıdaki şekilde gösterildiği gibi değiştirilir. 

<img align="center" src="img/img6.png">

Ardından darknet github hesabının olduğu siteye yeniden gidilir. İlk olarak yolov4.conv.137 dosyası bilgisayarımıza
indirilir. Ctrl+F kullanılarak bu dosya bulunabilir.

<img align="center" src="img/img7.png">

İkinci olarak yine bu adreste bulunan yolov4.weights dosyası bilgisayarımıza indirilir.

<img align="center" src="img/img8.png">

Daha sonra indirilen bu iki dosya darknet içerisine kaydedilir.

<img align="center" src="img/img9.png">

Darknet klasörü içerisinde bulunan cfg dosyası açılır. Bu dosya içerisindeki yolov4.cfg dosyası kopyalanır
ve darknet klasörü içerisine yapıştırılır. Bu klasörün ismi lettuce_yolov4.cfg olarak değiştirilir.

<img align="center" src="img/img10.png">

<img align="center" src="img/img11.png">

Daha sonra lettuce_yolov4.cfg dosyası not defteri ile açılır ve aşağıdaki değişiklikler yapılır:

<img align="center" src="img/img12.png">

Yukarıdaki değişiklikler yapıldıktan sonra Ctrl+F yaparak arama bölümü açılır. “class” kelimesi aratılır.
Cfg dosyası içerisindeki tüm class parametrelerinin değiştirilmesi gerekmektedir. Veri setinde kaç adet 
sınıf varsa bu değer class parametresine yazılır. Bizim modelimizde sadece marul resimleri olduğu için class 
parametremize 1 değeri atanacaktır. Ayrıca filters parametresi de class değerinin 5 fazlasının 3 katı olması 
gerekmektedir (filters = (class+5)*3).

<img align="center" src="img/img13.png">

<img align="center" src="img/img14.png">

<img align="center" src="img/img15.png">

### ADIM-3: Veri Setini Oluşturma

İlk olarak veri setinde bulunacak resimleri saklayacağımız dosyayı oluşturalım. Dosyayı LettuceDetection 
klasörü içerisinde lettuce_images isminde oluşturacağız.

<img align="center" src="img/img16.png">

Artık veri setimiz için resimleri toplamaya başlayacağız. Veri setinde bulunacak resimlerin 416x416
boyutundan fazla olmasına dikkat ediniz.

Veri setiniz için yeterli sayıda resim bulamıyorsanız aşağıda göstermiş olduğum kod satırları ile veri
setinizde bulunan resimleri arttırabilirsiniz. Bu yüzden Google Colab’ı açalım ve ilk olarak aşağıdaki 
kod satırlarını kullanarak drive ile bağlantıyı gerçekleştirelim.

<img align="center" src="img/img17.png">

Veri setini arttırmak için keras kütüphanesinde bulunan sınıfları ve metotları kullanacağız.

<img align="center" src="img/img18.png">

Veri arttırma yönteminin ve hiperparametrelerin seçimi aşağıdaki kod satırında gösterilmiştir.

<img align="center" src="img/img19.png">

Veri arttırma işleminin yapılacağı görüntünün dosya okunması işlemi aşağıdaki kod satırlarında 
gösterimiştir.

<img align="center" src="img/img20.png">

Okuduğumuz resimden kaç adet darklı resim oluşturmak istiyorsak bunu for döngüsünde belirtmemiz gerekir.
Bu işlem aşağıdaki kod satırlarında gösterilmiştir. 

<img align="center" src="img/img21.png">

Veri setimiz içerisinde toplam 400 adet görüntü olacaktır. Aynı görüntülerin veri setinde bulunmamasına 
dikkat ediniz. Veri seti oluşturulduktan sonra Ctrl+A tuşu ile tüm resmiler seçilir ve resimlerden bir 
tanesine yeniden adlandır seçeneği seçilir. Böylece tüm resimlerin isimleri aynı şekilde olacaktır. 
Fakat rakamlar parantez içerisinde ve boşluklu olacaktır. Bu hata oluşturur, bu yüzden aşağıdaki kod 
satırları ile resimlerin isimleri düzenlenir. Bu kod satırları ile tek tek resimlerin elle düzeltmek 
yerine hızlıca istediğimiz isimle değiştirebiliriz.

<img align="center" src="img/img22.png">

<img align="center" src="img/img23.png">

<img align="center" src="img/img24.png">

### ADIM-4: Veri Setindeki Resimleri Etiketleme

Resimleri etiketlemek için Make Sense’i kullanacağız. Bu site açık kaynaktır ve tamamen ücretsizdir. 
Etiketlenen resimleri yolo formatında indirme imkanımız da bulunmaktadır. Bu siteye aşağıdaki linkten
ulaşabilirsiniz.

https://www.makesense.ai 

<img align="center" src="img/img25.png">

<img align="center" src="img/img26.png">

lettuce_images dosyası içerisindeki tüm resimler seçilir ve hepsi yüklenir.

<img align="center" src="img/img27.png">

<img align="center" src="img/img28.png">

<img align="center" src="img/img29.png">

Çıkan imleç ile tespit etmek istediğimiz nesnenin sınırları çizilir. Ardından "Select label" seçeneğine
tıklanır.

<img align="center" src="img/img30.png">

<img align="center" src="img/img31.png">

<img align="center" src="img/img32.png">

<img align="center" src="img/img33.png">

Veri setimizde bulunan tüm resimler yukarıdaki işlemlerden geçirilir. Tüm resimlerin doğru bir şekilde etiketlendiğinden emin olunuz.

<img align="center" src="img/img34.png">

<img align="center" src="img/img35.png">

Export seçeneğine tıklandıktan sonra .zip uzantılı klasör bilgisayarımıza indirilir. Daha sonra bu zip dosya
içerisinde bulunan txt dosyaları, veri setimizin bulunduğu lettuce_images dosyasına atılır.

<img align="center" src="img/img36.png">

Bu txt dosyalarının içerisinde tespit etmek istediğimiz marulların verilerini tutmaktadır.

### ADIM-5: Eğitim ve Test Verilerinin Oluşturulması

Öncelikle veri setimizin ve gerekli dosyaların atılacağı lettuce_data dosyasını LettuceDetection
klasörü içerisine oluşturalım. Ardından oluşturulan dosya içerisine veri setimizin bulunduğu
lettuce_images dosyasını atalım.

<img align="center" src="img/img37.png">

Not: Genel olarak sinir ağlarında verilerin %80’i eğitim, %20’si test için kullanılmaktadır.

lettuce_data dosyası içerisine lettuce_training.txt ve lettuce_testing.txt dosyalarını oluşturalım.

<img align="center" src="img/img38.png">

Oluşturulan bu txt dosyaları içerisine veri setinde bulunan resimlerin yolları girilecektir. lettuce_training.txt
dosyasına 320 adet resim yolu, lettuce_testing.txt dosyasına 80 adet resim yolu girilecektir. Bu işlemleri kolayca
yapmak için aşağıdaki kod satırlarını kullanabilirsiniz. 

    import os
    direction= os.getcwd()
    file_test=open("lettuce_testing.txt","a+",encoding="utf-8")
    file_train=open("lettuce_training.txt","a+",encoding="utf-8")
    count=1
    while (count<=320):
        file_train.write(r"lettuce_data\lettuce_image\lettuce{}.jpg".format(count)+"\n")
        count+=1
        if count==321:
            while (count<=400):
                 file_test.write(r"lettuce_data\lettuce_image\lettuce{}.jpg".format(count)+"\n")
                 count+=1

<img align="center" src="img/img39.png">

lettuce_data klasörü içerisine iki adet daha dosya oluşturulacaktır. İlk dosyanın ismi lettuce.names 
olacaktır ve bu dosya class ismini barındıracaktır. İkinci dosyanın ismi lettuce.data olacaktır ve bu 
dosya içerisinde modelimiz ile ilgili bilgiler tutulacaktır. Dosyaların isimlerini kaydetmeden önce 
txt dosyası açınız. Daha sonra dosya içeriğini düzenleyip dosya ismini kaydediniz.

<img align="center" src="img/img40.png"><img align="center" src="img/img41.png">

Son olarak lettuce_data klasörümüz aşağıdaki gibi olacaktır.

<img align="center" src="img/img42.png">

Ardından bu lettuce_data klasörünü darknet klasörümüz içerisine atalım.

<img align="center" src="img/img43.png">

Son olarak lettuce_data klasörümüzün içerisine lettuce_labels isminde bir dosya oluşturalım. 
Bu dosya içerisine de etiketleme sonucu oluşan txt dosyalarımızı yükleyelim.

<img align="center" src="img/img44.png">

### ADIM-6: Google Colab Üzerinde Eğitim İşleminin Gerçekleştirilmesi

Darknet dosyamızı sıkıştırarak .zip formatına dönüştürelim. Daha sonra da bu dosyamızı 
Drive'mıza ekleyelim.

<img align="center" src="img/img45.png">

Drive’mızda yeni bir colab projesi oluşturalım. Colab projesinin nasıl oluşturulacağını daha önceki
yazılarımda anlatmıştım. Colab dosyamızın ismi lettuce_model.ipynb olarak değiştirelim. Drive’mıza 
custom_lettuce_model isminde bir klasör oluşturalım ve zip dosyamızı bu klasör içerisine atalım. 
Ardından çalışma zamanından GPU’yu seçerek, bağlantı kurma işlemini tamamlayalım.

<img align="center" src="img/img46.png">

Aşağıdaki kod satırları yazılarak Drive ile bağlantı kurulur. 

    from google.colab import drive
    drive.mount('/content/drive')

<img align="center" src="img/img47.png">

Drive ile bağlantı kurulduğu sol taraftaki bölmeden kontrol edilebilir.

<img align="center" src="img/img48.png">

Sırasıyla aşağıdaki kod satırları yazılarak ubuntu güncellemeleri gerçekleştirilir.

    %cat /etc/lsb-release

<img align="center" src="img/img49.png">

    !apt-get update

<img align="center" src="img/img50.png">

Aşağıdaki kod satırları ile ziplenmiş dosyalarımız çıkartılır. 

# 19. sayfada kaldım.

